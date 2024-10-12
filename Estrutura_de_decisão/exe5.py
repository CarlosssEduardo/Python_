#Exe.5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
print("\n---- Cálculo de Média ----")

nota1 = float(input("\nDigite a Primeira nota--> "))
nota2 = float(input("\nDigite a Segunda nota--> "))
media = (nota1 + nota2) / 2
if media >= 7 and media < 10:
  print(f"\nA média do aluno é {media:.2f} e ele está APROVADO")
elif media < 7:
  print(f"\nA média do aluno é {media:.2f} e ele está REPROVADO")
else:
  print(f"\nA média do aluno é {media:.2f} e ele está APROVADO COM DISTINÇÃO")