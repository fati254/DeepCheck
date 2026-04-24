#hadchi hta howa
def analyze_code(code):
    issues = [] #  Crée une liste vide pour stocker les problèmes détectés

    if "execute(" in code and "+" in code: #  Vérification de SQL Injection
        issues.append("Possible SQL Injection") # Si la condition est vraie, on ajoute un avertissement à la liste

    if "eval(" in code:  #  Vérification de eval()
        issues.append("Dangerous use of eval()")

    # exec()
    if "exec(" in code:
        issues.append("Dangerous use of exec()")

    # import os + system (command injection possible)
    if "os.system(" in code:
        issues.append("Possible command injection via os.system()")

    # subprocess avec shell=True
    if "subprocess" in code and "shell=True" in code:
        issues.append("Unsafe subprocess call with shell=True")

    # mot de passe en dur
    if "password =" in code or "passwd =" in code:
        issues.append("Hardcoded password detected")

    # utilisation de pickle (risque de code execution)
    if "pickle.load" in code:
        issues.append("Unsafe deserialization with pickle")

    # utilisation de input() (selon contexte)
    if "input(" in code:
        issues.append("User input detected (validate inputs!)")

    # ouverture de fichier en écriture sans contrôle
    if "open(" in code and "w" in code:
        issues.append("File write operation detected (check permissions)")

    # utilisation de requests sans timeout
    if "requests.get(" in code and "timeout" not in code:
        issues.append("HTTP request without timeout")

    return issues # Retourne la liste des problèmes détectés