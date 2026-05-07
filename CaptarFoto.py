import cv2
import time
import os
from datetime import datetime

def tirar_foto():
    # Abre a câmera (índice 0 = câmera padrão)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Não foi possível acessar a câmera.")
        return

    print("Pressione ESPAÇO para tirar a foto ou ESC para sair.\n")

    while True:
        ret, frame = camera.read()

        if not ret:
            print(" Falha ao capturar imagem.")
            break

        # Adiciona texto na tela
        cv2.putText(frame, "Pressione ESPACO para foto | ESC para sair",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Camera - Tire sua foto", frame)

        tecla = cv2.waitKey(1) & 0xFF

        # ESPAÇO = tirar foto
        if tecla == 32:
            nome_arquivo = f"foto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            caminho = os.path.join(os.path.expanduser("~"), "Pictures", nome_arquivo)

            # Garante que a pasta existe
            os.makedirs(os.path.dirname(caminho), exist_ok=True)

            cv2.imwrite(caminho, frame)
            print(f"Foto salva em: {caminho}")

            # Mostra a foto tirada por 2 segundos
            cv2.putText(frame, "Foto tirada!", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            cv2.imshow("Câmera - Tire sua foto", frame)
            cv2.waitKey(2000)
            break

        # ESC = sair sem tirar foto
        elif tecla == 27:
            print("Saindo sem tirar foto.")
            break

    camera.release()
    cv2.destroyAllWindows()
