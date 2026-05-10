import cv2
import os
import glob
from datetime import datetime

def exibir_foto(galeria=False):
    # Define a pasta onde as fotos são salvas
    pasta = os.path.join(os.path.expanduser("~"), "Pictures")
    # Procura por todas as fotos que começam com "foto_" e acabam com ".jpg"
    fotos = sorted(glob.glob(os.path.join(pasta, "foto_*.jpg")), 
                   key=os.path.getmtime, reverse=True)  # Ordena por data (mais recentes primeiro)
    
    # Se não encontrou nenhuma foto
    if not fotos:
        print("Nenhuma foto encontrada.\n")
        return
    
    # Se galeria=False, mostra apenas a última foto
    if not galeria:
        # Lê a primeira foto (mais recente)
        img = cv2.imread(fotos[0])
        if img is not None:
            print(f"Exibindo: {os.path.basename(fotos[0])}")
            print("Pressione qualquer tecla para fechar.\n")
            # Registra no histórico
            registrar_historico("Visualizou última foto")
            # Mostra a foto
            cv2.imshow("Minha Foto", img)
            # Espera o usuário apertar qualquer tecla
            cv2.waitKey(0)
            # Fecha a janela da foto
            cv2.destroyAllWindows()
    else:
        # Se galeria=True, abre modo galeria com navegação
        indice = 0  # Começa na primeira foto
        print(f"Galeria ({len(fotos)} fotos)")
        print("A/D = navegar | ESC = sair\n")
        # Registra que entrou na galeria
        registrar_historico("Acessou galeria")
        
        # Loop da galeria
        while True:
            # Lê a foto no índice atual
            img = cv2.imread(fotos[indice])
            if img is None:
                indice = (indice + 1) % len(fotos)
                continue
            
            # Cria uma cópia para não alterar a original
            img_copia = img.copy()
            # Adiciona o número da foto atual [1/10]
            cv2.putText(img_copia, f"[{indice + 1}/{len(fotos)}]", 
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            # Adiciona instruções
            cv2.putText(img_copia, "A/D = navegar | ESC = sair",
                        (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
            
            # Mostra a foto
            cv2.imshow("Galeria", img_copia)
            # Espera 30ms por uma tecla
            tecla = cv2.waitKey(30) & 0xFF
            
            # Se apertar ESC (27)
            if tecla == 27:
                print("Galeria fechada.\n")
                break
            # Se apertar D (próxima foto)
            elif tecla == ord('d') or tecla == ord('D'):
                indice = (indice + 1) % len(fotos)  # Vai para próxima (volta no final)
            # Se apertar A (foto anterior)
            elif tecla == ord('a') or tecla == ord('A'):
                indice = (indice - 1) % len(fotos)  # Volta para anterior (vai ao final)
        
        # Fecha a janela da galeria
        cv2.destroyAllWindows()
    
    print()

def registrar_historico(acao):
    """Registra ação no histórico"""
    # Define o caminho do arquivo de histórico
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    # Pega a hora atual
    hora = datetime.now().strftime("%d/%m %H:%M")
    # Abre o arquivo em modo append
    with open(arquivo, "a", encoding="utf-8") as f:
        # Escreve a ação com timestamp
        f.write(f"[{hora}] {acao}\n")