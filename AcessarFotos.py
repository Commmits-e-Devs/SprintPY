import cv2
import os
import glob
from datetime import datetime

def exibir_foto(galeria=False):
    pasta = os.path.join(os.path.expanduser("~"), "Pictures")
    fotos = sorted(glob.glob(os.path.join(pasta, "foto_*.jpg")), 
                   key=os.path.getmtime, reverse=True)
    
    if not fotos:
        print("📭 Nenhuma foto encontrada.\n")
        return
    
    if not galeria:
        # Mostra só a última
        img = cv2.imread(fotos[0])
        if img is not None:
            print(f"✅ Exibindo: {os.path.basename(fotos[0])}")
            print("Pressione qualquer tecla para fechar.\n")
            registrar_historico("👀 Visualizou última foto")
            cv2.imshow("Minha Foto", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        # Galeria com navegação
        indice = 0
        print(f"🎨 Galeria ({len(fotos)} fotos)")
        print("A/D ou SETAS = navegar | ESC = sair\n")
        registrar_historico("🎨 Acessou galeria")
        
        while True:
            img = cv2.imread(fotos[indice])
            if img is None:
                indice = (indice + 1) % len(fotos)
                continue
            
            img_copia = img.copy()
            cv2.putText(img_copia, f"[{indice + 1}/{len(fotos)}]", 
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(img_copia, "A/D = navegar | ESC = sair",
                        (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
            
            cv2.imshow("Galeria", img_copia)
            tecla = cv2.waitKey(30) & 0xFF
            
            if tecla == 27:  # ESC
                print("Galeria fechada.\n")
                break
            elif tecla == ord('d') or tecla == ord('D'):  # D = próxima
                indice = (indice + 1) % len(fotos)
            elif tecla == ord('a') or tecla == ord('A'):  # A = anterior
                indice = (indice - 1) % len(fotos)
        
        cv2.destroyAllWindows()
    
    print()

def registrar_historico(acao):
    """Registra ação no histórico"""
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    hora = datetime.now().strftime("%d/%m %H:%M")
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(f"[{hora}] {acao}\n")