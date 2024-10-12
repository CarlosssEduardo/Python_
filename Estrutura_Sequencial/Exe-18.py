# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
print (" ##### CALCULO DO TEMPO ##### ")
mb = int(input(" Qual o tamanho do arquivo para download em (MB):--> "))
link = int(input(" Qual a Velocidade de um link de Internt em ( MBPS): --> "))
tempo = ( mb / (link / 8 ) / 60 )
print( f" Para efeturar um download de {mb} MB com a Velocidade de {link} MBPS ira demorar {tempo:.0f} minutos ")