
#exe12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do salário bruto, mas não e desconto (é a empresa que deposita). O salário Liquido corresponde ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salario bruto até 900 (inclusive) - isento
# salário Bruto até 1500 (inclusive) - desconto de 5%
# salário Bruto até 2500 (inclusive) - desconto de 10%
# salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
mes = input("\nDigite o mês de referência: ")
x = mes.capitalize()
hora_trabalhada = float(input(f"\nDigite a hora de trabalho-->  "))
quantidades_horas =  float(input(f"\nDigite a quantidade de horas trabalhadas no mês {x}-->  "))
salario_base = hora_trabalhada * quantidades_horas
print(f"\nSalário Base no Mês de {x} é--> R$ {salario_base:.2f}")
if salario_base <= 900:
  print(f"\nIsento de imposto de renda")
elif salario_base > 900 and salario_base <= 1500:
  desconto = salario_base * 0.05
  print(f"\nDesconto de 5% do Imposto de Renda é--> R$ {desconto:.2f}")
elif salario_base > 1500 and salario_base <= 2500:
  desconto = salario_base * 0.1
  print(f"\nDesconto de 10% do Imposto de Renda é--> R$ {desconto:.2f}")
elif salario_base > 2500:
  desconto = salario_base * 0.2
  print(f"\nDesconto de 20% do Imposto de Renda é--> R$ {desconto:.2f}")
inss = salario_base * 0.1
print(f"\nDesconto de 10% do inss é--> R$ {inss:.2f}")
fgts = salario_base * 0.11
print(f"\nDeposito de 11% do FGTS é--> R$ {fgts:.2f}")
total_desconto = inss + desconto
print(f"\nTotal de descontos é--> R$ {total_desconto}")
salario_liquido= salario_base - total_desconto
print(f"\nSalário Liquido é--> R$ {salario_liquido:.2f}")