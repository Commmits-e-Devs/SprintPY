import cv2
import os
import glob

def exibir_foto(galeria=False):
    # Define a pasta onde as fotos são salvas
    pasta = os.path.join(os.path.expanduser("~"), "Pictures")
    # Procura por todas as fotos que começam com "foto_" e acabam com ".jpg"
    # Ordena por data (mais recentes primeiro)
    fotos = sorted(glob.glob(os.path.join(pasta, "foto_*.jpg")), 
                   key=os.path.getmtime, reverse=True)
    
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
                # Vai para próxima (volta ao início se estiver na última)
                indice = (indice + 1) % len(fotos)
            # Se apertar A (foto anterior)
            elif tecla == ord('a') or tecla == ord('A'):
                # Volta para anterior (vai ao final se estiver na primeira)
                indice = (indice - 1) % len(fotos)
        
        # Fecha a janela da galeria
        cv2.destroyAllWindows()
    
    print()