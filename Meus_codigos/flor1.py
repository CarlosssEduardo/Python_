# Importa a biblioteca turtle para desenho gráfico
import turtle

# Importa o módulo colorsys para trabalhar com cores em HSV (matiz, saturação, valor)
import colorsys as cs

# Define o tamanho da janela de desenho (800x800 pixels)
turtle.setup(800, 800)

# Define a velocidade de desenho como a mais rápida (0)
turtle.speed(0)

# Atualiza a tela somente a cada 10 ciclos de desenho para melhorar a performance
turtle.tracer(10)

# Define a espessura da linha de desenho como 2 pixels
turtle.width(2)

# Define a cor de fundo como preto
turtle.bgcolor("black")

# Loop principal para desenhar o padrão colorido
for j in range(25):
    # Loop interno para desenhar cada camada circular
    for i in range(15):
        # Define a cor da tartaruga usando o modelo HSV e converte para RGB
        turtle.color(cs.hsv_to_rgb(i / 15, j / 25, 1))

        # Gira a tartaruga 90 graus para a direita
        turtle.right(90)

        # Desenha um quarto de círculo com raio 200-j*4 e ângulo 90 graus
        turtle.circle(200 - j * 4, 90)

        # Gira a tartaruga 90 graus para a esquerda
        turtle.left(90)

        # Desenha outro quarto de círculo para completar o semicírculo
        turtle.circle(200 - j * 4, 90)

        # Gira a tartaruga 180 graus para desenhar a outra metade do círculo
        turtle.right(180)

        # Desenha um círculo completo com raio 50 e ângulo 240 graus (2 * 120)
        turtle.circle(50, 24)

# Oculta a tartaruga após a finalização do desenho
turtle.hideturtle()

# Mantém a janela aberta até ser fechada manualmente
turtle.done()