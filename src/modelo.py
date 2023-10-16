from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://entregaBranquinho:av8K1mJCP9jcHy@cluster0.dodulda.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercado_livre

#------------------------ METODOS DE USUARIO ------------------------------

def criarUsuario():
    minhaColecao = db.Usuario
    print("\n----INSERÇÃO DE USUÁRIO----")
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
    print(f'\nUsuário {nome} inserido com sucesso!')


def listarUsuario():
    minhaColecao = db.Usuario
    print("\n----LISTAGEM DE USUÁRIO----")
    email = input(str("Email do usuário: "))
    usuarioEscolhido = {"email": email}
    dadosUsuario = minhaColecao.find_one(usuarioEscolhido)
    print(dadosUsuario)
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
    print("\n----ATUALIZAÇÃO DE USUÁRIO----")
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
    print(f'\nUsuário deletado com sucesso!')


#----------------------------- METODOS DE VENDEDOR --------------------------------

def criarVendedor():
    minhaColecao = db.Vendedor
    print("\n----INSERÇÃO DE VENDEDOR----")
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
        "produtos": listaProduto
    }
    minhaColecao.insert_one(vendedor)
    print(f'Vendedor {nome} cadastrado com sucesso!')

def atualizarVendedor():
    minhaColecao = db.Vendedor
    print("\n----ATUALIZAÇÃO DE VENDEDOR----")
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
    print(f'\nVendedor {novoNome} atualizado com sucesso!')

def vincularProdutoVendedor(email, descricao, preco, quantidadeProduto):
    minhaColecao = db.Vendedor
    vendedorEscolhido = {}    
    key = True
    while key:
        vendedorEscolhido = minhaColecao.find_one({"email": email})
        if vendedorEscolhido == None:
            print("Nenhum vendedor encontrado")
            email = None
            email = input(str("Digite um email(Vendedor): "))
        else:
            key = False
    produto = {
        "descricao": descricao,
        "preco": preco,
        "quantidade_produto": quantidadeProduto 
    }
    atualizacao = {
        "$set": {
            "produtos": produto
        }
    }
    minhaColecao.update_one(vendedorEscolhido, atualizacao)
    return [vendedorEscolhido["nome"], vendedorEscolhido["email"]]

def listarVendedor():
    minhaColecao = db.Vendedor
    print("\n----LISTAGEM DE VENDEDOR---")
    email = input(str("Email do vendedor: "))
    vendedorEscolhido = {"email": email}
    dadosUsuario = minhaColecao.find_one(vendedorEscolhido)
    print(dadosUsuario)

def deletarDeletar():
    minhaColecao = db.Usuario
    print("\n----DELETAR DE VENDEDOR----")
    email = input(str("Email do vendedor: "))
    vendedorEscolhido = {"email" : email}
    minhaColecao.delete_one(vendedorEscolhido)
    print(f'\nVendedor deletado com sucesso!')

#----------------------------- METODOS DE PRODUTO --------------------------------

def criarProduto():
    minhaColecao = db.Produto
    print("\n----INSERÇÃO DE PRODUTO----")
    descricao = input(str("Descriçao: "))
    preco = input(str("Preço: "))
    quantidadeProduto = input(str("Quantidade: "))
    emailVendedor = input(str("Email do vendedor: "))
    listaAtributoVendedor = vincularProdutoVendedor(emailVendedor, descricao, preco, quantidadeProduto)
    listaVendedor = [{
        "nome": listaAtributoVendedor[0],
        "email": listaAtributoVendedor[1]
    }]
    produto = {
        "descricao": descricao,
        "preco": preco,
        "quantidade_produto": quantidadeProduto,
        "vendedor_produto": listaVendedor
    }
    print(f'\nProduto cadastrado com sucesso!')
    minhaColecao.insert_one(produto)

    
criarProduto()