import os
import subprocess

def atualizar_requirements(nome_ambiente):
    """Atualiza o arquivo requirements.txt usando o pip do ambiente virtual."""
    
    print("Atualizando o arquivo requirements.txt usando o pip do ambiente virtual.")
    
    pip_path = os.path.join(nome_ambiente, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(nome_ambiente, 'bin', 'pip')
    
    # Usar subprocess.run para atualizar o arquivo requirements.txt
    with open("requirements.txt", "w") as requirements_file:
        subprocess.run([pip_path, "freeze"], stdout=requirements_file, text=True)

def deletar_ambiente_virtual(nome_ambiente):
    """Apaga o ambiente virtual."""
    if os.name == 'nt':  # Windows
        subprocess.call(["rmdir", "/Q", "/S", nome_ambiente], shell=True)
    else:  # macOS e Linux
        subprocess.call(["rm", "-rf", nome_ambiente])

nome_ambiente = "env"

if os.path.exists(nome_ambiente):
    atualizar_requirements(nome_ambiente)

    '''resposta = input(f"Arquivo requirements atualizado! Deseja apagar o ambiente virtual '{nome_ambiente}'? [s] ou [n]: ").lower()

    if resposta == 's':
        deletar_ambiente_virtual(nome_ambiente)
        print(f"Ambiente virtual '{nome_ambiente}' foi apagado.")
    else:
        print(f"Ambiente virtual '{nome_ambiente}' foi mantido.")'''
else:
    print(f"Não foi possível atualizar o arquivo requirements, ambiente virtual '{nome_ambiente}' não encontrado na raiz do projeto.")
