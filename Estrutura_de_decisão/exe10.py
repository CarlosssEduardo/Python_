# Exe.10 Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", Conforme o caso.
turno = input("Qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno--> ")
if turno == "M":
  print("Bom Dia!")
elif turno == "V":
  print("Boa Tarde!")
elif turno == "N":
  print("Boa Noite!")
else:
  print("Valor Inválido")