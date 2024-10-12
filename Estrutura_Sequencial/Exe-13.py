# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# A) Para homens: (72.7*h) - 58
# B) Para mulheres: (62.1*h) - 44.7
sexo = input(" Qual seu sexo ? h/m: --> ")

if sexo == "h":
    altura = float(input(" Qual a sua altura: --> "))
    peso = float(input(" Qual Seu peso: --> "))
    peso_ideal = ( 72.7 * altura ) - 58
    perca_peso = peso_ideal - peso
    if peso > peso_ideal:
        print( f" O seu peso atual é: {peso} quilogramas e o seu peso ideal é: {peso_ideal:.3f} quilogramas. Você precisa Perder: {perca_peso:.3f} quilogramas." )
    else:
        print( f" O seu peso atual é: {peso} quilogramas e o seu peso ideal é: {peso_ideal:.3f} quilogramas. Você precisa Ganhar: {perca_peso:.3f} quilogramas." )
else:
    altura_mulher = float(input(" Qual sua Altura: --> "))
    peso_mulher = float(input(" Qual seu Peso: --> "))
    peso_ideal_mulher = ( 62.1 * altura_mulher ) - 44.7
    perca_peso_mulher = peso_ideal_mulher - peso_mulher
    if peso_mulher > perca_peso_mulher:
        print( f" O seu peso atual é: {peso_mulher} quilogramas e o seu peso ideal é: {peso_ideal_mulher:.3f} quilogramas. Você precisa Perder: {perca_peso_mulher:.3f} quilogramas." )
    else:
        print(f" O seu peso atual é: {peso_mulher} quilogramas e o seu peso ideal é: {peso_ideal_mulher:.3f} quilogramas. Você precisa Ganhar: {perca_peso_mulher:.3f} quilogramas." )