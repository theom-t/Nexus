# NEXUS: The Engineering Kernel
**"The Ultimate Stateful Engineering Shell"**

NEXUS is a stateful orchestrator designed to bridge high-level **Business Strategy** with rigorous **Technical Implementation**. It treats every prompt as an engineering task, passing it through a pipeline of simulation, expert delegation, and automated validation.

---

## 1. Core Philosophy: "The Integrated Kernel"
NEXUS is not a chatbot; it is a **Dispatcher** that synchronizes five specialized repository "drivers" into a single execution loop.

| Layer | Component | Repository | Role |
| --- | --- | --- | --- |
| **Context** | **Memory** | `OpenViking` | Manages project tiers: **L0 (Strategy)**, **L1 (Architecture)**, **L2 (Code)**. |
| **Routing** | **Personas** | `agency-agents` | Loads specialized expert sheets (e.g., *ML Engineer*, *Business Strategist*). |
| **Simulation** | **Predictive** | `MiroFish` | Runs "Swarm Simulations" to test logic or business impact before execution. |
| **Design** | **Aesthetics** | `impeccable` | Enforces OKLCH colors and professional UI/UX standards for apps. |
| **Validation** | **Quality** | `promptfoo` | Runs unit tests on AI output to ensure engineering requirements are met. |

---

## 2. System Specifications

### A. The "Mental State" (SQLite Persistence)
NEXUS uses a local SQLite database to maintain continuity across sessions.
*   **Active Project:** Pins the current L0/L1 context.
*   **Checkpointing:** Saves code diffs, agent "thoughts," and simulation reports.
*   **Hardware Profiles:** Stores environment-specific flags (e.g., `RTX_5090_BLACKWELL` vs. `JETSON_ORIN_NANO`).

### B. The Dispatcher Loop
1.  **Boot:** `nexus boot <project>` loads the tiered context from OpenViking.
2.  **Analyze:** Gemini identifies the necessary specialists from `agency-agents`.
3.  **Simulate:** For complex tasks, **MiroFish** generates a "Logic Swarm" report.
4.  **Execute:** Code or plans are generated, "pinned" to the L0 Strategy.
5.  **Audit:** **Impeccable** (for UI) or **Promptfoo** (for logic) validates the output.

---

## 3. Key Use Cases

### High-Level Business Strategy
*   **Market Analysis:** Using the *Strategist* persona to find "Best Strategies" for current markets.
*   **Profitability Simulation:** Running MiroFish swarms to project the impact of different monetization models.

### Machine Learning & Backend
*   **Hardware-Aware Dev:** Automatic injection of CUDA/CuPy optimizations for the RTX 5090.
*   **Pipeline Engineering:** Designing data hygiene rules (e.g., "45-day Macro lag") as L1 Architectural constraints.

### Application Development
*   **Fluid UI:** Automatically piping React/CSS through the **Impeccable** auditor for professional-grade aesthetics.
*   **Stateful Apps:** Building backends that respect the NEXUS "Mental State" architecture.

---

## 4. Technical Stack
*   **CLI Framework:** Python (Typer) + Rich (Terminal UI).
*   **Orchestrator:** Asyncio (for non-blocking simulations).
*   **Database:** SQLAlchemy + SQLite.
*   **Gemini Integration:** Registered as a **Gemini CLI Skill**, providing real-time tool access to the NEXUS Kernel.

---

## 5. Success Metrics
*   **Context Continuity:** Can the AI recall the L0 Strategy while writing an L2 function three days later?
*   **Zero-Guess Execution:** Does the MiroFish simulation correctly predict bottlenecks before code is run?
*   **Engineering Rigor:** Does every output pass the Promptfoo "Reality Check"?
