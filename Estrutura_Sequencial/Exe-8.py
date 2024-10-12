# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print(" ##### CALCULO DE SALÁRIO ##### ")
# O cálculo do salário é determinado pela soma do salário dividido por 30 dias, e então dividido pelo número de horas trabalhadas no mês.
ganhos_por_horas = float(input(" Qual é o valor da sua remuneração por hora? "))
horas_trabalhadas = float(input(" Quantas horas você dedicou ao trabalho durante o mês? "))
calculo = ganhos_por_horas * horas_trabalhadas
print( f" \n No mês em questão, o seu salário é R$ {calculo}")