import conexao
import servicos.produto as produto

global minhaColecao
db = conexao.conectar()
minhaColecao = db.Usuario


def criarUsuario():
    nome = str(input("Nome: "))
    cpf = str(input("CPF: "))
    while True:
        email = str(input("Email: "))
        usuarioEscolhido = minhaColecao.find_one({"email": email})
        if usuarioEscolhido != None:
            print("\nUsuário já cadastrado!")
            print("Digite outro email!\n")
        else:
            break            
    senha = str(input("Senha: "))
    telefone = str(input("Número telefone: "))
    listaEndereco = []
    listaCompra = []
    listaFavorito = []
    key = "S"
    while key == "S":
        cep = str(input("CEP: "))
        ruaAvenida = str(input("Nome da rua ou avenida: "))
        numeroEndereco = str(input("Número endereço: "))
        bairro = str(input("Bairro: "))
        cidade = str(input("Cidade: "))
        estado = str(input("Estado(Sigla): "))
        endereco = {
            "cep": cep,
            "rua_avenida": ruaAvenida,
            "numero": numeroEndereco,
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
    print(f"Nome: {usuarioEscolhido["nome"]}")
    print(f"Cpf: {usuarioEscolhido["cpf"]}")
    print(f"Email: {usuarioEscolhido["email"]}")
    print(f"Senha: {usuarioEscolhido["senha"]}")
    print(f"Telefone: {usuarioEscolhido["telefone"]}")
    print("\nEndereços:")
    for endereco in usuarioEscolhido["lista_endereco"]:
        print(f"Cep: {endereco["cep"]}")
        print(f"Rua/Avenida: {endereco["rua_avenida"]}")
        print(f"Número: {endereco["numero"]}")
        print(f"Bairro: {endereco["bairro"]}")
        print(f"Cidade: {endereco["cidade"]}")
        print(f"Estado: {endereco["estado"]}")
        print("\n---------------------------------------\n")

def atualizarUsuario():
    usuarioEscolhido = consultaUsuario()
    novoNome = str(input("Nome: "))
    novoCpf = str(input("CPF: "))
    novoEmail = str(input("Email: "))
    novaSenha = str(input("Senha: "))
    novoTelefone = str(input("Número telefone: "))
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
    usuarioEscolhido = consultaUsuario()
    minhaColecao.delete_one(usuarioEscolhido)
    print(f'\nUsuário {usuarioEscolhido["nome"]} foi deletado com sucesso!\n')

def criarEndereco():
    usuarioEscolhido = consultaUsuario()
    cep = str(input("CEP: "))
    ruaAvenida = str(input("Nome da rua ou avenida: "))
    numeroEndereco = input(input("Número endereço: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    estado = str(input("Estado(Sigla): "))
    enderecoObjeto = {
        "cep": cep,
        "rua_avenida": ruaAvenida,
        "numero": numeroEndereco,
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
    while True:
        email = str(input("Email do usuário: "))
        usuarioEscolhido = minhaColecao.find_one({"email": email})
        if usuarioEscolhido == None:
            print("Nenhum usuário encontrado")
            email = None
        else:
            break
    return usuarioEscolhido

def vinculaCompraUsuario(listaProduto, data_entrega, valorCompra):
    usuarioEscolhido = consultaUsuario()
    compra = {
        "lista_produto": listaProduto,
        "data_entrega": data_entrega,
        "valor_total_compra": valorCompra
    }
    atualizacao = {
        "$push": {
            "lista_compra": compra
        }
    }   
    minhaColecao.update_one(usuarioEscolhido, atualizacao)
    return [usuarioEscolhido["nome"], usuarioEscolhido["email"]]

def listarComprasUsuario():
    usuarioEscolhido = consultaUsuario()
    for compra in usuarioEscolhido["lista_compra"]:
        print("\nProdutos")
        for produto in compra["lista_produto"]:
            print(f"Descrição: {produto["descricao"]}")
            print(f"Quantidade: {produto["quantidade"]}")
            print(f"Preço Total: R${produto["valor_total_compra"]}")
            print("\n---------------------------------------\n")


def criarFavorito():
    usuarioEscolhido = consultaUsuario()
    produtoEscolhido = produto.consultaProduto()
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
    print("\nProdutos")
    for favorito in usuarioEscolhido["lista_favorito"]:
        print(f"Descrição: {favorito["descricao"]}")
        print(f"Preço: R${favorito["preco"]}")
        print("\n---------------------------------------\n")

def deletarFavorito():     
    usuarioEscolhido = consultaUsuario()
    produtoEscolhido = produto.consultaProduto()
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
    for usuario in minhaColecao.find():
        if len(usuario["lista_favorito"]) != 0:
            if produtoObjeto in usuario["lista_favorito"]:
                minhaColecao.update_one(usuario, atualizacaoListaFavorito)
