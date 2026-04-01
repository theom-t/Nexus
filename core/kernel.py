from core.drivers.agency import AgencyDriver
from core.drivers.viking import VikingDriver
from core.drivers.fish import MiroFishDriver
from core.drivers.impeccable import ImpeccableDriver
from core.drivers.promptfoo import PromptfooDriver
from core.drivers.researcher import ResearcherDriver
from core.drivers.profiler import HardwareProfiler
from core.drivers.memory import VectorMemory
from core.drivers.cleaner import CleanerDriver
import json

class NexusKernel:
    """
    The Orchestrator that binds all 8 drivers together.
    Upgraded to NEXUS V2 (Deep Agent Logic).
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
        self.cleaner = CleanerDriver()

    def autonomous_dispatch(self, user_input: str) -> dict:
        """
        NEXUS V2: Analyzes user input, performs TASK DECOMPOSITION, 
        and decides on reasoning effort.
        """
        # 1. Start with high-level intent
        plan = {
            "intent": "unknown",
            "persona": "engineering-senior-developer",
            "tasks": [],
            "reasoning_effort": "medium",
            "tools": ["OpenViking", "Promptfoo", "Cleaner"],
            "models": {
                "leader": "Gemini 3 Pro (Cloud)", 
                "architect": "deepseek-coder-v2:16b (Local)",
                "swarm": "llama3.1:8b (Local)"
            }
        }

        input_lower = user_input.lower()
        
        # 2. Task Decomposition logic (V2)
        if any(word in input_lower for word in ["business", "strategy", "market", "monetize"]):
            plan["intent"] = "business_strategy"
            plan["persona"] = "marketing-growth-hacker"
            plan["reasoning_effort"] = "high"
            plan["tasks"] = ["Market Research", "Financial Simulation", "ROI Logic Audit"]
            plan["tools"].extend(["Researcher", "MiroFish"])
        elif any(word in input_lower for word in ["ui", "frontend", "react", "css", "design"]):
            plan["intent"] = "ui_development"
            plan["persona"] = "engineering-frontend-developer"
            plan["tasks"] = ["Asset Selection", "OKLCH Styling", "Micro-interaction Design"]
            plan["tools"].append("Impeccable")
        elif any(word in input_lower for word in ["ml", "ai ", "gpu", "cuda", "blackwell"]):
            plan["intent"] = "machine_learning"
            plan["persona"] = "engineering-ai-engineer"
            plan["reasoning_effort"] = "high"
            plan["tasks"] = ["Hardware Profiling", "Kernel Optimization", "Memory Benchmarking"]
            plan["tools"].append("Researcher")

        return plan

    def get_full_orchestration_prompt(self, user_input: str) -> str:
        """
        NEXUS V2: Recursive Signal Filtering and Layered Context.
        """
        # 1. WASH through Cleaner Driver (System Layer)
        pre_cleaned_msg = self.cleaner.get_cleaning_system_prompt()
        
        # 2. Run Autonomous Dispatch (Task Layer)
        plan = self.autonomous_dispatch(user_input)
        
        # 3. Load Persona & Hardware (Hardware Profile)
        persona_content = self.agency.format_as_system_prompt(plan["persona"])
        hw_status = self.profiler.format_for_prompt()
        
        # 4. Inject Hierarchical Context (Memory Layer)
        context_content = self.viking.format_for_prompt()
        past_memories = self.memory.recall(user_input)
        
        # 5. Build NEXUS V2 Header
        orchestration_msg = f"--- NEXUS V2 DEEP ORCHESTRATION ---\n"
        orchestration_msg += f"INTENT: {plan['intent']}\n"
        orchestration_msg += f"REASONING EFFORT: {plan['reasoning_effort'].upper()}\n"
        orchestration_msg += f"TASK PLAN: {json.dumps(plan['tasks'])}\n"
        orchestration_msg += f"COUNCIL OF EXPERTS: Leader({plan['models']['leader']}), Architect({plan['models']['architect']})\n"
        orchestration_msg += "------------------------------------\n\n"
        
        # 6. Apply Internal Shadow Auditor (Validation Layer)
        audit_mandate = (
            "\n### INTERNAL AUDIT MANDATE ###\n"
            "An internal Shadow Auditor persona is active. Before final output, "
            "you MUST identify one potential 'failure point' in your logic and provide a self-correction."
        )
        
        full_prompt = (
            f"{pre_cleaned_msg}\n\n"
            f"{persona_content}\n\n"
            f"{orchestration_msg}\n\n"
            f"{context_content}\n\n"
            f"{past_memories}\n\n"
            f"{hw_status}\n\n"
            f"USER REQUEST: <user_request>{user_input}</user_request>\n\n"
            f"{audit_mandate}"
        )
        
        # Tool Guardrails
        if "Impeccable" in plan["tools"]: full_prompt += self.design.audit_prompt()
        full_prompt += self.validator.get_assertion_prompt(["Adhere to L0 Strategy", "Technical Feasibility Verified"])
        
        # Memory Compression (Mental State Update)
        self.memory.remember(self.project_name, user_input, {"type": "v2_orchestration", "intent": plan["intent"]})
            
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
