#exe17. Faça um programa que leia um número correspondeten a um determinado ano e informe se este ano é ou não bissexto.
ano = int(input("Digite um ano--> "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f"O ano {ano} é bissexto")
else:
  print(f"O ano {ano} não é bissexto")