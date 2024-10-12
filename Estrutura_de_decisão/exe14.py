#exe14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. Atribuição de conceitos obedece à tabela abaixo. O algoritmo deve mostra na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E.
nota1 = float(input("\nDigite a primeira nota--> "))
nota2 = float(input("\nDigite a segunda nota--> "))
media = (nota1 + nota2) / 2
print(f"\nSUA MÉDIA DE APROVEITAMENTO É--> {media}")
if media >= 9.0 and media <= 10.0:
  print(f"\nCONCEITO--> A")
  print(f"\nVOCÊ FOI APROVADO")
elif media >= 7.5 and media < 9.0:
  print(f"\nCONCEITO B")
  print(f"\nVOCÊ FOI APROVADO")
elif media >= 6.0 and media < 7.5:
  print(f"\nCONCEITO C")
  print(f"\nVOCÊ FOI APROVADO")
elif media >= 4.0 and media < 6.0:
  print(f"\nCONCEITO D")
  print(f"\nVOCÊ FOI REPROVADO")
elif media >= 0.0 and media < 4.0:
  print(f"\nCONCEITO E")
  print(f"\nVOCÊ FOI REPROVADO")