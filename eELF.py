import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem
image = cv2.imread('ireland.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
else:
    # Aplica o Filtro Laplaciano
    laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)

    # Converte de volta para uint8
    laplacian = np.uint8(np.absolute(laplacian))

    # Lista de imagens e títulos
    images = [image, laplacian]
    titles = ['Original', 'Bordas Realçadas']

    # Define o tamanho da figura
    plt.figure(figsize=(15, 5))

    # Loop sobre as imagens e títulos
    for i in range(2):
        # Cria subplots para cada imagem
        plt.subplot(1, 2, i + 1)
        plt.imshow(images[i], cmap='gray')  # Especifica cmap='gray' para imagens em escala de cinza
        plt.title(titles[i])
        # Remove os eixos (ticks) das imagens para uma visualização mais limpa
        plt.xticks([]), plt.yticks([])

    # Ajusta margens e espaçamento entre subplots
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1, wspace=0.01)

    # Exibir as imagens
    plt.show()
