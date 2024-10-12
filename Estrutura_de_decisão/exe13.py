#exe13.Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
x = int(input("\nDigite um número de 1 a 7: "))
if x == 1:
  print(f"\nDomingo")
elif x == 2:
  print("\nSegunda-Feira")
elif x == 3:
  print("\nTerça-Feira")
elif x == 4:
  print("\nQuarta-Feira")
elif x == 5:
  print("\nQuinta-Feira")
elif x == 6:
  print("\nSexta-Feira")
elif x == 7:
  print("\nSábado")
else:
  print("\nValor inválido")