#Exe.25 - Faça um prgrama que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já tr_abalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responde positivamente a 2 questões ela deve ser classficada como "Suspeitar", entre 3 a 4 como "Coumplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

#Explicação do Codigo--> "def" é uma palavra-chave em Python usada para definir uma função. Uma função é um bloco de código reutilizável que executa uma tarefa específica e pode ser chamado várias vezes ao longo do programa.

# Função pergunta_sim_nao: Esta função faz a pergunta e só aceita "sim" ou "não" como resposta.
def pergunta_sim_nao(pergunta):
  # "while True:" Cria um loop que continua pedindo a resposta até que o usuário insira "sim" ou "não".
  while True:
    # resposta.strip().lower(): Remove espaços extras e converte a resposta para minúsculas, para garantir que variações como "Sim" ou "SIM" sejam aceitas.
      resposta = input(pergunta + " (s/n): ").strip().lower()
    # if resposta in ["sim", "não"]:: Verifica se a resposta está entre as válidas. Se sim, a função retorna a resposta e o loop termina. Caso contrário, repete a pergunta.
    # O operador "in" verifica a existência de um valor em uma lista. No caso o "sim" ou "não"
      if resposta in ["s", "n"]:
        # "return" o comando return é usado para encerrar a execução de uma função e enviar um valor de volta para o chamador.
          return resposta
      else:
          print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

# Perguntas do Inquerito Policial.
# Aqui criamos um lista chamada "perguntas" que contém as respotas do inquerito policial.
resposta1 = pergunta_sim_nao("\nTelefonou para a Vitima?")
resposta2 = pergunta_sim_nao("\nEsteve no local do crime?")
resposta3 = pergunta_sim_nao("\nMora perto da vitima?")
resposta4 = pergunta_sim_nao("\nDevia para a vitima?")
resposta5 = pergunta_sim_nao("\nJá trabalhou com a vitima?")
# A lista "perguntas" é usada para armazenar as respostas do inquerito policial. 
perguntas = [resposta1, resposta2, resposta3, resposta4, resposta5]
# Aqui criamos uma variavel chamada "if perguntas" que conta quantas respostas "sim" o usuario respondeu no inquerito policial.
# O metodo string count() retorna o número de vezes que um valor especificado aparece.

if perguntas.count("s") == 2:
  print("\nSuspeito")
  if perguntas.count("s") == 3 or perguntas.count("s") == 4:
     print("\nCumplice")
     if perguntas.count("s") == 5:
        print("\nAssassino")
  else:
        print("\nInoncente")