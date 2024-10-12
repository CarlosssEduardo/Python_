# Exe.27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# ATE - 5 - KG:  
# Morango R$ 2,50 por kg
# Maçã R$ 1,80 por kg

# ACIMA DE - 5 - KG:
# Morango R$ 2,20 por kg
# Maçã R$ 1,50 por kg

# Se o cliente comprar mais de 8 kg em frutas ou o valor total da compra ultrapassar R$ 25,00 receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# def - é uma palavra-chave em Python usada para definir uma função. 
def frutas_maça_morango(frutas):
    # "while True:" Cria um loop que continua pedindo a resposta até que o usuário insirar "morango" ou "maçã".
  while True:
    frutas = input(frutas + "Morango ou Maçã--> ").strip().lower()
    # if frutas in ["morango", "maçã"]:: Verifica se a resposta está entre as válidas. Se sim, a função retorna a resposta e o loop termina. Caso contrário, repete.
    if frutas in ["morango", "maçã"]:
      return frutas
    else:
      print("Resposta inválida. Por favor, responda com 'morango' ou 'maçã'.")

frutas = frutas_maça_morango("\nQual fruta você deseja comprar? ")
valor = float(input(f"\nQuantos Kg de {frutas} você deseja comprar? "))

if frutas == "morango" and valor <= 5:
  preço = valor * 2.50
  print("\nO KG do Morango custa R$ 2,50 Reais.")
  print(f"\nO valor a ser pago de Morango é R$ {preço:.2f} Reais.")
elif frutas == "morango" and valor > 5:
  preço = valor * 2.20
  print("\nO Kg do Morango custa R$ 2,20 Reais.")
  print(f"\nO valor a ser pago de Morango é R$ {preço:.2f} Reais.")

if frutas == "maçã" and valor <= 5:
  preço = valor * 1.80
  print("\nO Kg da Maçã custa R$ 1.80 Reais.")
  print(f"\nO valor a ser pago de Maçã é R$ {preço:.2f} Reais. ")
elif frutas == "maçã" and valor > 5:
  preço = valor * 1.50
  print("\nO KG da Maçã custa R$ 1.50 Reais.")
  print(f"\nO valor a ser pago de Maçã é R$ {preço:.2f} Reais.")

if frutas == "morango" and valor > 8 or frutas == "maçã" and valor > 8 or preço >= 25:
  desconto = 0.10 # 10% de desconto.
  total_com_desconto = preço - (preço * desconto)
  print(f"\nVocê ganhou 10% de desconto")
  print(f"\nO valor total de {frutas} com desconto é R$ {total_com_desconto:.2f} Reais.")