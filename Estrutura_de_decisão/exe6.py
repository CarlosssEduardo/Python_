#Faça um pograma que leia três números e mostre o maior deles.
x = int(input('Digite o primeiro número--> '))
y = int(input('Digite o segundo número-->'))
z = int(input('Digite o terceiro número-->'))
if x > y and x > z:
  print('O maior número e',x)
elif y > x and y > z:
  print('O maior número e',y)
elif z > x and z > y:
  print('O maior número e',z)
else:
  print('Os números são iguais')