from core.state import get_session, Project, Checkpoint
import subprocess
import os
import json
import datetime
from typing import List

class MiroFishDriver:
    """
    Manages Simulation Swarms using the real MiroFish engine.
    Ensures high agent activity and hardware efficiency.
    """
    def __init__(self, project_name: str, repos_path: str = "/home/tmainetucker/Repos/nexus/repos/MiroFish"):
        self.project_name = project_name
        self.repos_path = os.path.abspath(repos_path)
        self.backend_path = os.path.join(self.repos_path, "backend")

    def run_simulation(self, query: str, personas: List[str]) -> str:
        """
        Autonomously generates a simulation config and executes it.
        """
        from openai import OpenAI
        
        # 1. Setup Local Environment
        provider = "local"
        base_url = "http://localhost:11434/v1"
        api_key = "ollama"
        model = "llama3.1:8b"
        
        # 2. Use Gemini/Local to design the EXPERTS and TRIGGER
        client = OpenAI(api_key=api_key, base_url=base_url)
        
        design_prompt = (
            f"Given this research task: '{query}', identify 3 specialized expert personas "
            "who would have a high-stakes debate about it. For each expert, provide a name and "
            "a 1-sentence persona. Also, provide a 'Trigger Post' for Twitter and Reddit to start the debate. "
            "Return ONLY a JSON object: "
            "{'experts': [{'name': '...', 'persona': '...'}], 'twitter_trigger': '...', 'reddit_trigger': '...'}"
        )
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": design_prompt}],
                response_format={"type": "json_object"},
                extra_body={"keep_alive": 0}
            )
            design = json.loads(response.choices[0].message.content)
        except Exception:
            # Fallback if LLM fails to return valid JSON
            design = {
                "experts": [{"name": p, "persona": f"Expert in {p}"} for p in personas[:3]],
                "twitter_trigger": f"Debate: {query}",
                "reddit_trigger": f"Which is best: {query}?"
            }

        # 3. CONSTRUCT the config (Hard-coded stability)
        all_hours = list(range(0, 24))
        config = {
            "simulation_id": f"nexus_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "project_id": self.project_name,
            "simulation_requirement": query,
            "time_config": {
                "total_simulation_hours": 24,
                "minutes_per_round": 30,
                "agents_per_hour_min": 5,
                "agents_per_hour_max": 10,
                "peak_hours": all_hours,
                "peak_activity_multiplier": 2.0
            },
            "agent_configs": [],
            "event_config": {
                "initial_posts": [
                    {"content": design["twitter_trigger"], "platform": "twitter", "poster_agent_id": 0, "poster_type": "Person"},
                    {"content": design["reddit_trigger"], "platform": "reddit", "poster_agent_id": 1, "poster_type": "Person"}
                ]
            },
            "llm_model": model,
            "llm_base_url": base_url
        }

        # Populate agents with guaranteed activity
        for i, expert in enumerate(design["experts"]):
            config["agent_configs"].append({
                "agent_id": i,
                "entity_name": expert["name"],
                "entity_type": "Person",
                "persona": expert["persona"],
                "activity_level": 1.0,
                "posts_per_hour": 10,
                "active_hours": all_hours
            })

        # 4. Save config and setup .env
        config_path = os.path.join(self.backend_path, "nexus_sim_config.json")
        with open(config_path, "w") as f:
            json.dump(config, f, indent=2)

        with open(os.path.join(self.backend_path, ".env"), "w") as f:
            f.write(f"LLM_API_KEY={api_key}\n")
            f.write(f"LLM_BASE_URL={base_url}\n")
            f.write(f"LLM_MODEL_NAME={model}\n")
            f.write("CAMEL_AGENT_LOG_LEVEL=INFO\n")
            f.write("OLLAMA_KEEP_ALIVE=0\n")

        # 5. Generate Profile Files
        import csv
        with open(os.path.join(self.backend_path, "twitter_profiles.csv"), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['user_id', 'name', 'username', 'user_char', 'description'])
            for a in config["agent_configs"]:
                writer.writerow([a['agent_id'], a['entity_name'], f"user_{a['agent_id']}", a['persona'], "Expert"])

        with open(os.path.join(self.backend_path, "reddit_profiles.json"), 'w') as f:
            reddit_profiles = []
            for a in config["agent_configs"]:
                reddit_profiles.append({
                    "user_id": a['agent_id'], "username": f"user_{a['agent_id']}", "name": a['entity_name'],
                    "bio": a['persona'][:150], "persona": a['persona'], "realname": a['entity_name'],
                    "karma": 1000, "created_at": "2024-01-01", "age": 30, "gender": "other", "mbti": "INTJ", "country": "UK"
                })
            json.dump(reddit_profiles, f, indent=2)

        # 6. RUN
        try:
            cmd = ["mamba", "run", "-n", "nexus", "python", "scripts/run_parallel_simulation.py", "--config", "nexus_sim_config.json", "--no-wait", "--max-rounds", "20"]
            subprocess.run(cmd, cwd=self.backend_path, capture_output=True, text=True, check=True)
            
            # 7. EXTRACT DEBATE CONTENT (The Real Intelligence)
            report = f"--- MIROFISH COUNCIL OF EXPERTS DEBATE ---\nQUERY: {query}\n\n"
            
            platforms = ["twitter", "reddit"]
            for platform in platforms:
                actions_path = os.path.join(self.backend_path, platform, "actions.jsonl")
                if os.path.exists(actions_path):
                    report += f"[{platform.upper()} DISCUSSIONS]:\n"
                    with open(actions_path, "r") as f:
                        for line in f:
                            try:
                                data = json.loads(line)
                                if data.get("action_type") == "CREATE_POST":
                                    agent = data.get("agent_name", "Expert")
                                    content = data.get("action_args", {}).get("content", "")
                                    report += f"- {agent}: \"{content}\"\n"
                            except Exception: continue
                    report += "\n"

            return report
        except subprocess.CalledProcessError as e:
            return f"MiroFish Error: {e.stderr}"

if __name__ == "__main__":
    fish = MiroFishDriver("NEXUS_CORE")
    print(fish.run_simulation("Test the improved activity logic.", ["Architect"]))
