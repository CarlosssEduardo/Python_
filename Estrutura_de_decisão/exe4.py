#Exe.4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
while True:
  letra = input("\nDigite uma letra--> ").strip()
  # O metodo isalpha() - verifica se todos os caracteres da string são letras. Se não forem, o loop é interrompido com break.
  if letra.isalpha():
    # O break -  em Python é usado para interromper ou sair de um loop antes que ele tenha percorrido todas as suas iterações. 
    break
  else:
    print(f"\nA letra {letra} não é uma letra")


if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
  print(f"\nA letra {letra} é uma vogal")
else:
  print(f"\nA letra {letra} é uma consoante")