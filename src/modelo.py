from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime


uri = "mongodb+srv://entregaBranquinho:N4UNMCRomo4fJ3@cluster0.dodulda.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercado_livre

#------------------------ METODOS DE USUARIO ------------------------------

def criarUsuario():
    minhaColecao = db.Usuario
    nome = input(str("Nome: "))
    cpf = input(str("CPF: "))
    while True:
        email = input(str("Email: "))
        usuarioEscolhido = minhaColecao.find_one({"email": email})
        if usuarioEscolhido != None:
            print("\nUsuário já cadastrado!")
            print("Digite outro email!\n")
        else:
            break            
    senha = input(str("Senha: "))
    telefone = input(str("Número telefone: "))
    listaEndereco = []
    listaCompra = []
    listaFavorito = []
    key = "S"
    while key == "S":
        cep = input(str("CEP: "))
        ruaAvenida = input(str("Nome da rua ou avenida: "))
        numeroEndereco = input(str("Número endereço: "))
        bairro = input(str("Bairro: "))
        cidade = input(str("Cidade: "))
        estado = input(str("Estado(Sigla): "))
        endereco = {
            "cep": cep,
            "rua/avenida": ruaAvenida,
            "numeroEndereco": numeroEndereco,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,            
            }
        listaEndereco.append(endereco)
        key = input("Deseja cadastrar um novo endereço(S/N)? ")        
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "lista_endereco": listaEndereco,
        "lista_compra": listaCompra,
        "lista_favorito": listaFavorito
    }
    minhaColecao.insert_one(usuario)
    print(f'\nUsuário {nome} inserido com sucesso!\n')


def listarUsuario():    
    usuarioEscolhido = consultaUsuario()
    print(f'\n{usuarioEscolhido}\n')    
    
def atualizarUsuario():
    minhaColecao = db.Usuario
    usuarioEscolhido = consultaUsuario()
    novoNome = input(str("Nome: "))
    novoCpf = input(str("CPF: "))
    novoEmail = input(str("Email: "))
    novaSenha = input(str("Senha: "))
    novoTelefone = input(str("Número telefone: "))
    atualizacao = {
        "$set": {
            "nome": novoNome,
            "cpf": novoCpf,
            "email": novoEmail,
            "senha": novaSenha,
            "telefone": novoTelefone
        }        
    }
    minhaColecao.update_one(usuarioEscolhido, atualizacao)
    print(f'\nUsuário {novoNome} atualizado com sucesso!\n')

def deletarUsuario():
    minhaColecao = db.Usuario
    usuarioEscolhido = consultaUsuario()
    minhaColecao.delete_one(usuarioEscolhido)
    print(f'\nUsuário {usuarioEscolhido["nome"]} foi deletado com sucesso!\n')

def criarEndereco():
    minhaColecao = db.Usuario
    usuarioEscolhido = consultaUsuario()
    cep = input(str("CEP: "))
    ruaAvenida = input(str("Nome da rua ou avenida: "))
    numeroEndereco = input(str("Número endereço: "))
    bairro = input(str("Bairro: "))
    cidade = input(str("Cidade: "))
    estado = input(str("Estado(Sigla): "))
    enderecoObjeto = {
        "cep": cep,
        "rua/avenida": ruaAvenida,
        "numeroEndereco": numeroEndereco,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado, 
    }
    atualizazao = {
        "$push": {
            "lista_endereco": enderecoObjeto
        }
    }
    minhaColecao.update_one(usuarioEscolhido, atualizazao)
    print(f'\nEndereço cadastrado com sucesso!\n')

def consultaUsuario():
    minhaColecao = db.Usuario
    while True:
        email = input(str("Email do usuário: "))
        usuarioEscolhido = minhaColecao.find_one({"email": email})
        if usuarioEscolhido == None:
            print("Nenhum usuário encontrado")
            email = None
        else:
            break
    return usuarioEscolhido

def vinculaCompraUsuario(listaProduto, data_entrega):
    minhaColecao = db.Usuario
    usuarioEscolhido = consultaUsuario()
    compra = {
        "lista_produto": listaProduto,
        "data_entrega": data_entrega
    }
    atualizacao = {
        "$push": {
            "lista_compra": compra
        }
    }   
    minhaColecao.update_one(usuarioEscolhido, atualizacao)
    return [usuarioEscolhido["nome"], usuarioEscolhido["email"]]

def criarFavorito():
    minhaColecao = db.Usuario
    usuarioEscolhido = consultaUsuario()
    produtoEscolhido = consultaProduto()
    produtoObjeto = {
        "descricao": produtoEscolhido["descricao"],
        "preco": produtoEscolhido["preco"],
        "vendedor": produtoEscolhido["vendedor"]        
    }
    consultaFavorito = usuarioEscolhido["lista_favorito"]
    if produtoObjeto in consultaFavorito:
        print("Produto já está entre os favoritos!")
    else:
        atualizacao = {
            "$push": {
                "lista_favorito": produtoObjeto 
            }
        }
        minhaColecao.update_one(usuarioEscolhido, atualizacao)
        print(f'\nO produto {produtoEscolhido["descricao"]} está entre seus favoritos!\n')
    

def listarFavorito():
    usuarioEscolhido = consultaUsuario()           
    print(f'\n{usuarioEscolhido["lista_favorito"]}\n')

def deletarFavorito():
    minhaColecao = db.Usuario      
    usuarioEscolhido = consultaUsuario()
    produtoEscolhido = consultaProduto()
    produtoObjeto = {
        "descricao": produtoEscolhido["descricao"],
        "preco": produtoEscolhido["preco"],
        "vendedor": produtoEscolhido["vendedor"]
    }
    atualizacaoListaFavorito = {
        "$pull": {
            "lista_favorito": produtoObjeto
        }
    }
    minhaColecao.update_one(usuarioEscolhido, atualizacaoListaFavorito)
    print(f'\nO produto {produtoObjeto["descricao"]} deixou da sua lista de favoritos!\n')

def desvinculaProdutoFavorito(produto):
    minhaColecao = db.Usuario    
    produtoObjeto = {
        "descricao": produto["descricao"],
        "preco": produto["preco"],
        "vendedor": produto["vendedor"]
    }
    atualizacaoListaFavorito = {
        "$pull": {
            "lista_favorito": produtoObjeto
        }
    }
    listaUsuario = []
    for usuario in minhaColecao.find():
        if len(usuario["lista_favorito"]) != 0:
            if produtoObjeto in usuario["lista_favorito"]:
                minhaColecao.update_one(usuario, atualizacaoListaFavorito)


#----------------------------- METODOS DE VENDEDOR --------------------------------

def criarVendedor():
    minhaColecao = db.Vendedor
    nome = input(str("Nome: "))
    documento = input(str("Número do documento: "))
    while True:
        email = input(str("Email: "))
        usuarioEscolhido = minhaColecao.find_one({"email": email})
        if usuarioEscolhido != None:
            print("\nVendedor já cadastrado")
            print("Digite outro email!\n")
        else:
            break
    senha = input(str("Senha: "))
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
    novoNome = input(str("Nome: "))
    novoDocumento = input(str("Número do documento: "))
    novoEmail = input(str("Email: "))
    novaSenha = input(str("Senha: "))
    atualizacao = {
        "$set": {
            "nome": novoNome,
            "documento_vendedor": novoDocumento,
            "email": novoEmail,
            "senha": novaSenha
            }        
    }
    minhaColecao.update_one(vendedorEscolhido, atualizacao)
    print(f'\nVendedor {novoNome} atualizado com sucesso!\n')

def listarVendedor():
    vendedorEscolhido = consultaVendedor()
    print(f'\n{vendedorEscolhido}\n')

def deletarVendedor():
    minhaColecao = db.Vendedor
    vendedorEscolhido = consultaVendedor()
    minhaColecao.delete_one(vendedorEscolhido)
    print(f'\nVendedor {vendedorEscolhido["nome"]} foi deletado com sucesso!\n')

def consultaVendedor():
    minhaColecao = db.Vendedor
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
    minhaColecao = db.Vendedor
    vendedorEscolhido = consultaVendedor()
    produto = {
        "descricao": descricao,
        "preco": preco,
        "quantidade_produto": quantidadeProduto
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
    minhaColecao = db.Vendedor
    vendedorEscolhido = consultaVendedor()
    atualizacaoListaProduto = {
        "$pull": {
            "lista_produto": {
                "descricao": produto["descricao"]
            }
        }
    }
    minhaColecao.update_one(vendedorEscolhido, atualizacaoListaProduto)


#----------------------------- METODOS DE PRODUTO --------------------------------

def criarProduto():
    minhaColecao = db.Produto
    while True:
        descricao = input(str("Descrição: "))
        produtoEscolhido = minhaColecao.find_one({"descricao": descricao})
        if produtoEscolhido != None:
            print("\nProduto já cadastrado!")
            print("Digite outra descrição!\n")
        else:
            break
    preco = input(str("Preço: "))
    quantidadeProduto = input(str("Quantidade: "))
    listaNomeEmailVendedor = vinculaProdutoVendedor(descricao, preco, quantidadeProduto)
    if listaNomeEmailVendedor != True:
        vendedor = {
        "nome": listaNomeEmailVendedor[0],
        "email": listaNomeEmailVendedor[1]
        }
        produto = {
            "descricao": descricao,
            "preco": preco,
            "quantidade": quantidadeProduto,
            "vendedor": vendedor
        }
        print(f'\nProduto cadastrado com sucesso!\n')
        minhaColecao.insert_one(produto)

def atualizarProduto():
    minhaColecao = db.Produto
    produtoEscolhido = consultaProduto()
    novoPreco = input(str("Digite o novo preço: "))
    novaQuantidade = input(str("Digite a nova quantidade: "))
    atualizacao = {
        "$set": {
            "preco": novoPreco,
            "quantidade": novaQuantidade
        }        
    }
    minhaColecao.update_one(produtoEscolhido, atualizacao)
    print(f'\nUsuário {produtoEscolhido["descricao"]} atualizado com sucesso!\n')
    
def listarProduto():
    produtoEscolhido = consultaProduto()
    print(f'\n{produtoEscolhido}\n')

def deletarProduto():
    minhaColecao = db.Produto
    produtoEscolhido = consultaProduto()
    desvinculaProdutoVendedor(produtoEscolhido)    
    desvinculaProdutoFavorito(produtoEscolhido)
    minhaColecao.delete_one(produtoEscolhido)
    print(f'\nO produto {produtoEscolhido["descricao"]} foi deletado com sucesso!\n')    

def consultaProduto():
    minhaColecao = db.Produto
    while True:
        descricao = input(str("Descrição do produto: "))
        produtoEscolhido = minhaColecao.find_one({"descricao": descricao})
        if produtoEscolhido == None:
            print("Nenhum produto encontrado")
            descricao = None            
        else:
            break
    return produtoEscolhido


#----------------------------- METODOS DE COMPRA --------------------------------

def criarCompra():
    minhaColecao = db.Compra
    dataCompra = datetime.now()
    listaProduto = []
    dataCompraFormatada = dataCompra.strftime("%d/%m/%Y %H:%M")
    key = "S"
    while key == "S":
        produtoObjeto = {}
        produtoEscolhido = consultaProduto()
        quantidadeProdutoCompra = input(str("Unidades de produtos compradas: "))        
        produtoObjeto = {
            "descricao": produtoEscolhido["descricao"],
            "preco": produtoEscolhido["preco"],
            "quantidade_produto_compra": quantidadeProdutoCompra,
            "vendedor": produtoEscolhido["vendedor"] 
        }
        listaProduto.append(produtoObjeto)
        key = input(str("Deseja comprar um outro produto(S/N)? "))
    dataCompraEntrega = input(str("Data da entrega(dd/mm/AAAA): "))
    listaNomeEmailUsuario = vinculaCompraUsuario(listaProduto, dataCompraEntrega)  
    usuarioObjeto = {
        "nome": listaNomeEmailUsuario[0],
        "email": listaNomeEmailUsuario[1]
    }
    compra = {
        "usuario": usuarioObjeto,
        "lista_produto": listaProduto,
        "data_compra": dataCompraFormatada,
        "data_entrega_compra": dataCompraEntrega
    }

    minhaColecao.insert_one(compra)
    print(f'\nCompra realizada com sucesso!\n')

def listarCompra():
    minhaColecao = db.Compra
    print("\n----LISTAGEM DAS COMPRAS---\n")
    listaCompra = []
    for compra in minhaColecao.find():
      listaCompra.append(compra)
    print(f'\n{listaCompra}\n')


