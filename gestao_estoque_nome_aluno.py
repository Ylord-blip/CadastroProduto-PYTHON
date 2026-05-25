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

conexao.commit()
def cadastrar_produto():
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


def consultar_estoque():
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        print("\nProdutos cadastrados:")

        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]} | Quantidade: {produto[3]} | Categoria: {produto[4]}")


def registrar_entrada():
        list_products = cursor.execute('SELECT * FROM produtos').fetchall()

        for produto in list_products:
          print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]} | Quantidade: {produto[3]} | Categoria: {produto[4]}")

        produto_id = int(input("Qual o ID do produto?"))
        quantidade = int(input("Qual a quantidade adicionada?"))

        cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE id = ?
        """, (quantidade, produto_id))

        conexao.commit()

        print("Estoque atualizado")
        consultar_estoque()

def registrar_saida():
        list_products = cursor.execute('SELECT * FROM produtos').fetchall()

        for produto in list_products:
          print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]} | Quantidade: {produto[3]} | Categoria: {produto[4]}")


        produto_id = int(input("Qual o ID do produto?"))
        # Fix: Pass produto_id as a single-element tuple (produto_id,)
        # Fix: Use fetchone() to get the actual quantity, not just the cursor object
        qtde_estoque_result = cursor.execute("""SELECT quantidade FROM produtos WHERE id = ?""", (produto_id,)).fetchone()
        conexao.commit()


        if qtde_estoque_result:
          qtde_atual = qtde_estoque_result[0]

          quantidade_retirada = int(input("Qual a quantidade a ser retirada?"))
        
          if (quantidade_retirada <= qtde_atual):
            cursor.execute("""
            UPDATE produtos
            SET quantidade = ?
            WHERE id = ?
            """, (qtde_atual - quantidade_retirada, produto_id))
            conexao.commit()
          else:
            print("Quantidade indisponível")
        else:
          print("Produto não encontrado")
        
        print("Estoque atualizado")
        consultar_estoque()

def estoque_abaixo_limite():
    Consulta = cursor.execute('SELECT quantidade FROM produtos WHERE id = ?').fetchall()

    qtde_estoque_resuslt = cursor.execute("""SELECT quantidade FROM produtos WHERE id = ?""",).fetchone()
    conexao.commit()

    if (Consulta <= "15"):
            cursor.execute("""
            UPDATE produtos
            SET quantidade = ?
            WHERE id = ?
            """, (qtde_atual, Consulta))
            conexao.commit()
            print("Seu banco está abaixo do limite do estoque")
    else:
        print("A quantidade está acima do limite")
while True:
    print("\n1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("3 - Registrar Entrada")
    print("4 - Registrar Saída")
    print("5 - Estoque abaixo do limite")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        cadastrar_produto()

    elif opcao == 2:
        consultar_estoque()

    elif opcao == 3:
        registrar_entrada()

    elif opcao == 4:
        registrar_saida()

    elif opcao == 5:
        estoque_abaixo_limite()

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

conexao.close()