# Exe.24 - Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.
numero = float(input("Digite um número--> "))
# Primeiro, verificamos se o número é par ou ímpar. usado o operador de módulo (%) para verificar se o número é divisível por 2. Se o resto da divisão for 0, o número é par, caso contrário, é ímpar.
if numero % 2 == 0:
  print(f"\nO número {numero} é par")
else:
  print(f"\nO número {numero} é impar")
# Agora, Verificamos ser o número e inteiro ou decimal. Para isso, usamos a função int() para converter o número em um número inteiro e verificar se o resultado é igual ao número original. Se for igual, o número é inteiro, caso contrário e decimal. O modulo "round" é usado para arredondar o número para o inteiro mais próximo.
if (numero == round(numero)):
  print(f"\nO número {numero} é inteiro")
# Aqui, verificamos se o número é positivo ou negativo. Usamos o operador de comparação > para verificar se o número é maior que zero. Se for, o número é positivo, caso contrário, é negaivo. 
if numero > 0:
  print(f"\nO número {numero} é positivo")
else:
  print(f"\nO número {numero} é negativo")
  print(f"\nO número {numero} é decimal")