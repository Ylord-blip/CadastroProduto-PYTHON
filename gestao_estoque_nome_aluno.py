produtos = [
    {
        "nome": "Mouse Gamer",
        "preco": 89.90,
        "quantidade": 15,
        "categoria": "Periféricos"
    },
    {
        "nome": "Teclado Mecânico",
        "preco": 249.90,
        "quantidade": 8,
        "categoria": "Periféricos"
    },
    {
        "nome": "Monitor 24 polegadas",
        "preco": 799.90,
        "quantidade": 25,
        "categoria": "Monitores"
    },
    {
        "nome": "Headset Gamer",
        "preco": 159.90,
        "quantidade": 12,
        "categoria": "Áudio"
    },
    {
        "nome": "Webcam Full HD",
        "preco": 199.90,
        "quantidade": 30,
        "categoria": "Acessórios"
    }
]

import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    categoria TEXT NOT NULL
)
""")

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("3 - Registrar Entrada")
    print("4 - Registrar Saída")
    print("5 - Consultar Estoque")
    print("6 - Estoque abaixo do limite")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

conexao.commit()
def cadastrar_produto(nome, categoria, preco, quantidade):
    if opcao == 1:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
        categoria = input("Categoria: ")

        cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade, categoria)
        VALUES (?, ?, ?, ?)
        """, (nome, preco, quantidade, categoria))

        conexao.commit()

        print("Produto cadastrado com sucesso!")

        
def consultar_estoque(produto_id):
    if opcao == 2:
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        print("\nProdutos cadastrados:")

        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]} | Quantidade: {produto[3]} | Categoria: {produto[4]}")


def registrar_saida(produto_id, quantidade):
        produto_id = int(input("Qual o ID do produto?"))
        quantidade = int(input("Qual a quantidade adicionada?"))

        cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE id = ?
        """, (quantidade, produto_id))

        conexao.commit()

        print("Estoque atualizado")

    if opcao == 0:
        print("Saindo...")
        break

conexao.close()