#exe15. Faça um programa que peça os 3 lados de um triângulo. O programa devera informar se os valores podem ser um triângulo, se o mesmo é: equilátero, isosceles ou escaleno.
#Dicas:
#três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo equilátero: três lados iguais;
#Triângulo isósceles: quaisquer dois lados iguais;
#Triângulo escaleno: três lados diferentes;
l1 = float(input("\nDigite o primeiro lado do triângulo--> "))
l2 = float(input("\nDigite o segundo lado do triângulo--> "))
l3 = float(input("\nDigite o terceiro lado do triângulo--> "))
if l1 + l2 > l3:
  if l1 == l2 == l3:
    print("\nOs lados formam Triângulo Equilátero")
  elif l1 == l2 or l1 == l3 or l2 == l3:
    print("\nOs lados formam um Triângulo Isósceles")
  elif l1 != l2 != l3:
    print("\nOs lados formam um Triângulo Escaleno")
else:
  print("\nOs lados não formam um Triângulo")