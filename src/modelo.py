from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import json

uri = "mongodb+srv://entregaBranquinho:av8K1mJCP9jcHy@cluster0.dodulda.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercado_livre

#------------------------ METODOS DE USUARIO ------------------------------

def criarUsuario():
    minhaColecao = db.Usuario
    print("\n----INSERÇÃO DE USUÁRIO----\n")
    nome = input(str("Nome: "))
    cpf = input(str("CPF: "))
    email = input(str("Email: "))
    senha = input(str("Senha: "))
    telefone = input(str("Número telefone: "))
    listaEnderecos = []
    listaCompras = []
    listaFavoritos = []
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
        listaEnderecos.append(endereco)
        key = input("Deseja cadastrar um novo endereço(S/N)? ")        
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "enderecos": listaEnderecos,
        "compras": listaCompras,
        "favoritos": listaFavoritos
    }
    minhaColecao.insert_one(usuario)
    print(f'\nUsuário {nome} inserido com sucesso!\n')


def listarUsuario():
    minhaColecao = db.Usuario
    print("\n----LISTAGEM DE USUÁRIO----\n")
    email = input(str("Email do usuário: "))
    usuarioEscolhido = consultaUsuario(email)
    return usuarioEscolhido    
    """ listaAtributos = []
    incremento = 1
    for atributo in dadosUsuario:
        listaAtributos.append(atributo)
    for incremento <= len(listaAtributos):
        atributoString = listaAtributos
        print(dadosUsuario[])
 """
    
def atualizarUsuario():
    minhaColecao = db.Usuario
    print("\n----ATUALIZAÇÃO DE USUÁRIO----\n")
    email = input(str("Email do usuário: "))
    usuarioEscolhido = {"email" : email}
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
    print(f'\nUsuário {novoNome} atualizado com sucesso!')

def deletarUsuario():
    minhaColecao = db.Usuario
    print("\n----DELETAR DE USUÁRIO----")
    email = input(str("Email do usuário: "))
    usuarioEscolhido = {"email" : email}
    minhaColecao.delete_one(usuarioEscolhido)
    print(f'\nUsuário deletado com sucesso!\n')

def consultaUsuario(email):
    minhaColecao = db.Usuario
    while True:
        usuarioEscolhido = minhaColecao.find_one({"email": email})
        if usuarioEscolhido == None:
            print("Nenhum usuário encontrado")
            usuarioEscolhido = None
            usuarioEscolhido = input(str("Digite um novo email(Usuário): "))
        else:
            break
    return usuarioEscolhido

""" def favorito()
    minhaColecao = db.Usuario
    em """
#----------------------------- METODOS DE VENDEDOR --------------------------------

def criarVendedor():
    minhaColecao = db.Vendedor
    print("\n----INSERÇÃO DE VENDEDOR----\n")
    nome = input(str("Nome: "))
    documento = input(str("Número do documento: "))
    email = input(str("Email: "))
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
    print(f'Vendedor {nome} cadastrado com sucesso!')

def atualizarVendedor():
    minhaColecao = db.Vendedor
    print("\n----ATUALIZAÇÃO DE VENDEDOR----\n")
    email = input(str("Email do vendedor: "))
    vendedorEscolhido = {"email" : email}
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
    minhaColecao = db.Vendedor
    print("\n----LISTAGEM DE VENDEDOR---\n")
    email = input(str("Email do vendedor: "))
    vendedorEscolhido = consultaVendedor(email)
    return vendedorEscolhido

def deletarVendedor():
    minhaColecao = db.Usuario
    print("\n----DELETAR DE VENDEDOR----\n")
    email = input(str("Email do vendedor: "))
    vendedorEscolhido = {"email" : email}
    minhaColecao.delete_one(vendedorEscolhido)
    print(f'\nVendedor deletado com sucesso!\n')

def consultaVendedor(email):
    minhaColecao = db.Vendedor
    while True:
        vendedorEscolhido = minhaColecao.find_one({"email": email})
        if vendedorEscolhido == None:
            print("Nenhum vendedor encontrado")
            email = None
            email = input(str("Digite um novo email(Vendedor): "))
        else:
            break
    return vendedorEscolhido

def vincularProdutoVendedor(email, descricao, preco, quantidadeProduto):
    minhaColecao = db.Vendedor
    vendedorEscolhido = consultaVendedor(email)
    listaProduto = []
    produto = {
        "descricao": descricao,
        "preco": preco,
        "quantidade_produto": quantidadeProduto 
    }
    listaProduto.append(produto)
    atualizacao = {
        "$set": {
            "lista_produto": listaProduto
        }
    }
    minhaColecao.update_one(vendedorEscolhido, atualizacao)
    return [vendedorEscolhido["nome"], vendedorEscolhido["email"]]

def desvinculaProdutoVendedor(email, descricao):
    minhaColecao = db.Vendedor
    vendedorEscolhido = consultaVendedor(email)
    atualizacaoListaProduto = {
        "$pull": {
            "lista_produto": {
                "descricao": descricao
            }
        }
    }
    minhaColecao.update_one(vendedorEscolhido, atualizacaoListaProduto)


#----------------------------- METODOS DE PRODUTO --------------------------------

def criarProduto():
    minhaColecao = db.Produto
    print("\n----INSERÇÃO DE PRODUTO----")
    descricao = input(str("Descriçao: "))
    preco = input(str("Preço: "))
    quantidadeProduto = input(str("Quantidade: "))
    emailVendedor = input(str("Email do vendedor: "))
    listaNomeEmailVendedor = vincularProdutoVendedor(emailVendedor, descricao, preco, quantidadeProduto)
    vendedor = {
        "nome": listaNomeEmailVendedor[0],
        "email": listaNomeEmailVendedor[1]
    }
    produto = {
        "descricao": descricao,
        "preco": preco,
        "quantidade_produto": quantidadeProduto,
        "vendedor_produto": vendedor
    }
    print(f'\nProduto cadastrado com sucesso!\n')
    minhaColecao.insert_one(produto)

    
def listarProduto():
    minhaColecao = db.Produto
    print("\n----LISTAGEM DE PRODUTO---\n")
    descricao = input(str("Descrição produto: "))
    produtoEscolhido = consultaProduto(descricao)
    return produtoEscolhido

def deletarProduto():
    minhaColecao = db.Produto
    print("\n----DELETAR DE PRODUTO----\n")
    descricao = input(str("Descrição produto: "))
    email = input(str("Email do vendedor em que o produto pertence: "))
    produtoEscolhido = {"descricao" : descricao}
    desvinculaProdutoVendedor(email, descricao)
    minhaColecao.delete_one(produtoEscolhido)
    print(f'\nProduto deletado com sucesso!\n')    

def consultaProduto(descricao):
    minhaColecao = db.Produto
    while True:
        produtoEscolhido = minhaColecao.find_one({"descricao": descricao})
        if produtoEscolhido == None:
            print("Nenhum produto encontrado")
            produtoEscolhido = None
            produtoEscolhido = input(str("Digite um nova descrição: "))
        else:
            break
    return produtoEscolhido


#----------------------------- METODOS DE COMPRA --------------------------------

def criarCompra():
    minhaColecao = db.Compra
    print("\n----INSERÇÃO DE COMPRA----\n")
    dataCompra = datetime.now()
    listaProduto = []
    dataCompraFormatada = dataCompra.strftime("%d/%m/%Y %H:%M")
    dataCompraEntrega = input(str("Data da entrega(dd/mm/AAAA): "))
    key = "S"
    while key == "S":
        descricaoProduto = input(str("Descrição do produto: "))
        produtoEscolhido = consultaProduto(descricaoProduto)
        listaProduto.append(produtoEscolhido)
        key = input(str("Deseja comprar um outro produto(S/N)? "))
    emailUsuario = input(str("Digite o email do usuário: "))
    usuarioEscolhido = consultaUsuario(emailUsuario)
    usuarioObjeto = {
        "nome": usuarioEscolhido["nome"],
        "email": usuarioEscolhido["email"]
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
      print(compra)
    return listaCompra


