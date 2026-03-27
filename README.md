# NEXUS: The Engineering Kernel
**"The Ultimate Stateful Engineering Shell"**

NEXUS is an autonomous, stateful orchestrator designed to bridge high-level **Business Strategy** with rigorous **Technical Implementation**. It treats every prompt as an engineering task, passing it through a pipeline of simulation, expert delegation, and automated validation.

---

## 1. Core Philosophy: "The Integrated Kernel"
NEXUS acts as a **Dispatcher** that synchronizes five specialized engineering "drivers" into a single, autonomous execution loop.

| Layer | Component | Integrated Repository | Role |
| --- | --- | --- | --- |
| **Context** | **Memory** | [OpenViking](https://github.com/volcengine/OpenViking) | Tiered Context: **L0 (Strategy)**, **L1 (Architecture)**, **L2 (Code)**. |
| **Routing** | **Personas** | [Agency-Agents](https://github.com/msitarzewski/agency-agents) | Loads specialized experts (e.g., *ML Engineer*, *Growth Hacker*). |
| **Simulation** | **Predictive** | [MiroFish](https://github.com/666ghj/MiroFish) | Runs "Swarm Simulations" to test logic or business impact. |
| **Design** | **Aesthetics** | [Impeccable](https://github.com/pbakaus/impeccable) | Enforces OKLCH colors and professional UI/UX standards. |
| **Validation** | **Quality** | [Promptfoo](https://github.com/promptfoo/promptfoo) | Automated unit tests for AI output requirements. |

---

## 2. Step-by-Step Setup

### A. Clone the Repository
NEXUS uses **Git Submodules**. You must use the `--recursive` flag to pull the integrated repositories.
```bash
git clone --recursive https://github.com/theom-t/Nexus.git
cd Nexus
```

### B. Environment Setup (Isolated)
We recommend using **Mamba** or **Conda** to keep your system clean.
```bash
# 1. Create the environment
mamba create -n nexus python=3.12 -y
mamba activate nexus

# 2. Install core dependencies
mamba install sqlalchemy typer rich python-dotenv -y

# 3. Install NVIDIA metrics library (Required for Hardware Discovery)
pip install nvidia-ml-py
```

### C. Configuration (.env)
NEXUS needs to know which LLMs to use.
```bash
# Copy the template
cp .env.example .env

# Open .env and add your API keys (Gemini, OpenAI, etc.)
# If using local models (Ollama), ensure your local endpoint is set.
```

---

## 3. Linking to your AI CLI (Gemini CLI)

To use NEXUS as a "Skill" inside your terminal:

1. **Create the Skill Folder:**
   ```bash
   mkdir -p ~/.gemini/skills/nexus/scripts
   ```
2. **Link the NEXUS files:**
   ```bash
   # Run this inside the Nexus/ directory you cloned
   ln -s $(pwd)/* ~/.gemini/skills/nexus/scripts/
   ```
3. **Register the Skill:**
   Copy the `NEXUS_SPEC.md` to the skill root so Gemini can "read" the instructions:
   ```bash
   cp NEXUS_SPEC.md ~/.gemini/skills/nexus/SKILL.md
   ```
4. **Reload Gemini:**
   Open your Gemini CLI and type `/skills reload`. You should see `nexus` in the list.

---

## 4. Hardware Agnostic Discovery
NEXUS automatically detects your local compute environment (RTX Desktop, Jetson Orin, or CPU).
- **Desktop:** Uses `nvidia-smi` to optimize for VRAM and CUDA versions.
- **Jetson:** Detects `tegrastats` to prioritize NVDLA and power efficiency.
- **Generic:** Falls back to standard CPU/OS-level optimizations.

---

## 5. First Steps (Try these!)

1. **Boot a Project:**
   ```bash
   mamba run -n nexus python nexus.py boot "MyProject" --description "Build a SaaS."
   ```
2. **Autonomous Chat:**
   In your Gemini CLI, ask: 
   > *"Run a nexus_chat to design a React dashboard for my new project."*
3. **Run a Simulation:**
   In your Gemini CLI, ask:
   > *"Run a nexus_simulation to see the impact of 1000 users on my current architecture."*

---

## 6. Attribution
NEXUS is a synthesis of several incredible open-source projects. We thank the authors of OpenViking, Agency-Agents, MiroFish, Impeccable, and Promptfoo for their foundational work.
