import os
import subprocess

nome_ambiente = "env"

if os.name == 'nt':  # Windows
    if not os.path.isdir(nome_ambiente):
        subprocess.call(["python", "-m", "venv", nome_ambiente])

    subprocess.call([f"{nome_ambiente}\\Scripts\\pip", "install", "--upgrade", "pip"])
    subprocess.call([f"{nome_ambiente}\\Scripts\\pip", "install", "-r", "requirements.txt"])

else:  # macOS e Linux
    if not os.path.isdir(nome_ambiente):
        subprocess.call(["python3", "-m", "venv", nome_ambiente])

    subprocess.call([f"{nome_ambiente}/bin/pip", "install", "--upgrade", "pip"])
    subprocess.call([f"{nome_ambiente}/bin/pip", "install", "-r", "requirements.txt"])


comando_ativacao = ""

if os.name == 'nt':  # Windows
    comando_ativacao = f".\\{nome_ambiente}\\Scripts\\activate"
    ubprocess.run(comando_ativacao, shell=True)
    print(f"Para ativar o ambiente: {comando_ativacao}")

else:  # macOS e Linux
    comando_ativacao = f"source ./{nome_ambiente}/bin/activate"
    subprocess.run(comando_ativacao, shell=True)
    print(f"Para ativar o ambiente: {comando_ativacao}")


