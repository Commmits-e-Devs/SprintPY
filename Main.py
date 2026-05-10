from AcessarFotos import exibir_foto
from CaptarFoto import tirar_foto
import os
from datetime import datetime

def registrar_historico(acao):
    """Registra ação no histórico"""
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    hora = datetime.now().strftime("%d/%m %H:%M")
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(f"[{hora}] {acao}\n")

def exibir_historico():
    """Mostra as últimas 10 ações"""
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    
    if not os.path.exists(arquivo):
        print("📭 Histórico vazio.\n")
        return
    
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    print("\n" + "="*40)
    print("📋 ÚLTIMAS AÇÕES")
    print("="*40)
    
    for linha in linhas[-10:]:
        print(linha.strip())
    
    print("="*40 + "\n")

def menu():
    registrar_historico("🟢 Aplicação iniciada")
    
    while True:
        print("\n" + "="*40)
        print("📷 BEM-VINDO À CÂMERA JOVI")
        print("="*40)
        print("1 - Tirar foto")
        print("2 - Ver última foto")
        print("3 - Galeria de fotos")
        print("4 - Ver histórico")
        print("5 - Sair")
        print("="*40)
        
        try:
            opc = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("❌ Digite um número válido!")
            continue
        
        if opc == 1:
            print("\n📸 Abrindo câmera...")
            tirar_foto()
        elif opc == 2:
            print("\n👀 Buscando última foto...")
            exibir_foto()
        elif opc == 3:
            print("\n🎨 Abrindo galeria...")
            exibir_foto(galeria=True)
        elif opc == 4:
            exibir_historico()
        elif opc == 5:
            print("\n👋 Até logo!\n")
            registrar_historico("🔴 Aplicação encerrada")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    menu()