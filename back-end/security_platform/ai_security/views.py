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


def assistant_api(request):

    issues = [

    {
        "title": "SQL Injection Risk",
        "severity": "CRITICAL",
        "priority": 1,
        "description": "User input inserted directly into SQL query.",
        "recommendation": "Use parameterized queries.",
        "secure_example": "cursor.execute(query, params)"
    },

    {
        "title": "Hardcoded Password",
        "severity": "HIGH",
        "priority": 2,
        "description": "Password detected directly inside code.",
        "recommendation": "Store passwords in environment variables.",
        "secure_example": "os.getenv('DB_PASSWORD')"
    },

    {
        "title": "DEBUG=True",
        "severity": "MEDIUM",
        "priority": 3,
        "description": "Debug mode enabled in production.",
        "recommendation": "Set DEBUG=False.",
        "secure_example": "DEBUG = False"
    },

    {
        "title": "Weak Input Validation",
        "severity": "LOW",
        "priority": 4,
        "description": "Input validation can be improved.",
        "recommendation": "Validate all user inputs.",
        "secure_example": "form.is_valid()"
    }

]
    issues = sorted(
        issues,
        key=lambda x: x['priority']
)

    return JsonResponse({
        "issues": issues
    })