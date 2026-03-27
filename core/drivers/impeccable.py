import os

class ImpeccableDriver:
    """
    Enforces design standards using the Impeccable framework.
    Provides "Design Guardrails" for UI/UX output.
    """
    def __init__(self, repos_path: str = "/home/tmainetucker/Repos/nexus/repos/impeccable"):
        self.repos_path = os.path.abspath(repos_path)
        # Impeccable stores its main design rules in markdown files
        self.rules_path = os.path.join(self.repos_path, "dist")

    def get_design_system_context(self) -> str:
        """
        Loads the core design system rules (e.g., OKLCH, Typography).
        """
        # Try to load the main reference file
        ref_file = os.path.join(self.rules_path, "reference.md")
        if not os.path.exists(ref_file):
            # Fallback to listing what's in dist/ if reference.md isn't there
            return "IMPECCABLE DESIGN RULES: Use OKLCH colors, fluid typography, and professional easing."
            
        with open(ref_file, 'r') as f:
            return f.read()

    def audit_prompt(self) -> str:
        """
        Returns a prompt suffix to force Gemini to audit its UI design.
        """
        return (
            "\n\n[IMPECCABLE AUDIT]: "
            "Ensure the generated UI uses OKLCH colors for better accessibility and "
            "professional contrast. Apply fluid typography and ensure interactive "
            "elements have polished easing curves."
        )

if __name__ == "__main__":
    # Quick test
    driver = ImpeccableDriver()
    print("Design System Context (truncated):")
    print(driver.get_design_system_context()[:300] + "...")
