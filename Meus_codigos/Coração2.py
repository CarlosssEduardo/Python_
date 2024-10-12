from turtle import *  # Importa todas as funções do módulo turtle para desenhar

# Define a cor da caneta como vermelha
color("red")

# Inicia o preenchimento da forma
begin_fill()

# Define a espessura da linha
pensize(3)

# Gira a tartaruga 50 graus para a esquerda
left(50)

# Move a tartaruga 133 pixels para frente
forward(133)

# Desenha um arco de círculo com raio 50 e ângulo de 200 graus
circle(50, 200)

# Gira a tartaruga 140 graus para a direita
right(140)

# Desenha outro arco de círculo
circle(50, 200)

# Move a tartaruga 133 pixels para frente, fechando a forma
forward(133)

# Finaliza o preenchimento da forma
end_fill()