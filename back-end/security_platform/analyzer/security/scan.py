def analyze_code(code, language):
    issues = []
    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):
        line_clean = line.strip().lower()

        if not line_clean:
            continue

        # =========================
        # 🐍 PYTHON ANALYSIS
        # =========================
        if language == "python":

            if "execute(" in line_clean and "+" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Possible SQL Injection",
                    "recommendation": "Use parameterized queries (cursor.execute(query, params))",
                    "fix": None
                })

            if "eval(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Dangerous use of eval()",
                    "recommendation": "Use ast.literal_eval() instead",
                    "fix": "replace_eval"
                })

            if "exec(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Dangerous use of exec()",
                    "recommendation": "Avoid exec()",
                    "fix": None
                })

            if "os.system(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Command injection risk",
                    "recommendation": "Use subprocess.run([...])",
                    "fix": None
                })

            if "shell=true" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Unsafe subprocess (shell=True)",
                    "recommendation": "Use shell=False",
                    "fix": "remove_shell_true"
                })

            if "password =" in line_clean or "passwd =" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Hardcoded password",
                    "recommendation": "Use environment variables",
                    "fix": None
                })

            if "pickle.load" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Unsafe deserialization",
                    "recommendation": "Avoid pickle with untrusted data",
                    "fix": None
                })

            if "input(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "User input detected",
                    "recommendation": "Validate input",
                    "fix": None
                })

            if "open(" in line_clean and "'w'" in line_clean:
                issues.append({
                    "line": i,
                    "message": "File write detected",
                    "recommendation": "Check permissions",
                    "fix": None
                })

            if "requests.get(" in line_clean and "timeout" not in line_clean:
                issues.append({
                    "line": i,
                    "message": "No timeout in request",
                    "recommendation": "Add timeout=5",
                    "fix": "add_timeout"
                })


        # =========================
        # ⚡ JAVASCRIPT ANALYSIS
        # =========================
        elif language == "javascript":

            if "eval(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Dangerous use of eval()",
                    "recommendation": "Avoid eval()",
                    "fix": None
                })

            if "exec(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Command execution risk",
                    "recommendation": "Sanitize inputs",
                    "fix": None
                })

            if "innerhtml" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Possible XSS vulnerability",
                    "recommendation": "Use textContent instead",
                    "fix": None
                })

            if "query =" in line_clean and "+" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Possible SQL Injection",
                    "recommendation": "Use prepared statements",
                    "fix": None
                })

            if "password =" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Hardcoded password",
                    "recommendation": "Use environment variables",
                    "fix": None
                })

            if "fetch(" in line_clean and "timeout" not in line_clean:
                issues.append({
                    "line": i,
                    "message": "No timeout in fetch request",
                    "recommendation": "Use AbortController",
                    "fix": None
                })

            if "document.write" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Unsafe DOM manipulation",
                    "recommendation": "Avoid document.write",
                    "fix": None
                })

            if "localstorage.setitem" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Sensitive data in localStorage",
                    "recommendation": "Avoid storing secrets",
                    "fix": None
                })


        # =========================
        # 🐘 PHP ANALYSIS
        # =========================
        elif language == "php":

            if "eval(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Dangerous use of eval()",
                    "recommendation": "Avoid eval()",
                    "fix": None
                })

            if "system(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Command injection risk",
                    "recommendation": "Sanitize input",
                    "fix": None
                })

            if "mysqli_query" in line_clean and "$" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Possible SQL Injection",
                    "recommendation": "Use prepared statements",
                    "fix": None
                })

            if "echo" in line_clean and "$_get" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Possible XSS",
                    "recommendation": "Use htmlspecialchars()",
                    "fix": None
                })

            if "unserialize(" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Unsafe deserialization",
                    "recommendation": "Avoid unserialize()",
                    "fix": None
                })

            if "include(" in line_clean and "$_get" in line_clean:
                issues.append({
                    "line": i,
                    "message": "File inclusion vulnerability",
                    "recommendation": "Whitelist files",
                    "fix": None
                })

            if "password =" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Hardcoded password",
                    "recommendation": "Use env variables",
                    "fix": None
                })

            if "header(" in line_clean and "$_get" in line_clean:
                issues.append({
                    "line": i,
                    "message": "Open redirect",
                    "recommendation": "Validate URLs",
                    "fix": None
                })

    return issues