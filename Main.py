from AcessarFotos import exibir_foto
from CaptarFoto import tirar_foto
import os
from datetime import datetime

# Lista para armazenar o histórico em memória
historico_lista = []

def registrar_historico(acao):
    """Registra ação no histórico"""
    # Pega hora atual
    hora = datetime.now().strftime("%d/%m %H:%M")
    # Adiciona na lista em memória
    historico_lista.append(f"[{hora}] {acao}")
    
    # Caminho do arquivo de histórico
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    # Abre arquivo em modo append (adiciona no final)
    with open(arquivo, "a", encoding="utf-8") as f:
        # Escreve ação com timestamp
        f.write(f"[{hora}] {acao}\n")

def exibir_historico():
    """Mostra as últimas 10 ações"""
    # Se a lista estiver vazia
    if not historico_lista:
        print("Histórico vazio.\n")
        return
    
    # Mostra cabeçalho formatado
    print("\n" + "="*40)
    print("ÚLTIMAS AÇÕES")
    print("="*40)
    
    # Mostra as últimas 10 ações da lista
    for acao in historico_lista[-10:]:
        print(acao)
    
    # Mostra rodapé formatado
    print("="*40 + "\n")

def menu():
    """Menu principal da aplicação"""
    # Registra que a app foi iniciada
    registrar_historico("Aplicação iniciada")
    
    # Loop infinito até escolher sair
    while True:
        # Mostra o menu formatado COM EMOJIS
        print("\n" + "="*40)
        print("📷 BEM-VINDO À CÂMERA JOVI")
        print("="*40)
        print("1️⃣  - Tirar foto")
        print("2️⃣  - Ver última foto")
        print("3️⃣  - Galeria de fotos")
        print("4️⃣  - Ver histórico")
        print("5️⃣  - Sair")
        print("="*40)
        
        # Pede para o usuário escolher
        try:
            opc = int(input("\nEscolha uma opção: "))
        except ValueError:
            # Se digitar algo que não é número
            print("Digite um número válido!")
            continue
        
        # Opção 1: Tirar foto
        if opc == 1:
            print("\nAbrindo câmera...")
            tirar_foto()
        
        # Opção 2: Ver última foto
        elif opc == 2:
            print("\nBuscando última foto...")
            exibir_foto()
        
        # Opção 3: Galeria
        elif opc == 3:
            print("\nAbrindo galeria...")
            exibir_foto(galeria=True)
        
        # Opção 4: Ver histórico
        elif opc == 4:
            exibir_historico()
        
        # Opção 5: Sair
        elif opc == 5:
            print("\nAté logo!\n")
            # Registra que fechou a app
            registrar_historico("Aplicação encerrada")
            break
        
        # Se digitar número fora das opções
        else:
            print("Opção inválida!")

# Executa o programa
if __name__ == "__main__":
    menu()