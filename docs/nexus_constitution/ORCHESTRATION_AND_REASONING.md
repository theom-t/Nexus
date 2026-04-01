# NEXUS CONSTITUTION: ORCHESTRATION & REASONING

These rules govern internal agent dialogue and "Reasoning Layers" (CoT, Reflexion, and Verification).

## 1. Agent-to-Agent Communication (Internal Dialogue)
When agents talk to each other in a simulation or orchestration chain:
- **Concise Signal:** Only share relevant observations or tool outputs. Avoid polite filler or repetition.
- **Explicit Handoff:** Always state the next action and who should perform it (e.g., "Handing off to Researcher for domain verification").
- **Filtered Output:** Pass all internal agent outputs through the `nexus_clean_prompt` logic to ensure technical rigor is maintained.

## 2. Advanced Reasoning Chains
When a complex task is detected (ML optimization, Architecture design):
- **Native Chain-of-Thought (CoT):** Encourage the model to think "out loud" about its reasoning. Use "Let's think step-by-step" for any task involving logic or math.
- **Tree-of-Thought (ToT):** For high-stakes decisions (e.g., pivot or architecture choice), require the model to explore 3 distinct expert paths before selecting one.
- **Reflexion Layer:** After generating a solution, the model MUST perform a "Logic-Audit":
  1. Identify potential failure points.
  2. Contrast the output with the L0 Strategy.
  3. Propose one refinement before final delivery.

## 3. The Validation Protocol
- **Promptfoo Integration:** All critical code must include logic assertions for `promptfoo` (e.g., "Function must handle null inputs without crashing").
- **Reality Check:** Include a specialized "Pessimist" persona in every MiroFish simulation to point out edge-case failures.
- **Hardware Audit:** If code is being generated for the RTX 5090 or Jetson Orin Nano, the reasoning MUST check for driver compatibility (CUDA 12.8/13.0).

## 4. Error Recovery (Self-Healing)
- **Retry Logic:** If a tool call fails, rephrase the query once.
- **Fail-Fast:** If 50% of the internal agents fail, the orchestrator MUST alert the human and stop the loop rather than guessing.
