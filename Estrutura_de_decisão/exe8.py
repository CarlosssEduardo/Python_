#Faça um programa que pergunte o preço de três produtos e informe qual produto voce deve comprar, sabendo que a decisão é sempre pelo mais barato.
x1 = float(input("Digite o preço do primeiro produto--> "))
x2 = float(input("Digite o preço do segundo produto--> "))
x3 = float(input("Digite o preço do terceiro produto--> "))
if x1 < x2 and x1 < x3:
  print("O produto mais barato que você deve comprar é o primeiro produto que custa R$", x1)
elif x2 < x1 and x2 < x3:
  print("O produto mais barato que você deve comprar é o segundo produto que custa R$", x2)
elif x3 < x1 and x3 < x2:
  print("O produto mais barato que você deve comprar é o terceiro produto que custa R$", x3)
else:
  print("Todos os Produtos são baratos")