#Faça um programa que leia três números e mostre-os em ordem decrescente.
x = int(input("Digite um número--> "))
y = int(input("Digite um Segundo número--> "))
z = int(input("Digite um terceiro número--> "))
if x >= y and x >= z and y >= z:
  print("A ordem descrescente e--> ", x, y, z)
elif x >= y and x >= z and z >= y:
  print("A ordem descrescente e--> ", x, z, y)
elif y >= x and y >= z and x >= z:
  print("A ordem descrescente e--> ", y, x, z)
elif y >= x and y >= z and z >= x:
  print("A ordem descrescente e--> ", y, z, x)
elif z >= x and z >= y and x >= y:
  print("A ordem descrescente e--> ", z, x, y)
elif z >= x and z >= y and y >= x:
  print("A ordem descrescente e--> ", z, y, x)