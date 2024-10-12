# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
x = int(input("Digite um número--> "))
y = int(input("Digite um Segundo número--> "))
z = int(input("Digite um Terceiro número--> "))
if x > y and x > z:
  print("O maior número é o", x)
elif y > x and y > z:
  print("O maior número é o", y)
elif z > x and z > y:
  print("O maior número é o", z)
  if x < y and x < z:
    print("O menor número é o", x)
  elif y < x and y < z:
    print("O menor número é o", y)
  elif z < x and z < y:
    print("O menor número é o", z)
else:
  print("Os números são iguais")