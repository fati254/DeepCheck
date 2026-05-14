import re


def create_issue(
    line,
    severity,
    message,
    recommendation,
    fix=None,
    fix_type="manual"
):
    return {
        "line": line,
        "severity": severity,
        "message": message,
        "recommendation": recommendation,
        "fix": fix,
        "fix_type": fix_type
    }


def analyze_code(code, language):

    issues = []
    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):

        line_clean = line.strip().lower()

        if not line_clean:
            continue

        # =====================================================
        # 🐍 PYTHON ANALYSIS
        # =====================================================
        if language == "python":

            # SQL Injection
            if (
                "execute(" in line_clean
                and "+" in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "CRITICAL",
                    "Possible SQL Injection",
                    "Use parameterized queries",
                    "parameterized_query",
                    "suggestion"
                ))

            # eval()
            if re.search(r'(?<!literal_)eval\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Dangerous use of eval()",
                    "Replace eval() with ast.literal_eval()",
                    "replace_eval",
                    "auto"
                ))

            # exec()
            if re.search(r'\bexec\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Dangerous use of exec()",
                    "Avoid dynamic code execution",
                    None,
                    "manual"
                ))

            # os.system()
            if re.search(r'os\.system\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "CRITICAL",
                    "Possible command injection",
                    "Use subprocess.run([...], shell=False)",
                    "replace_os_system",
                    "suggestion"
                ))

            # shell=True
            if re.search(r'shell\s*=\s*true', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Unsafe subprocess usage with shell=True",
                    "Use shell=False",
                    "remove_shell_true",
                    "auto"
                ))

            # Hardcoded password
            if re.search(
                r'(password|passwd|pwd)\s*=\s*[\'"].+[\'"]',
                line_clean
            ):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Hardcoded password detected",
                    "Use environment variables",
                    None,
                    "manual"
                ))

            # pickle.load()
            if re.search(r'pickle\.load[s]?\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Unsafe deserialization with pickle",
                    "Use JSON instead of pickle",
                    "replace_pickle",
                    "suggestion"
                ))

            # input()
            if re.search(r'\binput\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "MEDIUM",
                    "User input detected",
                    "Validate and sanitize inputs",
                    None,
                    "manual"
                ))

            # File write
            if (
                "open(" in line_clean
                and (
                    "'w'" in line_clean
                    or '"w"' in line_clean
                )
            ):

                issues.append(create_issue(
                    i,
                    "MEDIUM",
                    "File write operation detected",
                    "Validate file paths",
                    None,
                    "manual"
                ))

            # requests.get without timeout
            if (
                "requests.get(" in line_clean
                and "timeout=" not in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "MEDIUM",
                    "HTTP request without timeout",
                    "Add timeout parameter",
                    "add_timeout",
                    "auto"
                ))

            # Weak hashing
            if re.search(r'\b(md5|sha1)\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Weak hashing algorithm detected",
                    "Use bcrypt or SHA256",
                    "replace_md5",
                    "auto"
                ))

            # Debug mode
            if re.search(r'debug\s*=\s*true', line_clean):

                issues.append(create_issue(
                    i,
                    "MEDIUM",
                    "Debug mode enabled",
                    "Disable debug mode in production",
                    "disable_debug",
                    "auto"
                ))

            # CSRF disabled
            if "@csrf_exempt" in line_clean:

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "CSRF protection disabled",
                    "Enable CSRF protection",
                    None,
                    "manual"
                ))

            # JWT insecure
            if (
                "algorithm='none'" in line_clean
                or 'algorithm="none"' in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "CRITICAL",
                    "Insecure JWT configuration",
                    "Use HS256 or RS256",
                    "secure_jwt",
                    "auto"
                ))

        # =====================================================
        # ⚡ JAVASCRIPT ANALYSIS
        # =====================================================
        elif language == "javascript":

            # eval()
            if re.search(r'(?<!safe_)eval\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Dangerous use of eval()",
                    "Avoid eval()",
                    "replace_eval",
                    "auto"
                ))

            # innerHTML
            if re.search(r'innerhtml', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Possible DOM XSS vulnerability",
                    "Use textContent instead",
                    "replace_innerhtml",
                    "auto"
                ))

            # document.write()
            if re.search(r'document\.write', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Unsafe DOM manipulation",
                    "Avoid document.write()",
                    "replace_documentwrite",
                    "suggestion"
                ))

            # SQL Injection
            if (
                "query =" in line_clean
                and "+" in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "CRITICAL",
                    "Possible SQL Injection",
                    "Use prepared statements",
                    "prepared_statements",
                    "suggestion"
                ))

            # Hardcoded password
            if re.search(
                r'password\s*=\s*[\'"].+[\'"]',
                line_clean
            ):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Hardcoded password detected",
                    "Store secrets securely",
                    None,
                    "manual"
                ))

            # fetch() without timeout
            if (
                "fetch(" in line_clean
                and "abortcontroller" not in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "MEDIUM",
                    "No timeout handling in fetch request",
                    "Use AbortController",
                    "add_fetch_timeout",
                    "suggestion"
                ))

            # localStorage
            if "localstorage.setitem" in line_clean:

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Sensitive data stored in localStorage",
                    "Avoid storing tokens",
                    "secure_storage",
                    "manual"
                ))

            # Weak hashing
            if re.search(r'\b(md5|sha1)\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Weak hashing algorithm",
                    "Use bcrypt or SHA256",
                    "replace_sha1",
                    "auto"
                ))

            # JWT insecure
            if (
                "jwt.sign" in line_clean
                and "none" in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "CRITICAL",
                    "Insecure JWT algorithm",
                    "Use secure JWT signing",
                    "secure_jwt",
                    "auto"
                ))

        # =====================================================
        # 🐘 PHP ANALYSIS
        # =====================================================
        elif language == "php":

            # eval()
            if re.search(r'\beval\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Dangerous use of eval()",
                    "Avoid eval()",
                    None,
                    "manual"
                ))

            # system()
            if re.search(r'\bsystem\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "CRITICAL",
                    "Possible command injection",
                    "Sanitize user input",
                    None,
                    "manual"
                ))

            # SQL Injection
            if (
                "mysqli_query" in line_clean
                and "$" in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "CRITICAL",
                    "Possible SQL Injection",
                    "Use prepared statements",
                    None,
                    "suggestion"
                ))

            # XSS
            if (
                "echo" in line_clean
                and "$_get" in line_clean
            ):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Possible XSS vulnerability",
                    "Use htmlspecialchars()",
                    "escape_html",
                    "suggestion"
                ))

            # unserialize()
            if re.search(r'unserialize\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Unsafe deserialization",
                    "Avoid unserialize()",
                    "safe_deserialize",
                    "suggestion"
                ))

            # Weak hashing
            if re.search(r'\b(md5|sha1)\s*\(', line_clean):

                issues.append(create_issue(
                    i,
                    "HIGH",
                    "Weak hashing algorithm",
                    "Use password_hash()",
                    "replace_md5",
                    "auto"
                ))

    return issues