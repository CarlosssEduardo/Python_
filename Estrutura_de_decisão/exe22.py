# Exe.22 Faça um programa que leia um número inteiro e diga ser ele é par ou impar. Dica utilize o operador de modulo (resto de divisão) %
x = int(input("Digite um número inteiro--> "))
# A variavel "x % 2 == 0:" está verificando se x(número na qual o usúario digita) é um número par. Se o resto da divisão de x por 2 for 0, isso significa que x é divisível por 2 e, portanto, é um número par. Se não for 0, então x` é um número ímpar.
if x % 2 == 0:
  print(f"\nO número {x} é par")
else:
  print(f"\nO número {x} é impar")