#Exe.28 - O hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# ATÉ 5 KG:
# File Duplo: R$ 4,90 por kg
# Alcatra: R$ 5,90 por Kg
# Picanha: R$ 6,90 por Kg

# ACIMA DE 5 KG:
# File Duplo: R$ 5,80 por Kg
# Alcatra: R$ 6,80 por Kg
# Picanha: R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreve um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


# Aqui Decidir Contruir uma tabela de preços para cada tipo de carne e mostra na tela para o usuario.
print("\n------ Hipermercado Tabajara ------")
print("\nTipos de carne disponiveis: ")
print("\n1 - File Duplo - R$ 4,90 por Kg")
print("\n2 - Alcatra - R$ 5,90 por Kg")
print("\n3 - Picanha - R$ 6,90 por Kg")
# def - definir uma função
def tipo_carne(tipo):
  # while True - faz com que o bloco de código seja executado enquanto a condição for verdadeira.
  while True:
    # a string strip() e usada para remover espaços em branco do início e do final de uma string.
    # a string lower() e usada para converter uma string para letras minúsculas.
    tipo = input(tipo + "1/2/3:").strip().lower()
    # o metodo in - verifica se um valor está presente em uma sequência.
    if tipo in ["1", "2", "3"]:
      return tipo
    else:
      print("Resposta inválida. Por favor, responda com '1' ou '2' ou '3'--> ")

tipo = tipo_carne("\nQual tipo de carne você deseja comprar--> ")

if tipo == "1":
  tipo = "File Duplo"
  carne = float(input(f"\nQuantos Kg de {tipo} você deseja comprar--> "))
  valor = carne * 4.90
  print(f"\nPreço normal: R$ {valor:.2f}")
  desconto = 0.05
  preço_com_desconto = valor - (valor * desconto)

elif tipo =="2":
  tipo = "Alcatra"
  carne = float(input(f"\nQuantos Kg de {tipo} você deseja comprar--> "))
  valor = carne * 5.90
  print(f"\nPreço normal: R$ {valor:.2f}")
  desconto = 0.05
  preço_com_desconto = valor - (valor * desconto)

elif tipo == "3":
  tipo = "Picanha"
  carne = float(input(f"\nQuantos Kg de {tipo} você deseja comprar--> "))
  valor = carne * 6.90
  print(f"\nPreço normal: R$ {valor:.2f}")
  desconto = 0.05
  preço_com_desconto = valor - (valor * desconto)


# Aqui é feito a verificação se o cliente é do tipo Tabajara, se for então o desconto será de 5%.
# para isso criei outra função de bloco de codigo chamada cupom_fiscal.
def cupom_fiscal(cartao):
  while True:
    cartao = input(cartao + "s/n: ").strip().lower()
    if cartao in ["s", "n"]:
      return cartao
    else:
      print("Resposta inválida. Por favor, responda com 's' ou 'n'--> ")


cartao = cupom_fiscal("\nVocê deseja pagar com cartão Tabajara ? ")


print("\n------ CUPOM FISCAL ------\n")
if cartao == "s":
  print(f"\nTipo de carne: {tipo}")
  print(f"\nQuantidade: {carne} Kg")
  print(f"\nTipo de pagamento: Cartão Tabajara")
  print(f"\nPreço normal: R$ {valor:.2f}")
  print(f"\nDesconto: R$ {valor * desconto:.2f}")
  print(f"\nPreço Total: R$ {preço_com_desconto:.2f}")

else:
  print(f"\nTipo de carne: {tipo}")
  print(f"\nQuantidade: {carne} Kg")
  print(f"\nTipo de pagamento: Dinheiro")
  print(f"\nPreço normal: R$ {valor:.2f}")
  print(f"\nDesconto: R$ 0.00")