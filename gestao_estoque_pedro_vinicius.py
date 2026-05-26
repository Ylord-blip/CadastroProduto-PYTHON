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
def cadastrar_produto(nome, preco, quantidade, categoria):
        cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade, categoria)
        VALUES (?, ?, ?, ?)
        """, (nome, preco, quantidade, categoria))

        conexao.commit()
        print("Produto cadastrado com sucesso!")


def consultar_estoque(produto_id=None):
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        print("\nProdutos cadastrados:")

        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]} | Quantidade: {produto[3]} | Categoria: {produto[4]}")

def registrar_entrada(produto_id, quantidade):
    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade + ?
    WHERE id = ?
    """, (quantidade, produto_id))

    if cursor.rowcount > 0:
        conexao.commit()
        print("Estoque atualizado")
    else:
        print("Produto não encontrado")
       
def registrar_saida(produto_id, quantidade):
        list_products = cursor.execute('SELECT * FROM produtos').fetchall()

        for produto in list_products:
          print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]} | Quantidade: {produto[3]} | Categoria: {produto[4]}")

        resultado = cursor.execute("""SELECT quantidade FROM produtos WHERE id = ?""", (produto_id,)).fetchone()

        if resultado:
          qtde_atual = resultado[0]

          if quantidade <= qtde_atual:
            cursor.execute("""
            UPDATE produtos
            SET quantidade = ?
            WHERE id = ?
            """, (qtde_atual - quantidade, produto_id))
            conexao.commit()
            print("Estoque atualizado")
            consultar_estoque(produto_id=None)
          else:
            print("Quantidade indisponível")
        else:
          print("Produto não encontrado")

def estoque_abaixo_limite(limite):
    cursor.execute("""
    SELECT nome, quantidade 
    FROM produtos 
    WHERE quantidade < ?
    """, (limite,))

    produto_baixo = cursor.fetchall()

    if produto_baixo:
        print("\nSeu estoque está abaixo do limite")

        for produto in produto_baixo:
            nome = produto[0]
            quantidade = produto[1]
            print(f"Nome: {nome} e Quantidade: {quantidade}")
    else:
        print("Seu estoque está acima do limite")

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("3 - Registrar Entrada")
    print("4 - Registrar Saída")
    print("5 - Estoque abaixo do limite")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
        categoria = input("Categoria: ")
        cadastrar_produto(nome, preco, quantidade, categoria)

    elif opcao == 2:
        consultar_estoque(produto_id=None)

    elif opcao == 3:
        produto_id = int(input("Qual o ID do produto?"))
        quantidade = int(input("Qual a quantidade adicionada?"))
        registrar_entrada(produto_id, quantidade)

    elif opcao == 4:
        produto_id = int(input("Qual o ID do produto?"))
        quantidade= int(input("Qual a quantidade a ser retirada?"))
        registrar_saida(produto_id, quantidade)

    elif opcao == 5:
        limite = int(input("Digite o limite mínimo de estoque: "))
        estoque_abaixo_limite(limite)

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

conexao.close()