import math  # Importa o módulo math para usar funções matemáticas
from turtle import *  # Importa todas as funções do módulo turtle para desenhar

# Define a função que calcula a coordenada y do coração
def hearta(k):
    return 15 * math.sin(k) ** 3

# Define a função que calcula a coordenada x do coração
def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2 * k) - 2 * \
           math.cos(3 * k) - \
           math.cos(4 * k)

# Configura a velocidade do desenho e a cor de fundo
speed(9000)  # Define a velocidade máxima de desenho
bgcolor("black")  # Define a cor de fundo como preta

# Loop principal para desenhar o coração
for i in range(6000):
    # Calcula as coordenadas e move a tartaruga para o ponto
    goto(hearta(i) * 20, heartb(i) * 20)
    # Desenha pequenos segmentos para criar um efeito visual
    for j in range(5):
        color("#f73487")  # Define a cor dos segmentos
        goto(0, 0)  # Volta para o centro

# Mantém a janela aberta até ser fechada manualmente
done()