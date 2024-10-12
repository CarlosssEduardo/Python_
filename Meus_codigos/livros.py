import itertools
import locale

# Lista de dados (livros)
livros = [
    {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'ano': 1954, 'valor': 59.90},
    {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949, 'valor': 49.90},
    {'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry', 'ano': 1943, 'valor': 39.90},
    {'titulo': 'Duna', 'autor': 'Frank Herbert', 'ano': 1965, 'valor': 59.90},
    {'titulo': 'A Revolução dos Bichos', 'autor': 'George Orwell', 'ano': 1945, 'valor': 49.90},
    {'titulo': 'Harry Potter e a Pedra Filosofal', 'autor': 'J.K. Rowling', 'ano': 1997, 'valor': 69.90},
]

def buscar_livro(palavra_chave, lista_livros):
    resultados = []
    for livro in lista_livros:
        if palavra_chave.lower() in livro['titulo'].lower() or palavra_chave.lower() in livro['autor'].lower():
            resultados.append(livro)
    return resultados

def mostrar_carrossel_livros():
    palavra_chave = input("Digite a palavra-chave para buscar (ou 's' para sair): ").strip().lower()
    if palavra_chave == 's':
        print("Busca encerrada!")
        return

    resultados = buscar_livro(palavra_chave, livros)

    if not resultados:
        print("Nenhum livro encontrado.")
    else:
        print("Resultados da busca:")
        try:
            # Tenta configurar a localidade para pt_BR
            locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        except locale.Error:
            # Se a localidade não for encontrada, tenta usar uma localidade alternativa
            try:
                locale.setlocale(locale.LC_MONETARY, 'pt_BR')
            except locale.Error:
                # Caso nenhuma localidade pt_BR seja encontrada, usa a localidade padrão do sistema
                locale.setlocale(locale.LC_MONETARY, '')
        for i, livro in enumerate(resultados, start=1):
            preco_formatado = locale.currency(livro.get('preco', livro.get('valor')), grouping=True)
            print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']}) - {preco_formatado}")

# Executar a função
mostrar_carrossel_livros()