# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.
joao_peixe = int(input(" Qual o peso do peixe que João capturou em KG: --> "))
regulamento_pescar = 50 
multa = joao_peixe - regulamento_pescar
excesso = float ( 4.00 * multa )
if joao_peixe > regulamento_pescar:
    print( f"\n João Excedeu o limite de peixe estabelecido pelo regulamento de São Paulo: {multa} KG")
    print( f"\n João excedeu: {multa}KG e deverar pagar R$: {excesso} Reais de Multa" )
else:
    print( "\n João Não Excedeu o limite de peixe estabelecido pelo regulamento" )