def analyze_code(code):
    issues = []

    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):
        line_clean = line.strip()

        # ignorer lignes vides
        if not line_clean:
            continue

        # SQL Injection
        if "execute(" in line_clean and "+" in line_clean:
            issues.append({
                "line": i,
                "message": "Possible SQL Injection",
                "recommendation": "Use parameterized queries (cursor.execute(query, params))",
                "fix": None
            })

        # eval()
        if "eval(" in line_clean:
            issues.append({
                "line": i,
                "message": "Dangerous use of eval()",
                "recommendation": "Use ast.literal_eval() instead of eval()",
                "fix": "replace_eval"
            })

        # exec()
        if "exec(" in line_clean:
            issues.append({
                "line": i,
                "message": "Dangerous use of exec()",
                "recommendation": "Avoid exec() or restrict input",
                "fix": None
            })

        # os.system
        if "os.system(" in line_clean:
            issues.append({
                "line": i,
                "message": "Possible command injection",
                "recommendation": "Use subprocess.run() with list arguments",
                "fix": None
            })

        # subprocess shell=True
        if "subprocess" in line_clean and "shell=True" in line_clean:
            issues.append({
                "line": i,
                "message": "Unsafe subprocess usage (shell=True)",
                "recommendation": "Use shell=False to prevent injection",
                "fix": "remove_shell_true"
            })

        # password hardcoded (plus robuste)
        if any(x in line_clean.lower() for x in ["password =", "passwd =", "pwd ="]):
            issues.append({
                "line": i,
                "message": "Hardcoded password detected",
                "recommendation": "Store secrets in environment variables",
                "fix": None
            })

        # pickle
        if "pickle.load" in line_clean:
            issues.append({
                "line": i,
                "message": "Unsafe deserialization with pickle",
                "recommendation": "Avoid loading untrusted data with pickle",
                "fix": None
            })

        # input
        if "input(" in line_clean:
            issues.append({
                "line": i,
                "message": "User input detected",
                "recommendation": "Validate and sanitize inputs",
                "fix": None
            })

        # file write (plus précis)
        if "open(" in line_clean and ("'w'" in line_clean or '"w"' in line_clean):
            issues.append({
                "line": i,
                "message": "File write operation detected",
                "recommendation": "Ensure proper permissions and validation",
                "fix": None
            })

        # requests timeout
        if "requests.get(" in line_clean and "timeout" not in line_clean:
            issues.append({
                "line": i,
                "message": "HTTP request without timeout",
                "recommendation": "Add timeout parameter (e.g., timeout=5)",
                "fix": "add_timeout"
            })

    return issues