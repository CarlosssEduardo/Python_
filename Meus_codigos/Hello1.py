import random
import time

def construir_frase(frase, delay= 0.5 ):
    """
    Constrói uma frase caractere por caractere em linhas separadas.

    Args:
        frase (str): A frase a ser construída.
    """

    for i in range(len(frase)):
        print(frase[:i+1])
        time.sleep(delay)

# Exemplo de uso:
frase = "hello world"
while True:
    construir_frase(frase, 0.2)