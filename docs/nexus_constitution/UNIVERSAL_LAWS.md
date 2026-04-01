# NEXUS CONSTITUTION: UNIVERSAL LAWS

These rules apply to EVERY prompt processed by the `nexus_clean_prompt` layer.

## 1. Core Structural Elements
Every "cleaned" prompt MUST contain these four elements:
- **Instruction:** Specific command (e.g., "Synthesize," "Extract," "Optimize").
- **Context:** L0 Strategy + L1 Architecture + Current Hardware Profile.
- **Input Data:** The raw user request, de-noised.
- **Output Indicator:** Explicit format (e.g., "Return a JSON object," "Provide a 3-step technical plan").

## 2. The Directives of Clarity
- **Constraint-First:** Instructions must be placed at the beginning of the prompt.
- **Positive Guidance:** Always tell the model **what to do**, rather than what not to do. If a "don't" is necessary, pair it with a "instead, do [X]."
- **Delimiters:** Use XML-style tags (e.g., `<user_request>`, `<context>`) to separate segments and prevent prompt injection or confusion.
- **Temporal Awareness:** Always inject the current date and time to avoid stale reasoning (e.g., "Latest news" queries).

## 3. De-Noising logic
- **Vague Removal:** Replace "Make it good" or "Fix this" with "Optimize the following code for O(n) complexity and readability."
- **Impreciseness Filter:** Convert "A few sentences" into "2-3 technical sentences." Convert "Fast" into "Minimize latency and token usage."

## 4. Safety & Validation
- **Verification Mandate:** Every complex output must include a self-check or "Reflection" step where the model evaluates its own logic against the L0 Strategy.
