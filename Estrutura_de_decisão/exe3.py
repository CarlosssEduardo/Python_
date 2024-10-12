#Exe.3 - Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print("\nDigite F para Feminino e M para Masculino")
sexo = input("\nDigite o seu sexo--> ")
if sexo == "F" or sexo == "f":
  print("\nF - Feminino")
elif sexo == "M" or sexo == "m":
  print("\nM - Masculino")
else:
  print("\nSexo Inválido")