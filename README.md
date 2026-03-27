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

## 2. Key Features

### 🧠 Autonomous Dispatcher
NEXUS automatically analyzes your intent (ML, Business, UI, or Testing) and selects the appropriate persona, context tiers, and validation tools without manual intervention.

### 💾 Persistent Mental State
Using a local SQLite database, NEXUS "remembers" your project's L0 Strategy across different terminal sessions and files.

### 🏎️ Hardware-Aware Engineering
Optimized for high-performance hardware, including native support for identifying **RTX 5090 (Blackwell)** and **Jetson Orin Nano** optimization requirements.

---

### 3. Setup & Skill Linking

NEXUS is designed to be a **Stateful Kernel** for your AI CLI (Gemini, Claude, or Agent-Zero).

#### Linking to Gemini CLI
1. **Create Skill Directory:** `mkdir -p ~/.gemini/skills/nexus/scripts`
2. **Link NEXUS:** `ln -s $(pwd)/* ~/.gemini/skills/nexus/scripts/`
3. **Initialize Skill:** Copy the `SKILL.md` (or your spec) to `~/.gemini/skills/nexus/SKILL.md`.
4. **Reload:** Run `/skills reload` in your Gemini CLI.

---

## 4. System Configuration

### 🖥️ Hardware Agnostic Discovery
NEXUS automatically detects your local compute environment.
- **Auto-Detect:** The kernel queries `nvidia-smi` or `tegrastats` to identify your GPU (e.g., Blackwell, Ada, or Orin).
- **Optimization Injection:** It automatically injects relevant hardware-specific constraints (e.g., CUDA vs. MPS vs. NVDLA) into the AI's system prompt.

### 🌐 LLM & API Endpoints
NEXUS supports both local and remote models. To configure your endpoints:
1. Copy the template: `cp .env.example .env`
2. Edit `.env` to set your providers:
   - `NEXUS_LLM_PROVIDER`: `gemini`, `openai`, or `local` (Ollama/vLLM)
   - `NEXUS_API_KEY`: Your provider key.
   - `NEXUS_LOCAL_ENDPOINT`: `http://localhost:11434` (if using Ollama).

---

## 5. Usage
Once linked, NEXUS acts as your autonomous engineering lead:
- `nexus_chat "Task"`: Triggers autonomous orchestration.
- `nexus_simulate "Decision"`: Predicts outcomes using MiroFish swarms.

