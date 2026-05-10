from AcessarFotos import exibir_foto
from CaptarFoto import tirar_foto
import os
from datetime import datetime

# Lista para armazenar o histórico em memória durante a sessão
historico_lista = []

def registrar_historico(acao):
    """Registra ação no histórico"""
    # Pega hora atual no formato DD/MM HH:MM
    hora = datetime.now().strftime("%d/%m %H:%M")
    # Adiciona a ação na lista em memória
    historico_lista.append(f"[{hora}] {acao}")
    
    # Define caminho do arquivo de histórico
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    # Abre arquivo em modo append (adiciona no final)
    with open(arquivo, "a", encoding="utf-8") as f:
        # Escreve ação com timestamp no arquivo
        f.write(f"[{hora}] {acao}\n")

def exibir_historico():
    """Mostra todas as ações registradas"""
    # Define caminho do arquivo de histórico
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    
    # Se o arquivo não existe ainda
    if not os.path.exists(arquivo):
        print("Histórico vazio.\n")
        return
    
    # Abre e lê todas as linhas do arquivo
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    # Se não tem nenhuma linha
    if not linhas:
        print("Histórico vazio.\n")
        return
    
    # Mostra cabeçalho formatado
    print("\n" + "="*40)
    print("TODAS AS AÇÕES")
    print("="*40)
    
    # Mostra TODAS as ações do arquivo (não apenas últimas 10)
    for acao in linhas:
        print(acao.strip())
    
    # Mostra rodapé formatado
    print("="*40 + "\n")

def menu():
    """Menu principal da aplicação"""
    # Registra que a app foi iniciada
    registrar_historico("Aplicação iniciada")
    
    # Loop infinito até escolher sair
    while True:
        # Mostra o menu formatado COM EMOJIS APENAS NO TÍTULO
        print("\n" + "="*40)
        print("📷 BEM-VINDO À CÂMERA JOVI")
        print("="*40)
        # Menu com números normais, sem emojis
        print("1 - Tirar foto")
        print("2 - Ver última foto")
        print("3 - Galeria de fotos")
        print("4 - Ver histórico")
        print("5 - Sair")
        print("="*40)
        
        # Pede para o usuário escolher uma opção
        try:
            opc = int(input("\nEscolha uma opção: "))
        except ValueError:
            # Se digitar algo que não é número, avisa e volta
            print("Digite um número válido!")
            continue
        
        # Opção 1: Tirar foto
        if opc == 1:
            print("\nAbrindo câmera...")
            # Chama função de captura
            tirar_foto()
            # Registra a ação no histórico
            registrar_historico("Tirou uma foto")
        
        # Opção 2: Ver última foto
        elif opc == 2:
            print("\nBuscando última foto...")
            # Chama função para exibir última foto
            exibir_foto()
            # Registra a ação no histórico
            registrar_historico("Visualizou última foto")
        
        # Opção 3: Galeria de fotos
        elif opc == 3:
            print("\nAbrindo galeria...")
            # Chama função de galeria
            exibir_foto(galeria=True)
            # Registra a ação no histórico
            registrar_historico("Acessou galeria de fotos")
        
        # Opção 4: Ver histórico
        elif opc == 4:
            # Mostra todas as ações registradas
            exibir_historico()
            # Registra que viu o histórico
            registrar_historico("Visualizou o histórico")
        
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