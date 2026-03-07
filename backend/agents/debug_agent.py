# agents/debug_agent.py

class DebugAgent:

    def __init__(self, llm):
        self.llm = llm

    def generate_fixes(self, code, lint_errors, runtime_error, n=3):

        prompt = f"""
You are a senior Python engineer.

Original Code:
{code}

Lint Errors:
{lint_errors}

Runtime Error:
{runtime_error}

Generate {n} different corrected versions of this code.
Return them separated by:
### FIX ###
Only return Python code.
"""

        response = self.llm(prompt)

        fixes = response.split("### FIX ###")
        fixes = [fix.strip() for fix in fixes if fix.strip()]
        fixes = [fix.replace("```python", "").replace("```", "").strip() for fix in fixes]

        return fixes[:n]