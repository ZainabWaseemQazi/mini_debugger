import concurrent.futures
from   agents.debug_agent import DebugAgent
from   sandbox.executor import DockerExecutor


class CodeOrchestrator:

    def __init__(self, executor, debug_agent, max_candidates=3):
        self.executor = executor
        self.debug_agent = debug_agent
        self.max_candidates = max_candidates

    def execute_candidate(self, code):
        return self.executor.run_code(code)

    def run(self, code):

        initial_result = self.executor.run_code(code)
        print("Initial execution result:", initial_result)

        if initial_result["success"]:
            return {
                "success": True,
                "status": "success",
                "final_code": code,
                "result": initial_result,
                "early_stop": False
            }

        fixes = self.debug_agent.generate_fixes(
            code,
            initial_result["lint_errors"],
            initial_result["stderr"],
            n=self.max_candidates
        )

        if not fixes:
            return {
                "success": False,
                "status": "no_fixes_generated",
                "final_code": code,
                "result": initial_result,
                "early_stop": False
            }

        results = []

        with concurrent.futures.ThreadPoolExecutor() as pool:

            futures = {
                pool.submit(self.execute_candidate, fix): fix
                for fix in fixes
            }

            for future in concurrent.futures.as_completed(futures):
                fix_code = futures[future]

                print(f"Evaluating fix:\n{fix_code}\n")
                result = future.result()
                print(f"Result for this fix: {result}\n")

                # 🚀 EARLY SUCCESS CHECK
                if result["success"]:
                    # Cancel remaining futures
                    for f in futures:
                        if not f.done():
                            f.cancel()

                    return {
                        "success": True,
                        "status": "success",
                        "final_code": fix_code,
                        "result": result,
                        "early_stop": True
                    }

                results.append((fix_code, result))

        # If no success found
        return self.select_best(results)

    def select_best(self, results):

        # Prefer successful executions
        successful = [r for r in results if r[1]["success"]]

        if successful:
            successful.sort(
                key=lambda x: len(x[1]["lint_errors"])
            )
            best_code, best_result = successful[0]

            return {
                "success": True,
                "status": "best_fix",
                "final_code": best_code,
                "result": best_result,
                "early_stop": False
                
            }

        # If none succeeded → choose smallest stderr
        results.sort(key=lambda x: len(x[1]["stderr"]))

        best_code, best_result = results[0]

        return {
            "success": False,
            "status": "partial_fix",
            "final_code": best_code,
            "result": best_result,
            "early_stop": False
        }