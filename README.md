# atividade2PDIBreno

#  **Atividade de Filtros da disiciplina de Processamento Digital de Imagens**

## **O que foi observado na saída do arquivo uMFilter.py:**

O código implementou um filtro de nitidez em uma imagem utilizando máscaras de convolução. Ele realizou as seguintes etapas: leitura da imagem, conversão para o formato RGB, suavização da imagem com filtro Gaussiano, cálculo da máscara de nitidez, adição da máscara à imagem original e exibição das imagens original, suavizada e nítida. O filtro foi testado com diferentes tamanhos de kernel para observar o efeito na nitidez da imagem. Conforme o tamanho do kernel aumenta, a suavização da imagem é mais pronunciada, resultando em uma redução na nitidez perceptível na imagem final. A escolha do tamanho do kernel influencia o equilíbrio entre suavização e nitidez desejado na imagem processada.

-----------------------------------------------------------------------------

## **O que dá para notar no output do arquivo smoothingFilters.py:**


O Filtro de Suavização Média calculou a média dos valores dos pixels em uma vizinhança definida pelo tamanho do kernel. Cada pixel na imagem suavizada é substituído pela média dos valores dos pixels na vizinhança. Ele é eficaz para reduzir ruídos, mas suavizou detalhes na imagem, diminuiu a qualidade deles.

O Filtro de Suavização Mediana substituiu cada pixel da imagem pelo valor da mediana dos pixels em uma vizinhança definida pelo tamanho do kernel.
Ele preservou melhor os detalhes das bordas da imagem, fica bem claro que as linhas de todas as bordas de cada elemento ficaram destacadas.

O Filtro de Suavização Gaussiano aplicou uma convolução com uma máscara gaussiana para calcular o valor do pixel central.
A intensidade da suavização é controlada pelo tamanho do kernel e pelo desvio padrão da distribuição gaussiana.
É eficaz para suavizar imagens sem borrar muito os detalhes, sendo especialmente útil para preservar bordas e transições suaves.

-----------------------------------------------------------------------------

## **O que dá para notar no output do arquivo eELF.py:**

A diferença entre a imagem original e a imagem de resultado da saída está no realce das bordas. Na imagem original, as bordas podem não ser muito distintas ou visíveis, especialmente em áreas de transição suave entre diferentes regiões da imagem. No entanto, após a aplicação do Filtro Laplaciano, as bordas são realçadas, tornando-se mais evidentes e distintas. Isso ocorre porque o Filtro Laplaciano destaca as mudanças abruptas de intensidade na imagem, ressaltando as transições entre áreas de diferentes tons de cinza. Assim, a saída do Filtro Laplaciano mostra as bordas com maior nitidez, o que pode ser útil em várias aplicações de processamento de imagem, como detecção de bordas, segmentação e análise de textura.