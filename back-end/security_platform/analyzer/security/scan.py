#hadchi hta howa
def analyze_code(code):
    issues = [] #  Crée une liste vide pour stocker les problèmes détectés

    line = code.split("\n") ###pour detecter la ligne et separer ligne par ligne 
    
    for i, line in enumerate(line, start=1):
    
     if "execute(" in line and "+" in line: #  Vérification de SQL Injection
        issues.append(f"Possible SQL Injection (Line {i})") # Si la condition est vraie, on ajoute un avertissement à la liste

     if "eval(" in line:  #  Vérification de eval()
        issues.append(f"Dangerous use of eval() (Line {i})")

    # exec()
     if "exec(" in line:
        issues.append(f"Dangerous use of exec() (Line {i})")

    # import os + system (command injection possible)
     if "os.system(" in line:
        issues.append(f"Possible command injection via os.system() (Line {i})")

    # subprocess avec shell=True
     if "subprocess" in line and "shell=True" in line:
        issues.append(f"Unsafe subprocess call with shell=True (Line {i})")

    # mot de passe en dur
     if "password =" in line or "passwd =" in line:
        issues.append(f"Hardcoded password detected (Line {i})")

    # utilisation de pickle (risque de line execution)
     if "pickle.load" in line:
        issues.append(f"Unsafe deserialization with pickle (Line {i})")

    # utilisation de input() (selon contexte)
     if "input(" in line:
        issues.append(f"User input detected (validate inputs!) (Line {i})")

    # ouverture de fichier en écriture sans contrôle
     if "open(" in line and "w" in line:
        issues.append(f"File write operation detected (check permissions) (Line {i})")

    # utilisation de requests sans timeout
     if "requests.get(" in line and "timeout" not in line:
        issues.append(f"HTTP request without timeout (Line {i})")

    return issues # Retourne la liste des problèmes détectés