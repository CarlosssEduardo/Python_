# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
# Para usar o valor de pi em Python, importamos o módulo math, que já tem o valor de pi pré-definido.
raio = int(input(" Qual o valor do raio que deseja saber a área total ?"))
# A fórmula da área do círculo é a multiplicação de pi pelo quadrado do raio.
area = math.pi * raio ** 2
print( f" O valor total da área e = {area}." )