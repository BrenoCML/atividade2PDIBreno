import cv2
import numpy as np
import matplotlib.pyplot as plt


# Função para aplicar os filtros de suavização e plotar as imagens resultantes
def apply_smoothing_filters(image):
    # Filtro de Suavização Média
    average_blur = cv2.blur(image, (9, 9))

    # Filtro de Suavização Mediana
    median_blur = cv2.medianBlur(image, 11)

    # Filtro de Suavização Gaussiano
    gaussian_blur = cv2.GaussianBlur(image, (9, 9), 0)

    # Plota as imagens resultantes
    plt.figure(figsize=(10, 7))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(average_blur, cv2.COLOR_BGR2RGB))
    plt.title('Filtro de Suavização Média')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(median_blur, cv2.COLOR_BGR2RGB))
    plt.title('Filtro de Suavização Mediana')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB))
    plt.title('Filtro de Suavização Gaussiano')
    plt.axis('off')

    # Ajuste das margens e espaçamento
    plt.subplots_adjust(left=0.17, right=0.752, top=0.9, bottom=0.1, wspace=0)

    plt.show()


# Carregaas imagens
image1 = cv2.imread('fiordos-noruegos1.jpg')
image2 = cv2.imread('scotland.jpg')

# Aplica os filtros de suavização e compara visualmente
apply_smoothing_filters(image1)
apply_smoothing_filters(image2)
