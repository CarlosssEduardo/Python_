# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print('########## Área do Quadrado ##########')
#A fórmula da área do quadrado é a multiplicação da base pela altura e o resultado é dividido por 2.
base = int(input("  Insirar a Base do Quadrado= "))
altura = int(input(" Insirar a Altura do Quadrado= "))
resultado = ( base * altura ) / 2
dobro = resultado * 2
print( f" A área do Quadrado e= {resultado} ")
print( f" \n O dobro da area do Quadrado e= {dobro} ")