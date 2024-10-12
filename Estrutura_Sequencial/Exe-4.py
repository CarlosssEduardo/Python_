# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# Abaixo estão os dados que solicitarão ao usuário que introduza suas notas.
nota1 = float(input(" Insira Sua Primeira Nota: --> "))
nota2 = float(input(" Insira Sua Segunda Nota: --> ")) 
nota3 = float(input(" Insira Sua Terceira Nota: --> "))
nota4 = float(input(" Insira Sua Quarta Nota: --> "))
# Os dados abaixo calcularão a média do usuário, que será obtida somando as 4 notas e dividindo por 4.
# É importante sempre seguir a ordem das operações matemáticas
media = (nota1 + nota2 + nota3 + nota4) / 4
# Por exemplo, se você tem um número float x e quer exibi-lo formatado com duas casas decimais, você pode usar o especificador de formato "{:.2f}".format(x). Isso garante que o número seja exibido com precisão de duas casas decimais.
print(f" A Sua Média e {media:.2f}.")