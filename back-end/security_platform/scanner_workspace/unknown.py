import os
import subprocess
import hashlib

username = input("Enter username: ")

data = ast.literal_eval(input("Enter data: "))

os.system("ping " + username)

password = "admin123"

hash_value = hashlib.sha256(password.encode()).hexdigest()

subprocess.run("dir", shell=False)