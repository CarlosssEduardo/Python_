# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
print(" ##### LOJA DE TINTA ##### ")

area = int(input(" Insirar o Tamanho em M² da Area a ser Pintada: --> "))
litros = ( area / 6 ) * 1.1
latas = math.ceil ( litros / 18 )
valor_lata = latas * 80
galoes = math.ceil ( litros / 3.6 )
valor_galoes = galoes * 25

mixlatas = round( litros / 18 )
mixgaloes = round (( litros - mixlatas * 18 ) / 3.6 )
if ((litros - (mixlatas * 18 ) % 3.6 != 0)):
    mixgaloes += 1
    total_mix = ( mixlatas * 80 ) + ( mixgaloes * 25 )
    print( f" \n Ser for compra so latas de 18 litros ira precisar de {latas} latas e ira custar o valor de {valor_lata:.2f} Reais ")
    print( f" \n Ser for compra so galões de 3.6 litros ira precisar de {galoes} galoes e ira custar o valor de { valor_galoes:.2f} Reais")
    print( f" \n Ser desejar mesclar latas e galoes para dar o que precisar realmente será necessario {mixlatas} lata(s) e {mixgaloes} Galão e ira custar o total do {total_mix:.2f} Reais")