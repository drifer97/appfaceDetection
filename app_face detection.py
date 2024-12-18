import cv2
import os
from datetime import datetime

# Inicialize a Haar Cascade para detecção facial
haarcascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haarcascade_path)

# Inicie a captura da webcam
cap = cv2.VideoCapture(0)  # 0 é o índice padrão para a webcam

if not cap.isOpened():
    print("Erro: Não foi possível acessar a webcam.")
    exit()

# Configuração para gravação de vídeo
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec para gravação
output_path = "output_video.avi"
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20  # Taxa de quadros por segundo
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Crie uma pasta para salvar imagens capturadas, se ainda não existir
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

print("Pressione 'c' para capturar uma imagem, 'q' para sair.")

while True:
    # Leia o quadro da webcam
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível capturar a imagem da webcam.")
        break

    # Converta o quadro para escala de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecte rostos no quadro
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Desenhe retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Grava o quadro processado no vídeo
    video_writer.write(frame)

    # Exiba o quadro com os rostos detectados
    cv2.imshow("Detecção Facial", frame)

    # Capture a entrada do teclado
    key = cv2.waitKey(1) & 0xFF

    # Pressione 'c' para capturar uma imagem
    if key == ord('c'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = f"captured_images/captured_{timestamp}.jpg"
        cv2.imwrite(image_path, frame)
        print(f"Imagem capturada e salva em: {image_path}")

    # Pressione 'q' para sair
    if key == ord('q'):
        break

# Libere os recursos e feche as janelas
cap.release()
video_writer.release()
cv2.destroyAllWindows()
print(f"Vídeo salvo em: {output_path}")
