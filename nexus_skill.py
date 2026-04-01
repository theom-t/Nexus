import sys
import os

# Ensure the core module is importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.kernel import NexusKernel
from core.state import Project

# Active kernel instance
_kernel = None

def _get_kernel():
    global _kernel
    if not _kernel:
        # Default to NEXUS_CORE or try to detect from environment
        _kernel = NexusKernel("NEXUS_CORE")
    return _kernel

def nexus_boot(project_name: str, strategy: str = None, api_key: str = None, provider: str = "cloud", swarm_model: str = "gemini-1.5-flash"):
    """
    Initializes a NEXUS project. Sets the L0 Strategy.
    - provider: 'cloud' (Gemini) or 'local' (Ollama)
    - swarm_model: The model to use for simulations (e.g., 'llama3.1:8b' for local)
    """
    global _kernel
    _kernel = NexusKernel(project_name)
    
    # Update project config in DB
    session = _kernel.viking.get_session()
    project = session.query(Project).filter(Project.name == project_name).first()
    if project:
        if api_key: project.api_key = api_key
        project.llm_provider = provider
        project.swarm_model = swarm_model
        if strategy: project.l0_strategy = strategy
        session.commit()
    session.close()

    msg = f"Project '{project_name}' booted successfully."
    msg += f"\n- Provider: {provider}"
    msg += f"\n- Swarm Model: {swarm_model}"
    return msg

def nexus_chat(user_request: str, project_name: str = "NEXUS_CORE"):
    """
    The core NEXUS V2 orchestration function. Generates a high-fidelity 
    system prompt with task decomposition and internal auditing.
    """
    kernel = NexusKernel(project_name)
    return kernel.get_full_orchestration_prompt(user_request)

def nexus_clean_prompt(user_request: str):
    """
    The Signal Filter. Returns a 'washed' version of your prompt 
    aligned with NEXUS Constitutional best practices.
    """
    kernel = _get_kernel()
    return kernel.cleaner.get_cleaning_system_prompt() + f"\n\nRAW USER REQUEST: {user_request}"

def nexus_auto(user_request: str):
    """
    THE NATURAL LANGUAGE ENTRY POINT.
    Call this whenever the user asks NEXUS to do something without specifying a project.
    It will auto-boot a temporary session and run the autonomous dispatcher.
    """
    global _kernel
    if not _kernel:
        # Auto-generate a session name based on the request
        project_name = f"AUTO_{user_request[:10].replace(' ', '_')}"
        nexus_boot(project_name, strategy=user_request, provider="local", swarm_model="llama3.1:8b")
    else:
        project_name = _kernel.project_name
    
    # Run the autonomous chat loop
    return nexus_chat(user_request, project_name)

def nexus_simulate(query: str):
    """
    Runs a MiroFish simulation swarm to evaluate a decision.
    """
    kernel = _get_kernel()
    # Auto-pick experts for simulation based on query
    plan = kernel.autonomous_dispatch(query)
    return kernel.run_pre_execution_simulation(query, [plan["persona"], "testing-reality-checker"])

def nexus_simulation(query: str):
    """
    Alias for nexus_simulate as requested by README.md conventions.
    """
    return nexus_simulate(query)
