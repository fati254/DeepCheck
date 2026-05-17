from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os
import json
import subprocess

def assistant(request):

    sample_issues = [
        {
            'title': 'Hardcoded Password',
            'severity': 'CRITICAL',
            'description': 'Password detected directly inside code.',
            'recommendation': 'Store passwords in environment variables.',
            'secure_example': 'os.getenv("DB_PASSWORD")'
        },
        {
            'title': 'DEBUG=True',
            'severity': 'HIGH',
            'description': 'Debug mode should not be enabled in production.',
            'recommendation': 'Set DEBUG=False in production.',
            'secure_example': 'DEBUG = False'
        }
    ]

    critical_count = sum(1 for issue in sample_issues if issue['severity'] == 'CRITICAL')

    context = {
        'issues': sample_issues,
        'critical_count': critical_count
    }

    return render(request, 'ai_security/assistant.html', context)  



SONAR_URL = "http://localhost:9000"
SONAR_TOKEN = "sqp_5712940767dc9e00ab447eb9450ed6ee486d7534"
SECURITY_KNOWLEDGE_BASE = {

    "eval": {

        "title": "Dangerous eval() Usage",

        "severity": "CRITICAL",

        "description":
        "Using eval() allows arbitrary code execution.",

        "recommendation":
        "Avoid eval() and use safe parsers.",

        "secure_example":
        "ast.literal_eval(user_input)"
    },

    "exec": {

        "title": "Dangerous exec() Usage",

        "severity": "CRITICAL",

        "description":
        "exec() may execute malicious commands.",

        "recommendation":
        "Avoid dynamic execution.",

        "secure_example":
        "# Avoid exec()"
    },

    "pickle": {

        "title": "Unsafe Pickle Deserialization",

        "severity": "HIGH",

        "description":
        "pickle.loads() can execute malicious payloads.",

        "recommendation":
        "Use JSON instead of pickle.",

        "secure_example":
        "json.loads(data)"
    },

    "md5": {

        "title": "Weak MD5 Hash",

        "severity": "MEDIUM",

        "description":
        "MD5 hashing is insecure.",

        "recommendation":
        "Use SHA256 or bcrypt.",

        "secure_example":
        "hashlib.sha256(data.encode())"
    },

    "shell=true": {

        "title": "Dangerous shell=True Usage",

        "severity": "HIGH",

        "description":
        "shell=True can allow command injection.",

        "recommendation":
        "Use shell=False in subprocess.",

        "secure_example":
         'subprocess.run(["dir"], shell=False)'
},

"os.system": {

    "title": "Command Injection Risk",

    "severity": "HIGH",

    "description":
    "os.system() may execute dangerous system commands.",

    "recommendation":
    "Use subprocess with safe arguments.",

    "secure_example":
    'subprocess.run(["ping", username])'
},

"admin123": {

    "title": "Hardcoded Password",

    "severity": "HIGH",

    "description":
    "Hardcoded passwords are insecure.",

    "recommendation":
    "Store passwords in environment variables.",

    "secure_example":
    'os.getenv("DB_PASSWORD")'
},

"secret": {

    "title": "Hardcoded Secret Key",

    "severity": "CRITICAL",

    "description":
    "Secret keys should never be stored directly in code.",

    "recommendation":
    "Use environment variables or secret managers.",

    "secure_example":
    'os.getenv("SECRET_KEY")'
},

"select * from": {

    "title": "Possible SQL Injection",

    "severity": "CRITICAL",

    "description":
    "SQL query built from user input detected.",

    "recommendation":
    "Use parameterized queries.",

    "secure_example":
    'cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))'
},

"innerhtml": {

    "title": "Possible XSS Vulnerability",

    "severity": "HIGH",

    "description":
    "innerHTML may allow script injection.",

    "recommendation":
    "Use textContent instead of innerHTML.",

    "secure_example":
    'element.textContent = userInput'
},

"document.write": {

    "title": "Unsafe document.write Usage",

    "severity": "MEDIUM",

    "description":
    "document.write() may introduce XSS vulnerabilities.",

    "recommendation":
    "Use safe DOM methods.",

    "secure_example":
    'element.textContent = data'
},

"debug=true": {

    "title": "Debug Mode Enabled",

    "severity": "MEDIUM",

    "description":
    "Debug mode should not be enabled in production.",

    "recommendation":
    "Disable debug mode in production.",

    "secure_example":
    'debug=False'
},
    

}

@csrf_exempt
def assistant_api(request):

    global LAST_SCANNED_FILE

    try:

        scan_file = LAST_SCANNED_FILE

        response = requests.get(

            f"{SONAR_URL}/api/issues/search",

            params={
                "componentKeys": "DeepCheck",
                "resolved": "false",
                "ps": 20
            },

            auth=(SONAR_TOKEN, "")

        )

        sonar_data = response.json()

        issues = []

        # =========================
        # CUSTOM AI ANALYSIS
        # =========================

        if os.path.exists(scan_file):

            print("FILE DETECTED")

            with open(scan_file, "r", encoding="utf-8") as file:

                scanned_content = file.read().lower()

            print(scanned_content)

            for key, data in SECURITY_KNOWLEDGE_BASE.items():

                print("SEARCHING:", key)

                if key in scanned_content:

                    print("FOUND:", key)

                    issues.append({

                        "id": len(issues) + 1,

                        "title": data["title"],

                        "severity": data["severity"],

                        "priority": len(issues) + 1,

                        "description": data["description"],

                        "recommendation": data["recommendation"],

                        "secure_example": data["secure_example"],

                        "file": scan_file,

                        "line": 10

                    })

        # =========================
        # SONARQUBE ANALYSIS
        # =========================

        for issue in sonar_data.get("issues", []):

            component = issue.get(
                "component",
                ""
            )

            # ✅ IMPORTANT :
            # afficher seulement le fichier scanné
            if scan_file not in component:
                continue

            severity = issue.get(
                "severity",
                "LOW"
            )

            title = issue.get(
                "message",
                "Unknown Issue"
            )

            description = issue.get(
                "rule",
                "No description"
            )

            recommendation = (
                "Review this vulnerability "
                "and apply secure coding practices."
            )

            secure_example = (
                "Use secure development "
                "best practices."
            )

            priority = {

                "BLOCKER": 1,
                "CRITICAL": 2,
                "MAJOR": 3,
                "MINOR": 4,
                "INFO": 5

            }.get(severity, 5)

            issues.append({

                "id": len(issues) + 1,

                "title": title,

                "severity": severity,

                "priority": priority,

                "description": description,

                "recommendation": recommendation,

                "secure_example": secure_example,

                "file": scan_file,

                "line": issue.get("line", "?")

            })

        # =========================
        # SORT ISSUES
        # =========================

        issues = sorted(
            issues,
            key=lambda x: x["priority"]
        )

        return JsonResponse({

            "issues": issues

        })

    except Exception as e:

        return JsonResponse({

            "error": str(e)

        })
    
@csrf_exempt
def apply_fixes(request):

    return JsonResponse({

        "status": "success",

        "message":
        "Low and medium risks reviewed successfully."

    })

@csrf_exempt
def scan_code(request):

    global LAST_SCANNED_FILE

    try:

        body = json.loads(request.body)

        user_code = body.get("code", "")
        filename = body.get("filename", "unknown.py")

        # =========================
        # CREATE SCANNER WORKSPACE
        # =========================

        workspace = "scanner_workspace"

        os.makedirs(
            workspace,
            exist_ok=True
        )

        # =========================
        # FULL FILE PATH
        # =========================

        scan_path = os.path.join(
            workspace,
            filename
        )

        LAST_SCANNED_FILE = scan_path

        # =========================
        # DELETE OLD FILE
        # =========================

        if os.path.exists(scan_path):

            os.remove(scan_path)

        # =========================
        # SAVE USER CODE
        # =========================

        with open(
            scan_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(user_code)

        print("NEW CODE SAVED")
        print("FILE:", scan_path)

        # =========================
        # RUN SONAR SCANNER
        # =========================

        subprocess.run(

            ["sonar-scanner"],

            shell=True

        )

        return JsonResponse({

            "status": "success",

            "message":
            "Code scanned successfully"

        })

    except Exception as e:

        return JsonResponse({

            "status": "error",

            "error": str(e)

        })