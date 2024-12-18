# Detecção Facial com OpenCV e Webcam

Este projeto demonstra como usar a biblioteca OpenCV em Python para capturar imagens e vídeo da webcam, realizar detecção facial usando o Haar Cascade e incluir recursos extras como captura de imagens e gravação de vídeos processados.

## Funcionalidades

- **Detecção Facial**: Identifica rostos em tempo real no feed da webcam e destaca-os com retângulos.
- **Captura de Imagens**: Permite capturar imagens pressionando a tecla `c`. As imagens são salvas com nomes exclusivos baseados na data e hora.
- **Gravação de Vídeo**: Grava o feed processado da webcam (com detecção facial) em um arquivo de vídeo no formato `.avi`.

## Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado. Além disso, instale as seguintes bibliotecas:

- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)

Para instalar as dependências, execute:

```bash
pip install opencv-python opencv-python-headless numpy
```

## Como Usar

1. Clone ou baixe este repositório.
2. Certifique-se de que sua webcam esteja conectada e funcionando.
3. Execute o script principal no terminal:
   ```bash
   python webcam_face_detection.py
   ```
4. Durante a execução:
   - Pressione `c` para capturar uma imagem.
   - Pressione `q` para encerrar o programa.

## Estrutura do Projeto

```
.
├── captured_images/          # Pasta onde as imagens capturadas serão armazenadas
├── output_video.avi          # Arquivo de vídeo gerado (após execução do programa)
├── webcam_face_detection.py  # Script principal do projeto
└── README.md                 # Documentação do projeto
```

## Exemplo de Uso

### Detecção Facial em Tempo Real
A detecção facial usa o modelo Haar Cascade para identificar rostos no feed da webcam. Cada rosto detectado é destacado com um retângulo azul.

### Captura de Imagens
Quando você pressiona `c`, uma imagem do feed atual é salva automaticamente na pasta `captured_images/`.

### Gravação de Vídeo
O vídeo processado (incluindo a detecção facial) é salvo automaticamente em `output_video.avi` durante a execução do programa.

## Requisitos do Sistema

- Python 3.8 ou superior
- Webcam funcional
- Sistema operacional compatível (Windows, macOS ou Linux)

## Tecnologias Utilizadas

- **Python**
- **OpenCV**: Para processamento de imagens e vídeo.
- **NumPy**: Para manipulação eficiente de matrizes e arrays.


