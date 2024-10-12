# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input(" Qual a sua altura ? "))
peso_ideal = ( 72.7 * altura ) - 58
print( f" Seu peso ideal e = {peso_ideal:.3f} KG ")