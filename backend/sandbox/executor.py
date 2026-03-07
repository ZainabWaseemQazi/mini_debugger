import subprocess
import tempfile
import os
import json

class DockerExecutor:

    def run_code(self, code: str):

        with tempfile.TemporaryDirectory() as tmpdir:

            file_path = os.path.join(tmpdir, "user_code.py")

            with open(file_path, "w") as f:
                f.write(code)

            # ----------------------
            # 1️⃣ Safe flake8 check
            # ----------------------
            try:
                lint_result = subprocess.run(
                    [
                        "docker", "run", "--rm",
                        "--network", "none",
                        "--memory", "128m",
                        "--cpus", "0.5",
                        "-v", f"{tmpdir}:/app:ro",
                        "python-runner",
                        "flake8",
                        "--format=json",
                        "user_code.py"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                lint_output = lint_result.stdout[:5000]  # limit size

                try:
                    lint_errors = json.loads(lint_output) if lint_output else {}
                except:
                    lint_errors = {"raw": lint_output}

            except Exception as e:
                lint_errors = {"flake8_error": str(e)}

            # ----------------------
            # 2️⃣ Safe execution
            # ----------------------
            try:
                run_result = subprocess.run(
                    [
                        "docker", "run", "--rm",
                        "--network", "none",
                        "--memory", "256m",
                        "--cpus", "1",
                        "-v", f"{tmpdir}:/app:ro",
                        "python-runner",
                        "python","/app/user_code.py"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=15
                )

                return {
                    
                    "lint_errors": lint_errors,
                    "stdout": run_result.stdout[:5000],
                    "stderr": run_result.stderr[:5000],
                    "success": run_result.returncode == 0
                }

            except subprocess.TimeoutExpired:
                return {
                    "lint_errors": lint_errors,
                    "stdout": "",
                    "stderr": "Execution timed out",
                    "success": False
                }