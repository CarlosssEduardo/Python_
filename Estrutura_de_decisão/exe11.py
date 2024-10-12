# Exe11. As Organizações Tabjara resolveram dar um aumento de salário aos seus colaboradores e me contrataram para desenvolver o programa que calculará os reajustes.
#. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#. salário até R$ 280,00(incluido): aumento de 20%
#. salário entre R$ 280,00 e R$ 700,00: aumento de 15%
#. salário entre R$ 700,00 e R$ 1500,00: aumento de 10%
#. salário de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:
#. salário antes do reajuste;
#. percentual de aumento aplicado;
#. valor do aumento;
#. novo salário, após o aumento.
salario = float(input("\nDigite seu salário--> "))
if salario <= 280:
  percentual = 20
elif salario > 280 and salario <= 700:
  percentual = 15
elif salario > 700 and salario <= 1500:
  percentual = 10
elif salario > 1500:
  percentual = 5
print(f"\nSalário antes do reajuste--> R$ {salario:.2f} \n")
print(f"Percentual de aumento aplicado--> {percentual}" "%\n")
print(f"Valor do aumento--> R$ {salario * percentual / 100:.2f} \n")
print(f"Novo salário, após o aumento--> R$ {salario + salario * percentual / 100:.2f}")