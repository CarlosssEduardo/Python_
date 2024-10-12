#exe16. Faça um programa que calcule as raizes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informado ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
a = float(input("Digite o valor de a--> "))
b = float(input("Digite o valor de b--> "))
c = float(input("Digite o valor de c--> "))
delta = b**2 - 4*a*c
if a == 0:
  print(f"\nA equação não é do segundo grau")
elif delta < 0:
  print(f"\nA equação não possui raizes reais")
elif delta == 0:
  print(f"\nA equação possui apenas uma raiz real")
elif delta > 0:
  print(f"\nA equação possui duas raizes reais")
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print(f"\nO valor de x1 é--> {x1}")
print(f"\nO valor de x2 é--> {x2}")
print("\nS-->", x1, "e", x2)