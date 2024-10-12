#exe19. Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da virgula entre outros. exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.
numero = int(input("Digite um número inteiro menor que 1000--> "))
# Aqui é feito a verificação se o número é menor que 1000, caso seja então o proximo bloco será executado.
if numero < 1000:
  # "//" E o operador de divisão inteira, ele divide dois números e retorna o resultado apenas a parte inteira do resultado da divisão.
  centena = numero // 100
  # "%" Esse operador retorna exatamente o valor que sobra apos a divisão. 
  # Exemplo: 10/3 = 3,3333..(mas só consideramos a parte inteira, que e 3)
  # Multiplique o quociente pelo divisor: 3 * 3 = 9
  # Subtraia o resultado da divisão do número original: 10 - 9 = 1
  # Dessa forma temos o resto.
  dezena = (numero % 100) // 10
  unidade = numero % 10
  print(f"\n{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades")