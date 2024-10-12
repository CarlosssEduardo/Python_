import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-9C9BDFL;"
    "Database=Pythonbd;"
)

conexao = pyodbc.connect(dados_conexao)
print("---> Conexão Bem Sucedida <---")

cursor = conexao.cursor()
id = 3
cliente = input("Digite o nome do Cliente--> ")
produto = input("Digite o Produto--> ")
data = input("Digite a Data de Hoje-->")
preco = input("Digite o Preço do Produto escolhido--> ")
quantidade = 1

comando = f"""INSERT INTO Vendas( id_venda, cliente, produto, data_venda, preco, quantidade )
VALUES 
    ({id}, '{cliente}', '{produto}', '{data}', '{preco}', {quantidade})"""
cursor.execute(comando)
cursor.commit()