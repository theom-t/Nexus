from core.drivers.agency import AgencyDriver
from core.drivers.viking import VikingDriver
from core.drivers.fish import MiroFishDriver
from core.drivers.impeccable import ImpeccableDriver
from core.drivers.promptfoo import PromptfooDriver
from core.drivers.researcher import ResearcherDriver
from core.drivers.profiler import HardwareProfiler
from core.drivers.memory import VectorMemory

class NexusKernel:
    """
    The Orchestrator that binds all 7 drivers together.
    """
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.agency = AgencyDriver()
        self.viking = VikingDriver(project_name)
        self.fish = MiroFishDriver(project_name)
        self.design = ImpeccableDriver()
        self.validator = PromptfooDriver()
        self.researcher = ResearcherDriver()
        self.profiler = HardwareProfiler()
        self.memory = VectorMemory()

    def autonomous_dispatch(self, user_input: str) -> dict:
        """
        Analyzes user input and automatically decides which tools, 
        personas, and context are required.
        """
        plan = {
            "intent": "unknown",
            "persona": "engineering-senior-developer",
            "tools": [],
            "simulation_required": False,
            "research_required": False,
            "consensus_required": False,
            "models": {
                "leader": "Gemini 3 Pro (Cloud)", 
                "architect": "deepseek-coder-v2:16b (Local)",
                "swarm": "llama3.1:8b (Local)",
                "researcher": "mistral-nemo (Local)"
            }
        }

        # 1. Detect Intent & Persona (Refined Priority)
        input_lower = user_input.lower()
        
        if any(word in input_lower for word in ["business", "strategy", "market", "profit", "monetize", "saas", "business idea"]):
            plan["intent"] = "business_strategy"
            plan["persona"] = "marketing-growth-hacker"
            plan["research_required"] = True # Always research business
            plan["consensus_required"] = True # High stakes
        elif any(word in input_lower for word in ["ui", "frontend", "react", "css", "design", "html", "dashboard", "mvp", "app"]):
            plan["intent"] = "ui_development"
            plan["persona"] = "engineering-frontend-developer"
        elif any(word in input_lower for word in ["ml", "ai ", "machine learning", "gpu", "cuda", "rtx", "blackwell"]):
            plan["intent"] = "machine_learning"
            plan["persona"] = "engineering-ai-engineer"
            plan["consensus_required"] = True # Engineering needs double check
        
        # 2. Add Tools
        plan["tools"].append("OpenViking")
        plan["tools"].append("Promptfoo")
        
        if plan["research_required"]: plan["tools"].append("Researcher")
        if plan.get("simulation_required") or "simulate" in input_lower:
            plan["simulation_required"] = True
            plan["tools"].append("MiroFish")
        if plan["intent"] == "ui_development":
            plan["tools"].append("Impeccable")

        return plan

    def get_full_orchestration_prompt(self, user_input: str) -> str:
        """
        Autonomously synthesizes the full system prompt based on user input.
        """
        plan = self.autonomous_dispatch(user_input)
        
        # 1. Load Persona
        persona_content = self.agency.format_as_system_prompt(plan["persona"])
        
        # 2. Inject Context & Memory
        context_content = self.viking.format_for_prompt()
        past_memories = self.memory.recall(user_input)
        
        # 3. Optional: Perform Live Research
        research_data = ""
        if plan["research_required"]:
            research_data = self.researcher.search_and_scrape(user_input)
            
        # 4. Hardware Profiling
        hw_status = self.profiler.format_for_prompt()
        
        # 5. Build Orchestration Header
        orchestration_msg = f"--- NEXUS HYBRID ORCHESTRATION ---\n"
        orchestration_msg += f"INTENT: {plan['intent']}\n"
        orchestration_msg += f"PERSONA: {plan['persona']}\n"
        orchestration_msg += f"COUNCIL OF EXPERTS:\n"
        orchestration_msg += f"  - LEADER: {plan['models']['leader']}\n"
        orchestration_msg += f"  - ARCHITECT: {plan['models']['architect']}\n"
        orchestration_msg += f"  - RESEARCHER: {plan['models']['researcher']}\n"
        orchestration_msg += f"  - SWARM ENGINE: {plan['models']['swarm']}\n"
        
        if plan["consensus_required"]:
            orchestration_msg += "CONSENSUS MANDATE: The Local Architect and Cloud Leader must reach agreement.\n"
        orchestration_msg += "----------------------------------\n\n"
        
        full_prompt = f"{persona_content}\n\n{context_content}\n\n{past_memories}\n\n{research_data}\n\n{hw_status}\n\n{orchestration_msg}\n\nUSER REQUEST: {user_input}"
        
        # 6. Tool Guardrails
        if "Impeccable" in plan["tools"]: full_prompt += self.design.audit_prompt()
        full_prompt += self.validator.get_assertion_prompt(["Adhere to L0 Strategy", "Technical Feasibility Verified"])
        
        # 7. Remember this task
        self.memory.remember(self.project_name, user_input, {"type": "user_request"})
            
        return full_prompt

    def run_pre_execution_simulation(self, query: str, personas: list) -> str:
        """
        Runs a MiroFish simulation before any code is generated.
        """
        return self.fish.run_simulation(query, personas)

if __name__ == "__main__":
    # Test Autonomous Orchestration
    kernel = NexusKernel("NEXUS_CORE")
    
    print("--- TESTING AUTONOMOUS DISPATCH (UI) ---")
    orchestrated_prompt = kernel.get_full_orchestration_prompt("Build a modern React dashboard with OKLCH colors.")
    print(orchestrated_prompt[:300] + "...")
    
    print("\n--- TESTING AUTONOMOUS DISPATCH (ML) ---")
    orchestrated_prompt = kernel.get_full_orchestration_prompt("Optimize the VMD script for Blackwell RTX 5090.")
    print(orchestrated_prompt[:300] + "...")
