import subprocess

# Instalar dependencias desde requirements.txt
# subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

# Instalar numpy usando pipwin
subprocess.check_call(["pipwin", "install", "numpy==1.19.5"])
