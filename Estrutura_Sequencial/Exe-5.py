# Faça um Programa que converta metros para centímetros.
metros =  int(input(" Quantos Metros Desejar Converte em Centimetros: -->"))
# Para realizar a conversão de uma unidade que esta à esquerda para outra que esta à direita. multiplique por 10 cada unidade de medida.
resultado = metros * 100
print(f"\n {metros} Metros e equivalente a {resultado} centimetros")