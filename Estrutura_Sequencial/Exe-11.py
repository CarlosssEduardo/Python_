# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo .
# B) a soma do triplo do primeiro com o terceiro.
# C) o terceiro elevado ao cubo.
x = int(input(" Insirar o Primeiro Número Inteiro: -- > "))
y = int(input(" Insirar o Segundo Número Inteiro: -- >"))
z = float(input(" \n Insirar o Primeiro Número Real: -- >"))
soma = ( x + y ) + z 
print( f" Resultado da soma de dois números inteiros com um numero real e= {soma}")
a = ( y / 2 ) * ( 2 * x )
print( f" O produto do dobro do primeiro com metade do segundo e= {a} ")
b = (x * 3 ) + z 
print( f" a soma do triplo do primeiro com o terceiro e= {b} ")
c = z ** 3 
print( f" O terceiro elevado ao cubo e= {c} ")
