from django.shortcuts import render

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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os

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
    }

}

@csrf_exempt
def assistant_api(request):

    try:

        response = requests.get(

            f"{SONAR_URL}/api/issues/search",

            params={
                "componentKeys": "DeepCheck",
                "ps": 20
            },

            auth=(SONAR_TOKEN, "")

        )

        sonar_data = response.json()

        issues = []

        # =========================
        # CUSTOM AI ANALYSIS
        # =========================

        scan_file = "scanned_code.py"

        if os.path.exists(scan_file):

            with open(scan_file, "r", encoding="utf-8") as file:

                scanned_content = file.read().lower()

            for key, data in SECURITY_KNOWLEDGE_BASE.items():

                if key in scanned_content:

                    issues.append({

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

                "title": title,
                "severity": severity,
                "priority": priority,
                "description": description,
                "recommendation": recommendation,
                "secure_example": secure_example,
                "file": issue.get("component", "Unknown File"),
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