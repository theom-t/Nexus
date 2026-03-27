import os
import glob
from typing import List, Dict

class AgencyDriver:
    def __init__(self, repos_path: str = "/home/tmainetucker/Repos/nexus/repos/agency-agents"):
        self.repos_path = os.path.abspath(repos_path)
        self.personas_path = self.repos_path

    def list_personas(self) -> List[str]:
        """
        Returns a list of all available personas found in the agency-agents repository.
        """
        # Look for .md files in the entire repo/ folder, excluding readme and contributing
        md_files = glob.glob(os.path.join(self.personas_path, "**/*.md"), recursive=True)
        # Filter out generic repo files
        exclude = ["README.md", "CONTRIBUTING.md", "LICENSE.md"]
        return [os.path.basename(f).replace(".md", "") for f in md_files if os.path.basename(f) not in exclude]

    def load_persona(self, persona_name: str) -> str:
        """
        Loads the markdown content of a specific persona.
        """
        # Search for the file in the agents/ folder
        search_pattern = os.path.join(self.personas_path, f"**/{persona_name}.md")
        files = glob.glob(search_pattern, recursive=True)
        
        if not files:
            raise FileNotFoundError(f"Persona '{persona_name}' not found in {self.personas_path}")
        
        with open(files[0], 'r', encoding='utf-8') as f:
            return f.read()

    def format_as_system_prompt(self, persona_name: str) -> str:
        """
        Wraps the persona content in a system-friendly prompt block.
        """
        content = self.load_persona(persona_name)
        return f"SYSTEM ROLE LOADED FROM AGENCY-AGENTS ({persona_name}):\n\n{content}"

if __name__ == "__main__":
    # Quick test
    driver = AgencyDriver()
    try:
        personas = driver.list_personas()
        print(f"Available personas: {personas[:10]}... ({len(personas)} total)")
        if personas:
            test_persona = personas[0]
            print(f"\nLoading '{test_persona}':")
            print(driver.load_persona(test_persona)[:200] + "...")
    except Exception as e:
        print(f"Error: {e}")
