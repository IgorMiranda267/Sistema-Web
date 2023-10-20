import os
import subprocess

# Nome do ambiente virtual
nome_ambiente = "env"

# Verifica se o ambiente virtual já existe
if not os.path.isdir(nome_ambiente):
    # Cria o ambiente virtual
    subprocess.call(["python", "-m", "venv", nome_ambiente])

# Atualiza o pip e instala as dependências
if os.name == 'nt':  # Windows
    subprocess.call([f"{nome_ambiente}\\Scripts\\pip", "install", "--upgrade", "pip"])
    subprocess.call([f"{nome_ambiente}\\Scripts\\pip", "install", "-r", "requirements.txt"])
else:  # macOS e Linux
    subprocess.call([f"{nome_ambiente}/bin/pip", "install", "--upgrade", "pip"])
    subprocess.call([f"{nome_ambiente}/bin/pip", "install", "-r", "requirements.txt"])


# Comando para ativar o ambiente virtual
comando_ativacao = ""

if os.name == 'nt':  # Windows
    comando_ativacao = f".\\{nome_ambiente}\\Scripts\\activate"
    print(f"Para ativar o ambiente: {comando_ativacao}")
else:  # macOS e Linux
    comando_ativacao = f"source ./{nome_ambiente}/bin/activate"
    print(f"Para ativar o ambiente: {comando_ativacao}")

# Ativa o ambiente virtual
#subprocess.run(comando_ativacao, shell=True)


