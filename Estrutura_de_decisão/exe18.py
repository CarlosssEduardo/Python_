#exe18. Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
dia = int(input("\nDigite o dia--> "))
mes = int(input("\nDigite o mês--> "))         
ano = int(input("\nDigite o ano--> "))
# meses representa os meses do ano, colocado em uma lista para facilitar a verificação, assim a contagem do mes começa em 1 e não em 0, pois zero e definido em aspas.
# A barra colocado dentro da lista é para que o programa não reconheça como uma barra, e sim como um caractere de separação.
meses = [ "", "Janeiro", "Fevereiro",\
         "Março", "Abril", "Maio",\
         "Junho", "Julho", "Agosto",\
         "Setembro", "Outubro", "Novembro",]
# Aqui é feito a verificação se o dia é válido, se o mes é válido e se o ano é válido. dessa forma o if só será executado se todas as condições forem verdadeiras. caso contrário o else será executado, imprimido a devida mensagem de erro.
if mes == 1 and dia <= 31 or mes == 3 and dia <= 31 or mes == 5 and dia <= 31 or mes == 7 and dia <= 31 or mes == 8 and dia <= 31 or mes == 10 and dia <= 31 or mes == 12 and dia <= 31:
         print(f"\n{dia} de {meses[mes]} de {ano} e uma data válida")
elif mes == 4 and dia <= 30 or mes == 6 and dia <= 30 or mes == 9 and dia <= 30 or mes == 11 and dia <= 30:
         print(f"\n{dia} de {meses[mes]} de {ano} e uma data válida")
         # Aqui é feito a verificação se o dia é válido, pois no mês de feverreiro sabemos que sao apenas 28 dias, quando for 29 dias o ano é bissexto.
elif mes == 2 and dia <= 28:
         print(f"\n{dia} de {meses[mes]} de {ano} e uma data válida")
         # aqui verificamos se o ano é bissexto, caso seja então o mês de fevereiro tem 29 dias.
# Como calcular um ano bissexto Se o ano não termina em 00, ele é bissexto caso seja divisível por 4. Exemplos: 1988, 1992, 1996, 2004, e assim por diante. Nota: Um número é divisível por 4 se a sua dezena (1988 = 88) é divisível por 4.
elif mes == 2 and dia == 29 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
         print(f"\n{dia} de {meses[mes]} de {ano} e uma data válida")
         # o else será executado caso a data não seja válida ou seja inválida.
else:
         print(f"\n{dia} de {meses[mes]} de {ano} nao e uma data inválida")
         print(f"\n{dia} e maior que o dia máximo do mês {meses[mes]}")