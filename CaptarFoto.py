import cv2
import os
from datetime import datetime

def tirar_foto():
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("❌ Câmera não disponível.\n")
        registrar_historico("❌ Câmera não encontrada")
        return
    
    print("💾 ESPAÇO = tirar foto | ESC = cancelar\n")
    
    while True:
        ret, frame = camera.read()
        
        if not ret:
            print("❌ Erro ao capturar.\n")
            break
        
        cv2.putText(frame, "ESPACO = foto | ESC = sair", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        cv2.imshow("Câmera", frame)
        
        tecla = cv2.waitKey(30) & 0xFF
        
        if tecla == 32:  # ESPAÇO
            nome = f"foto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            caminho = os.path.join(os.path.expanduser("~"), "Pictures", nome)
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            
            cv2.imwrite(caminho, frame)
            print(f"✅ Foto salva: {nome}\n")
            registrar_historico(f"📸 Salvou foto: {nome}")
            
            # Mostra "Foto tirada!" por 1 segundo
            cv2.putText(frame, "Foto tirada!", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            cv2.imshow("Câmera", frame)
            cv2.waitKey(1000)
            break
        
        elif tecla == 27:  # ESC
            print("❌ Cancelado.\n")
            registrar_historico("❌ Cancelou captura")
            break
    
    camera.release()
    cv2.destroyAllWindows()

def registrar_historico(acao):
    """Registra ação no histórico"""
    arquivo = os.path.expanduser("~/.historico_camera.txt")
    hora = datetime.now().strftime("%d/%m %H:%M")
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(f"[{hora}] {acao}\n")