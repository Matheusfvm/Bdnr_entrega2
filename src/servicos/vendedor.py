import conexao
import servicos.produto as produto


global minhaColecao
db = conexao.conectar()
minhaColecao = db.Vendedor


def criarVendedor():
    nome = str(input("Nome: "))
    documento = str(input("Número do documento: "))
    while True:
        email = str(input("Email: "))
        usuarioEscolhido = minhaColecao.find_one({"email": email})
        if usuarioEscolhido != None:
            print("\nVendedor já cadastrado")
            print("Digite outro email!\n")
        else:
            break
    senha = str(input("Senha: "))
    listaProduto = []
    vendedor = {
        "nome": nome,
        "documento": documento,
        "email": email,
        "senha": senha,
        "lista_produto": listaProduto
    }
    minhaColecao.insert_one(vendedor)
    print(f'\nVendedor {nome} cadastrado com sucesso!\n')

def atualizarVendedor():
    minhaColecao = db.Vendedor
    vendedorEscolhido = consultaVendedor()
    novoNome = str(input("Nome: "))
    novoEmail = str(input("Email: "))
    novaSenha = str(input("Senha: "))
    atualizacao = {
        "$set": {
            "nome": novoNome,
            "email": novoEmail,
            "senha": novaSenha
            }        
    }
    minhaColecao.update_one(vendedorEscolhido, atualizacao)
    print(f'\nVendedor {novoNome} atualizado com sucesso!\n')

def listarVendedor():
    vendedorEscolhido = consultaVendedor()
    print("\nVendedor")
    print(f"\nNome: {vendedorEscolhido['nome']}")
    print(f"Documento: {vendedorEscolhido['documento']}")
    print(f"Email: {vendedorEscolhido['email']}")
    print(f"Senha: {vendedorEscolhido['senha']}\n")
    print("Produtos")
    for produto in vendedorEscolhido['lista_produto']:
        print(f"\nDescrição: {produto['descricao']}")
        print(f"Preço: R${produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")
        print("\n---------------------------------------\n")

def deletarVendedor():
    vendedorEscolhido = consultaVendedor()
    listaDescricaoProduto = []
    for elementoProduto in vendedorEscolhido["lista_produto"]:
        listaDescricaoProduto.append(elementoProduto["descricao"])
    produto.desvincularVendedorProduto(listaDescricaoProduto)
    minhaColecao.delete_one(vendedorEscolhido)
    print(f'\nVendedor {vendedorEscolhido["nome"]} foi deletado com sucesso!\n')

def consultaVendedor():
    while True:
        email = input(str("Email do vendedor: "))
        vendedorEscolhido = minhaColecao.find_one({"email": email})
        if vendedorEscolhido == None:
            print("Nenhum vendedor encontrado")
            email = None
        else:
            break
    return vendedorEscolhido

def vinculaProdutoVendedor(descricao, preco, quantidadeProduto):
    vendedorEscolhido = consultaVendedor()
    produto = {
        "descricao": descricao,
        "preco": preco,
        "quantidade": quantidadeProduto
    }
    if produto in vendedorEscolhido["lista_produto"]:
        return True
    else:
        atualizacao = {
        "$push": {
            "lista_produto": produto
        }
        }
        minhaColecao.update_one(vendedorEscolhido, atualizacao)
        return [vendedorEscolhido["nome"], vendedorEscolhido["email"]]

def desvinculaProdutoVendedor(produto):
    vendedorEscolhido = minhaColecao.find_one({"email": produto["vendedor"]["email"]})
    atualizacaoListaProduto = {
        "$pull": {
            "lista_produto": {
                "descricao": produto["descricao"]
            }
        }
    }
    minhaColecao.update_one(vendedorEscolhido, atualizacaoListaProduto)

def alterarQuantidadeProdutoVendedor(quantidadeProduto, produto):
    email = produto["vendedor"]["email"]
    filtro = {
        "email": email, "lista_produto.descricao": produto["descricao"]
    }   
    atualizacaoListaProduto = {
        "$set": {
            "lista_produto.$.quantidade": quantidadeProduto
        }
    }
    minhaColecao.update_one(filtro, atualizacaoListaProduto)