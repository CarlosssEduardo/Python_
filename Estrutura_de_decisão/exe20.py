#Exe20. Faça um Programa para a leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
# Agora, pediremos ao aluno para inserir sua nota. O tipo 'float' permite que o número seja decimal, e a função 'input' captura o valor digitado pelo usuário."
x = float(input("\nDigite sua Primeira Nota--> "))
y = float(input("\nDigite sua Segunda Nota--> "))
z = float(input("\nDigite sua Terceira Nota--> "))
#Para calcular a média de um conjunto de números: Some todos os números e Divida o total pela quantidade de números.
media = (x + y + z) / 3
# "if" Bloco de código executado se a condição for verdadeira
# ":.2f" é uma especificação de formatação usada para exibir números com uma precisão específica e é comumente usada com strings formatadas.
# ":" — Indica o início da especificação de formatação dentro de uma string formatada.
# ".2" — Define o número de casas decimais após o ponto decimal.
# "f" - Indica que o número deve ser formatado como um número de ponto flutuante (float).
if media >= 7 and media < 10:
  print(f"\nAprovado com média {media:.2f}")
# Bloco de código executado se condição 2 for verdadeira
elif media < 7:
  print(f"\nReprovado com média {media:.2f}")
# Bloco de código executado se condição 3 for verdadeira  
elif media == 10:
  print(f"\nAprovado com Distinção com média {media:.2f}")
# Bloco de código executado se nenhuma das condições anteriores for verdadeira
else:
  print("\nErro")