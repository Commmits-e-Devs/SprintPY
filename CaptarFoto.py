import cv2
import os
from datetime import datetime

def tirar_foto():
    # Abre a câmera padrão do PC (índice 0)
    camera = cv2.VideoCapture(0)
    
    # Verifica se a câmera foi aberta com sucesso
    if not camera.isOpened():
        print("Câmera não disponível.\n")
        registrar_historico("Câmera não encontrada")
        return
    
    # Instrções para o usuário
    print("ESPAÇO = tirar foto | ESC = cancelar\n")
    
    # Loop contínuo até tirar foto ou cancelar
    while True:
        # Captura um frame (imagem) da câmera
        ret, frame = camera.read()
        
        # Se não conseguir capturar, sai do loop
        if not ret:
            print("Erro ao capturar.\n")
            break
        
        # Adiciona texto na imagem da câmera
        cv2.putText(frame, "ESPACO = foto | ESC = sair", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Mostra a imagem da câmera em uma janela
        cv2.imshow("Câmera", frame)
        
        # Espera 30ms por uma tecla do usuário
        tecla = cv2.waitKey(30) & 0xFF
        
        # Se apertar ESPAÇO (código 32)
        if tecla == 32:
            # Cria o nome do arquivo com data/hora
            nome = f"foto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            # Define o caminho onde salvar (pasta Pictures do usuário)
            caminho = os.path.join(os.path.expanduser("~"), "Pictures", nome)
            # Garante que a pasta Pictures existe
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            
            # Salva a foto no arquivo
            cv2.imwrite(caminho, frame)
            print(f"Foto salva: {nome}\n")
            # Registra a ação no histórico
            registrar_historico(f"Salvou foto: {nome}")
            
            # Mostra mensagem de sucesso por 1 segundo
            cv2.putText(frame, "Foto tirada!", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            cv2.imshow("Câmera", frame)
            cv2.waitKey(1000)
            break
        
        # Se apertar ESC (código 27)
        elif tecla == 27:
            print("Cancelado.\n")
            registrar_historico("Cancelou captura")
            break
    
    # Fecha a câmera
    camera.release()
    # Fecha todas as janelas abertas
    cv2.destroyAllWindows()

def registrar_historico(acao):
    """Registra ação no histórico"""
    # Define o caminho do arquivo de histórico
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    # Pega a hora atual no formato DD/MM HH:MM
    hora = datetime.now().strftime("%d/%m %H:%M")
    # Abre o arquivo em modo append (adiciona no final)
    with open(arquivo, "a", encoding="utf-8") as f:
        # Escreve a ação com timestamp no arquivo
        f.write(f"[{hora}] {acao}\n")