import os
import glob
from typing import Dict, Any

class CleanerDriver:
    """
    The Signal Filter for NEXUS. 
    Washes raw input through the NEXUS Constitution to ensure technical rigor.
    """
    def __init__(self, constitution_path: str = "docs/nexus_constitution"):
        self.constitution_path = os.path.abspath(constitution_path)
        self.rules = self._load_constitution()

    def _load_constitution(self) -> str:
        """Loads all markdown files from the constitution folder into a single reference string."""
        content = "--- NEXUS CONSTITUTION ---\n"
        md_files = glob.glob(os.path.join(self.constitution_path, "*.md"))
        for f_path in md_files:
            with open(f_path, 'r') as f:
                content += f"\nFILE: {os.path.basename(f_path)}\n"
                content += f.read() + "\n"
        return content

    def get_cleaning_system_prompt(self) -> str:
        """Generates the system prompt for the cleaning LLM."""
        return (
            "You are the NEXUS Signal Filter. Your sole purpose is to 'wash' raw user requests "
            "into high-fidelity engineering instructions based on the NEXUS CONSTITUTION provided below.\n\n"
            f"{self.rules}\n\n"
            "MANDATE: \n"
            "1. De-noise the request (remove vague terms like 'make it good').\n"
            "2. Inject mandatory delimiters (<user_request>, <context>).\n"
            "3. Enforce the Instruction-Context-Input-Output structure.\n"
            "4. Match the request against SITUATIONAL TRIGGERS and inject missing technical constraints (e.g., OKLCH for UI, CUDA 12.8 for ML).\n"
            "5. Return ONLY the cleaned prompt. No chat, no preamble."
        )

    def clean(self, raw_input: str, context: Dict[str, Any] = None) -> str:
        """
        Uses an LLM to clean the prompt. 
        Note: In a real implementation, this would call the configured NEXUS LLM.
        For now, it returns the instructions for how the prompt SHOULD be cleaned
        if the calling agent is the one doing the cleaning.
        """
        # This acts as a 'wrapper' that ensures the next layer follows the constitution
        clean_template = (
            f"--- NEXUS CLEANING PROTOCOL ACTIVATED ---\n"
            f"RAW INPUT: {raw_input}\n"
            f"CONTEXT: {context}\n"
            f"APPLYING CONSTITUTIONAL LAWS...\n"
            "------------------------------------------\n"
        )
        return clean_template
