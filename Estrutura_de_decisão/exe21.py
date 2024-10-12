#exe21. Faça um programa para um caixa eletrônico. O programa dverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. o valor minimo é de 10 reias e o máximo de 600 reais. O programa não deve ser preocupar com a quantidade de notas existentes máquina. 
# Exemplo 1: para sacar a quantia de 256reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
print("\n CAIXA ELETRONICO \n")
print("\n ---> O valor minimo para saque é de 10 reais e o valor maximo é de 600 reais <--- \n")
notas = [100, 50, 10, 5, 1]
print(f"\nAs notas disponiveis são: {notas}\n")
valor = int(input("\nDigite o valor do saque--> R$ "))
# Aqui Definimos uma condição para o valor do saque ser maior que 10 e menor que 600. Ser for verdadeiro o programa executa o comando abaixo.
if valor >= 10 and valor <= 600:
  # Aqui definimos uma variavel para o valor do saque. na qual o valor do saque é dividido pela nota de 100.
  print(f"\nVocê receberá {valor//100} notas de 100 reais")
  # Aqui definimos uma variavel para o valor = valor % 100. Que significa que o valor do saque é dividido pelo valor da nota de 100.
  valor = valor % 100
  print(f"\nVocê receberá {valor//50} notas de 50 reais")
  valor = valor % 50
  print(f"\nVocê receberá {valor//10} notas de 10 reais")
  valor = valor % 10
  print(f"\nVocê receberá {valor//5} notas de 5 reais")
  valor = valor % 5
  print(f"\nVocê receberá {valor//1} notas de 1 real")
else: 
  print(f"\n{valor} não é um valor válido para saque, Pois o valor minimo é de R$ 10,00 e o máximo é de R$ 600,00")