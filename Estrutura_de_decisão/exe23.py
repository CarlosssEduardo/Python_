#Exe.23 Faça um programa que peça um número inteiro e informe se o nuḿero é inteiro ou decimal. Dica: utilize uma função de arrendondamento.
x = float(input("Digite um número--> "))
# if (x == round(x)) verifica se x é um número inteiro. Se a condição for verdadeira, então x é um número inteiro; se for falsa, x é um número decimal.
# Função round(x): Essa função arredonda o número x para o inteiro mais próximo. Se x já for um número inteiro, round(x) retornará x mesmo.
if (x == round (x)):
  print(f"\n{int(x)} é um número inteiro")
else:
  print(f"\n{x} é um número decimal")