# Exe26. Um posto está vendendo combustiveis com a seguinte tabela de descontos: 
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90.

# "def" é uma palavra-chave em Python usada para definir uma função.
def tipo_alcool_gasolina(tipo):
    # "while True:" Cria um loop que continua pedindo a resposta até que o usuário insira "a" ou "g".
    while True:
        tipo = input(tipo + " (a/g): ").strip().lower()
        # if tipo in ["a", "g"]:: Verifica se a resposta está entre as válidas. Se sim, a função retorna a resposta e o loop termina. Caso contrário, repete.
        if tipo in ["a", "g"]:
            # "return" o comando return é usado para encerrar a execução de uma função e enviar um valor de volta para o chamador. 
            return tipo
        else:
            print("\nResposta inválida. Por favor, responda com 'a' ou 'g'.")

tipo = tipo_alcool_gasolina("\nTipo de combustível--> ")
if tipo == "a":
    valor = float(input("\nQuantos litros de álcool você desejar abastecer--> "))
    preço = valor * 1.90
    print(f"\nO valor a ser pago sem desconto de Álcool é R$ {preço:.2f} Reais")
elif tipo == "g":
    valor = float(input("\nQuantos litros de gasolina você desejar abastecer--> "))
    preço = valor * 2.50
    print(f"\nO valor a ser pago de Gasolina sem desconto é R$ {preço:.2f} Reais.")
# O desconto e calculado de acordo com a quantidade de litros vendidos.
# O percentual de desconto é representado como um número decimal em cálculos. 
# O desconto é de 3%. Para converter a porcentagem em uma forma decimal, dividimos o percentual por 100. Então, 3% se torna 0,03 quando convertido para um decimal.
# Dessa forma o Calculo e primeiro multiplicado pelo valor do combustivel, depois multiplicado pelo percentual de desconto e por fim subtraido do valor do combustivel.
desconto_alcool1 = preço - (preço * 0.03)
desconto_alcool2 = preço - (preço * 0.05)
if tipo == "a" and valor <= 20:
    print(f"\nO valor a ser pago com desconto de Álcool é R$ {desconto_alcool1:.2f} Reais.")
elif tipo == "a" and valor > 20:
    print(f"\nO valor a ser pago com desconto de Álcool é R$ {desconto_alcool2:.2f} Reais.")

desconto_gasolina1 = preço - (preço * 0.06) 
desconto_gasolina2 = preço - (preço * 0.10)
if tipo == "g" and valor <= 20:
    print(f"\nO valor a ser pago com desconto de Gasolina é R$ {desconto_gasolina1:.2f} Reais.")
elif tipo == "g" and valor > 20:
    print(f"\nO valor a ser pago com desconto de Gasolina é R$ {desconto_gasolina2:.2f} Reais.")