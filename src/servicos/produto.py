import conexao
import servicos.usuario as usuario
import servicos.vendedor as vendedor


global minhaColecao
db = conexao.conectar()
minhaColecao = db.Produto


def criarProduto():
    while True:
        descricao = str(input("Descrição: "))
        produtoEscolhido = minhaColecao.find_one({"descricao": descricao})
        if produtoEscolhido != None:
            print("\nProduto já cadastrado!")
            print("Digite outra descrição!\n")
        else:
            break
    preco = str(input("Preço(R$): "))
    while True:
        validacao = is_float(preco)
        if validacao:
            precoValidado = float(preco)
            break
        else:
            print("\nDigite uma valor valido!\n")
            preco = str(input("Digite o preço(R$): "))
    quantidadeProduto = str(input("Quantidade: "))
    while True:
        if quantidadeProduto.isnumeric():
            quantidadeValidada = int(quantidadeProduto)
            break
        else:
            print("\nDigite um número inteiro!\n")
            quantidadeProduto = str(input("Digite a quantidade: "))
    listaNomeEmailVendedor = vendedor.vinculaProdutoVendedor(descricao, preco, quantidadeProduto)
    if listaNomeEmailVendedor != True:
        vendedorObjeto = {
        "nome": listaNomeEmailVendedor[0],
        "email": listaNomeEmailVendedor[1]
        }
        produto = {
            "descricao": descricao,
            "preco": precoValidado,
            "quantidade": quantidadeValidada,
            "vendedor": vendedorObjeto
        }
        print(f'\nProduto cadastrado com sucesso!\n')
        minhaColecao.insert_one(produto)

def atualizarProduto():
    produtoEscolhido = consultaProduto()
    novoPreco = str(input("Digite o novo preço(R$): "))
    while True:
        validacao = is_float(novoPreco)
        if validacao:
            novoPrecoValidado = float(novoPreco)
            break
        else:
            print("Digite uma valor valido!")
            novoPreco = str(input("Digite o novo preço(R$): "))
    novaQuantidade = str(input("Digite a nova quantidade: "))
    while True:
        if novaQuantidade.isnumeric():
            novaQuantidadeValidada = int(novaQuantidade)
            break
        else:
            print("Digite um número inteiro!")
            novaQuantidade = str(input("Digite a nova quantidade: "))
    atualizacao = {
        "$set": {
            "preco": novoPrecoValidado,
            "quantidade": novaQuantidadeValidada
        }        
    }
    vendedor.alterarQuantidadeProdutoVendedor(novaQuantidade, produtoEscolhido)
    minhaColecao.update_one(produtoEscolhido, atualizacao)
    print(f'\nProduto {produtoEscolhido["descricao"]} atualizado com sucesso!\n')
    
def listarProduto():
    produtoEscolhido = consultaProduto()
    print("\nProduto")
    print(f"\nDescrição: {produtoEscolhido["descricao"]}")
    print(f"Preço: R${produtoEscolhido["preco"]:.2f}")
    print(f"Quantidade: {produtoEscolhido["quantidade"]}")
    print("\nVendedor\n")
    print(f"Nome: {produtoEscolhido["vendedor"]["nome"]}")
    print(f"Email: {produtoEscolhido["vendedor"]["email"]}")

def deletarProduto():
    produtoEscolhido = consultaProduto()
    vendedor.desvinculaProdutoVendedor(produtoEscolhido)    
    usuario.desvinculaProdutoFavorito(produtoEscolhido)
    minhaColecao.delete_one(produtoEscolhido)
    print(f'\nO produto {produtoEscolhido["descricao"]} foi deletado com sucesso!\n')    

def consultaProduto():
    while True:
        descricao = str(input("Descrição do produto: "))
        produtoEscolhido = minhaColecao.find_one({"descricao": descricao})
        if produtoEscolhido == None:
            print("Nenhum produto encontrado")
            descricao = None            
        else:
            break
    return produtoEscolhido

def diminuirQuantidadeProduto(quantidadeCompra, produto):
    produtoEscolhido = minhaColecao.find_one({"descricao": produto["descricao"]})    
    quantidadeEstoque = produtoEscolhido["quantidade"]  
    resultado = quantidadeEstoque - quantidadeCompra
    while resultado < 0:
        print(f"Só existem {quantidadeEstoque} no estoque!")
        quantidadeCompra = int(input(f"Unidades de produtos compradas(max = {quantidadeEstoque}): "))
        resultado = quantidadeEstoque - quantidadeCompra
    atualizacao = {
        "$set": {
            "quantidade": resultado
        }
    }
    minhaColecao.update_one(produto, atualizacao)
    return [quantidadeCompra, resultado]

def is_float(texto):
    try:
        float(texto)
        return True
    except ValueError:
        return False
    
def desvincularVendedorProduto(listaDescricao):
    for descricao in listaDescricao:
       produto = minhaColecao.find_one({"descricao": descricao})
       minhaColecao.delete_one(produto)