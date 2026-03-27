from core.state import get_session, Project
from typing import Optional

class VikingDriver:
    """
    Manages Tiered Context (L0, L1, L2) for projects.
    """
    def __init__(self, project_name: str):
        self.project_name = project_name

    def get_session(self):
        return get_session()

    def get_context(self) -> dict:
        """
        Retrieves the full tiered context for the project.
        """
        session = get_session()
        project = session.query(Project).filter(Project.name == self.project_name).first()
        
        if not project:
            session.close()
            return {"l0": None, "l1": None}
        
        context = {
            "l0": project.l0_strategy,
            "l1": project.l1_architecture
        }
        session.close()
        return context

    def update_l0(self, strategy: str):
        session = get_session()
        project = session.query(Project).filter(Project.name == self.project_name).first()
        if project:
            project.l0_strategy = strategy
            session.commit()
        session.close()

    def update_l1(self, architecture: str):
        session = get_session()
        project = session.query(Project).filter(Project.name == self.project_name).first()
        if project:
            project.l1_architecture = architecture
            session.commit()
        session.close()

    def format_for_prompt(self) -> str:
        """
        Returns a formatted string of the context to be injected into an LLM prompt.
        """
        ctx = self.get_context()
        prompt = "--- NEXUS TIERED CONTEXT ---\n"
        if ctx['l0']:
            prompt += f"[L0 STRATEGY]:\n{ctx['l0']}\n\n"
        if ctx['l1']:
            prompt += f"[L1 ARCHITECTURE]:\n{ctx['l1']}\n"
        prompt += "----------------------------"
        return prompt

if __name__ == "__main__":
    # Quick test
    viking = VikingDriver("NEXUS_CORE")
    viking.update_l0("Build the ultimate engineering shell.")
    viking.update_l1("Use a Python-based dispatcher with SQLite persistence.")
    print(viking.format_for_prompt())
