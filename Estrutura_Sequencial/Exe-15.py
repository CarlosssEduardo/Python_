# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
print(" ##### CALCULO DE SALÁRIO ##### ")
# O cálculo do salário é determinado pela soma do salário dividido por 30 dias, e então dividido pelo número de horas trabalhadas no mês.
mês = input( " Qual Mês desejar Calcular: -->" )
ganhos_por_horas = float(input( f" Quanto você ganhou por hora no mês de {mês}:--> "))
horas_trabalhadas = float(input(" Quantas horas você dedicou ao trabalho: --> "))
salario_bruto = ganhos_por_horas * horas_trabalhadas
print( f" \n No mês de {mês}, o seu Salário Bruto foi de: {salario_bruto:.2f} Reais" )
inss = salario_bruto*8/100
print( f" Você Pagou de Inss o Valor de: {inss:.2f} Reais" )
sindicato = salario_bruto*5/100
print( f" Você pagou de Sindicato o Valor de: {sindicato:.2f} Reais" )
imposto_renda = salario_bruto*11/100
print( f" Você Pagou de Imposto de Renda o Valor de R$: {imposto_renda:.2f} Reais")
desconto = inss + sindicato + imposto_renda
print(f" O valor de Desconto do seu salário e R$: {desconto:.2f} Reais" )
salario_liquido = salario_bruto - desconto
print( f" Seu salário Liquido e R$: {salario_liquido:.2f} Reais" )