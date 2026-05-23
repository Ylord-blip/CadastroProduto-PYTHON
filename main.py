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

nome = input("Nome do produto: ")
preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade: "))
categoria = input("Categoria: ")

cursor.execute("""
INSERT INTO produtos (nome, preco, quantidade, categoria)
VALUES (?, ?, ?, ?)
""", (nome, preco, quantidade, categoria))

conexao.commit()
conexao.close()

print("Produto adicionado com sucesso!")