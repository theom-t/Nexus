# NEXUS CONSTITUTION: SITUATIONAL TRIGGERS

Use these specific rule sets to "inject" missing context when the following keywords or intents are detected.

## SITUATION: Machine Learning / GPU
- **Detection:** `ML`, `AI`, `GPU`, `CUDA`, `RTX`, `Blackwell`, `Orin`.
- **Injection:**
  - Hardware Profile (RTX 5090 or Jetson Orin Nano).
  - Optimization Mandate: "Use `tf-nightly` or `pytorch-nightly` compat; manage `LD_LIBRARY_PATH`."
  - "Prefer CuPy for batch-accelerated operations on RTX 5090."
  - Memory Constraint: "Explicitly handle VRAM allocation and batch size logic."

## SITUATION: UI / Frontend
- **Detection:** `UI`, `React`, `CSS`, `Design`, `Dashboard`, `Dashboard`, `MVP`.
- **Injection:**
  - **Aesthetic Law:** "Enforce OKLCH color spaces; use `oklch()` for all styling."
  - "Prefer Vanilla CSS or Radix primitives over Tailwind (unless user requested)."
  - "Inject micro-interactions: hover states, transitions, and loading skeletons."
  - "Accessibility Check: Ensure ARIA labels and keyboard focus logic are included."

## SITUATION: Deep Research / Market Analysis
- **Detection:** `Research`, `Latest`, `Market`, `Competitors`, `Compare`, `Report`.
- **Injection:**
  - "Decompose query into 3-5 specific search subtasks."
  - "Execute search worker for EACH task; do not skip silently."
  - "Mandate Citations: Every claim must be backed by a cited source URL."
  - "Date Filter: Only use sources from the last [X] months."

## SITUATION: Business Strategy / SaaS
- **Detection:** `Business`, `Monetize`, `Profit`, `SaaS`, `Marketing`.
- **Injection:**
  - Load "Growth Hacker" or "Business Strategist" persona from `agency-agents`.
  - "Run a MiroFish Swarm simulation on the proposed revenue model."
  - "Verify ROI: Perform a logic-check for the monetization-to-implementation cost."

## SITUATION: Debugging / Error Fixing
- **Detection:** `Fix`, `Error`, `Bug`, `Traceback`, `Not working`.
- **Injection:**
  - "Identify the root cause BEFORE proposing a solution."
  - "Empirical Verification: Create a reproduction script or test case first."
  - "Surgical Change: Minimize the delta between the original and fixed code."
