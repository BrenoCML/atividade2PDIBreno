import cv2
from matplotlib import pyplot as plt


def sharpness_mask_filter(image_path, kernel_size, alpha=1.5, beta=-0.5):
    # Lê a imagem do caminho especificado
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print(f"Ocorreu um erro ao ler a imagem {image_path}")
        return

    # Converte a imagem de RGB (formato padrão do OpenCV) para RGB (formato padrão do Matplotlib)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Aplica o filtro Gaussiano para suavização da imagem
    blurred = cv2.GaussianBlur(image_rgb, (kernel_size, kernel_size), 0)

    # Calcula a máscara de nitidez subtraindo a imagem suavizada da imagem original
    mask = cv2.subtract(image_rgb, blurred)

    # Adiciona a máscara de nitidez à imagem original para criar a imagem nítida
    sharpened = cv2.addWeighted(image_rgb, alpha, mask, beta, 0)
    sharpened = cv2.addWeighted(image_rgb, alpha, mask, beta, 0)

    # Armazena as imagens para exibição
    images = [image_rgb, blurred, sharpened]
    titles = ['Imagem Original', 'Imagem Suavizada', 'Imagem Nítida']

    # Ajusta o tamanho da figura para melhor visualização
    plt.figure(figsize=(15, 5))
    for i in range(3):
        # Criar subplots para cada imagem
        ax = plt.subplot(1, 3, i + 1)
        ax.imshow(images[i])
        ax.set_title(titles[i])
        # Remover os eixos (ticks) das imagens para uma visualização mais limpa
        ax.set_xticks([]), ax.set_yticks([])
    # Ajusta margens e espaçamento entre subplots
    plt.subplots_adjust(left=0.00, right=1, top=0.9, bottom=0.1, wspace=0)  # Ajuste das margens e espaçamento
    # Exibe as imagens
    plt.show()

# Caminho para a imagem de entrada
image_path = 'livorno.jpg'

# Experimenta diferentes tamanhos de kernel e parâmetros de nitidez
for kernel_size in [3, 5, 9, 15, 21]:
    print(f"Aplicando filtro com kernel size: {kernel_size}")
    sharpness_mask_filter(image_path, kernel_size)
