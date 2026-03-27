import subprocess
import os
import json
import yaml

class PromptfooDriver:
    """
    Runs automated evaluations on AI output using promptfoo.
    Ensures that generated code/plans meet specific engineering assertions.
    """
    def __init__(self, repos_path: str = "/home/tmainetucker/Repos/nexus/repos/promptfoo"):
        self.repos_path = os.path.abspath(repos_path)

    def validate_output(self, prompt: str, output: str, assertions: list) -> dict:
        """
        Runs an actual promptfoo check against the output.
        """
        # 1. Prepare the config
        config = {
            "prompts": [prompt],
            "providers": ["echo"], # We use echo because we already have the output
            "tests": [
                {
                    "vars": {"output": output},
                    "assert": [{"type": "icontains", "value": a} for a in assertions]
                }
            ]
        }
        
        config_path = os.path.join(self.repos_path, "temp_config.yaml")
        with open(config_path, "w") as f:
            yaml.dump(config, f)

        # 2. Run the eval
        try:
            cmd = ["npx", "promptfoo", "eval", "-c", "temp_config.yaml", "--output", "results.json"]
            subprocess.run(cmd, cwd=self.repos_path, capture_output=True, check=True)
            
            # 3. Parse results
            results_path = os.path.join(self.repos_path, "results.json")
            with open(results_path, "r") as f:
                data = json.load(f)
                
            success = data["summary"]["numFailed"] == 0
            return {
                "success": success,
                "passed": data["summary"]["numPassed"],
                "failed": data["summary"]["numFailed"],
                "report": "Promptfoo analysis completed: " + ("PASS" if success else "FAIL")
            }
        except Exception as e:
            return {"success": False, "report": f"Promptfoo Error: {str(e)}"}

    def get_assertion_prompt(self, requirements: list) -> str:
        """
        Informs the LLM that its output will be tested against these specific requirements.
        """
        req_str = "\n- ".join(requirements)
        return f"\n\n[VALIDATION GATE]: Your response will be audited against the following requirements:\n- {req_str}"

if __name__ == "__main__":
    # Quick test
    driver = PromptfooDriver()
    print(driver.get_assertion_prompt(["Must use CuPy", "Must include error handling"]))
