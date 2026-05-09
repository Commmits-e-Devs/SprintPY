import cv2
import os
import glob

def exibir_foto(caminho=None):
    # Se nenhum caminho for passado, busca a foto mais recente na pasta Pictures
    if caminho is None:
        pasta = os.path.join(os.path.expanduser("~"), "Pictures")
        fotos = glob.glob(os.path.join(pasta, "foto_*.jpg"))

        if not fotos:
            print("Nenhuma foto encontrada na pasta Pictures.")
            return

        # Pega a foto mais recente
        caminho = max(fotos, key=os.path.getmtime)

    print(f"📂 Exibindo: {caminho}")

    img = cv2.imread(caminho)

    if img is None:
        print("Não foi possível carregar a imagem.")
        return

    cv2.imshow("Minha Foto", img)
    print("➡️  Pressione qualquer tecla para fechar.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
