import typer
from rich.console import Console
from rich.table import Table
from core.state import get_session, Project, Checkpoint
import datetime

app = typer.Typer(help="NEXUS: The Engineering Kernel")
console = Console()

@app.command()
def boot(
    project_name: str, 
    description: str = "New Nexus Project", 
    api_key: str = None,
    provider: str = "local",
    main_model: str = "deepseek-coder-v2:16b",
    swarm_model: str = "llama3.1:8b"
):
    """
    Load or create a Nexus Project environment.
    """
    session = get_session()
    project = session.query(Project).filter(Project.name == project_name).first()
    
    if not project:
        project = Project(
            name=project_name, 
            description=description, 
            l0_strategy=description, 
            api_key=api_key,
            llm_provider=provider,
            main_model=main_model,
            swarm_model=swarm_model
        )
        session.add(project)
        session.commit()
        console.print(f"[bold green]Created new project:[/bold green] {project_name}")
    else:
        if api_key: project.api_key = api_key
        project.llm_provider = provider
        project.main_model = main_model
        project.swarm_model = swarm_model
        session.commit()
        console.print(f"[bold blue]Booting existing project:[/bold blue] {project_name}")
    
    console.print(f"L0 Strategy: [italic]{project.l0_strategy or 'Not set'}[/italic]")
    console.print(f"Provider: [bold cyan]{project.llm_provider}[/bold cyan]")
    console.print(f"Main Model: [bold magenta]{project.main_model}[/bold magenta]")
    session.close()

@app.command()
def set_strategy(project_name: str, strategy: str):
    """
    Set the L0 Strategy for a project.
    """
    session = get_session()
    project = session.query(Project).filter(Project.name == project_name).first()
    if project:
        project.l0_strategy = strategy
        session.commit()
        console.print(f"[bold green]L0 Strategy updated for {project_name}.[/bold green]")
    else:
        console.print(f"[bold red]Project {project_name} not found.[/bold red]")
    session.close()

@app.command()
def list_projects():
    """
    List all Nexus projects.
    """
    session = get_session()
    projects = session.query(Project).all()
    
    table = Table(title="Nexus Projects")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Created", style="green")
    table.add_column("L0 Strategy", style="yellow")
    
    for p in projects:
        table.add_row(str(p.id), p.name, p.created_at.strftime("%Y-%m-%d"), p.l0_strategy[:50] + "..." if p.l0_strategy else "None")
    
    console.print(table)
    session.close()

from core.kernel import NexusKernel

@app.command()
def chat(user_input: str, project_name: str = "NEXUS_CORE"):
    """
    Autonomously generate an orchestration prompt for a task.
    """
    kernel = NexusKernel(project_name)
    prompt = kernel.get_full_orchestration_prompt(user_input)
    console.print(prompt)

@app.command()
def simulate(query: str, project_name: str = "NEXUS_CORE"):
    """
    Run a MiroFish simulation swarm.
    """
    kernel = NexusKernel(project_name)
    # Auto-pick experts for simulation
    plan = kernel.autonomous_dispatch(query)
    report = kernel.run_pre_execution_simulation(query, [plan["persona"], "testing-reality-checker"])
    console.print(report)

if __name__ == "__main__":
    app()
