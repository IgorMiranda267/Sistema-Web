import os
import subprocess

def atualizar_requirements(nome_ambiente):
    """Atualiza o arquivo requirements.txt usando o pip do ambiente virtual."""
    
    print("Atualizando o arquivo requirements.txt usando o pip do ambiente virtual.")
    
    pip_path = os.path.join(nome_ambiente, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(nome_ambiente, 'bin', 'pip')
    subprocess.call([pip_path, "freeze", ">", "requirements.txt"], shell=True)

def deletar_ambiente_virtual(nome_ambiente):
    """Apaga o ambiente virtual."""
    if os.name == 'nt':  # Windows
        subprocess.call(["rmdir", "/Q", "/S", nome_ambiente], shell=True)
    else:  # macOS e Linux
        subprocess.call(["rm", "-rf", nome_ambiente])

# Diretório do ambiente virtual (na raiz do projeto)
nome_ambiente = "env"

# Verifica se o ambiente virtual existe
if os.path.exists(nome_ambiente):
    # Atualizar o arquivo requirements.txt
    atualizar_requirements(nome_ambiente)

    # Pergunta ao usuário se deseja apagar o ambiente virtual
    '''resposta = input(f"Arquivo requirements atualizado! Deseja apagar o ambiente virtual '{nome_ambiente}'? [s] ou [n]: ").lower()

    if resposta == 's':
        deletar_ambiente_virtual(nome_ambiente)
        print(f"Ambiente virtual '{nome_ambiente}' foi apagado.")
    else:
        print(f"Ambiente virtual '{nome_ambiente}' foi mantido.")'''
else:
    print(f"Não foi possivel atualizar o arquivo requirements, ambiente virtual '{nome_ambiente}' não encontrado na raiz do projeto.")
