from servicos.usuario import *
from servicos.vendedor import *
from servicos.produto import *
from servicos.compra import *


key = 0
sub = 0
while key != 'S':
    print("\n1 - Usuário")
    print("2 - Vendedor")
    print("3 - Produto")
    print("4 - Compra")
    key = input("\nDigite a opção desejada?(S para sair) ")

    if key == '1':
        print("\n-----------------")
        print("\nMenu do Usuário\n")
        print("1 - Criar Usuário")
        print("2 - Listar Usuário")
        print("3 - Atualizar Usuário")
        print("4 - Apagar Usuário")
        print("5 - Adicionar novo Endereço")
        print("6 - Listar Compras")
        print("7 - Favoritar Produto")
        print("8 - Listar Favoritos")
        print("9 - Desfavoritar Produto")
        sub = input("\nDigite a opção desejada? (V para voltar) ")

        if sub == "1":
            print("\n----INSERIR USUÁRIO----\n")
            criarUsuario()
            
        elif sub == "2":
            print("\n----LISTAR USUÁRIO----\n")
            listarUsuario()
        
        elif sub == "3":
            print("\n----ATUALIZAR USUÁRIO----\n")
            atualizarUsuario()

        elif sub == "4":
            print("\n----DELETAR USUÁRIO----")
            deletarUsuario()
        
        elif sub == "5":
            print("\n----ADICIONAR ENDEREÇO----\n")
            criarEndereco()
        
        elif sub == "6":
            print("\n----LISTAR COMPRAS----\n")
            listarComprasUsuario()

        elif sub == "7":
            print("\n----FAVORITAR PRODUTO----\n")
            criarFavorito()

        elif sub == "8":
            print("\n----LISTAR FAVORITOS----\n")
            listarFavorito()

        elif sub == "9":
            print("\n----DESFAVORITAR PRODUTO----\n")
            deletarFavorito()
    
    elif key == '2':
        print("\n-----------------")
        print("\nMenu do Vendedor\n")
        print("1 - Criar Vendedor")
        print("2 - Listar Vendedor")
        print("3 - Atualizar Vendedor")
        print("4 - Apagar Vendedor")
        sub = input("\nDigite a opção desejada? (V para voltar) ")

        if sub == "1":
            print("\n----INSERIR VENDEDOR----\n")
            criarVendedor()
            
        elif sub == "2":
            print("\n----LISTAR VENDEDOR----\n")
            listarVendedor()
        
        elif sub == "3":
            print("\n----ATUALIZAR VENDEDOR----\n")
            atualizarVendedor()

        elif sub == "4":
            print("\n----DELETAR VENDEDOR----")
            deletarVendedor()

    elif key == '3':
        print("\n-----------------")
        print("\nMenu do Produto\n") 
        print("1 - Criar Produto")
        print("2 - Listar Produto")
        print("3 - Atualizar Produto")
        print("4 - Apagar Produto")
        sub = input("\nDigite a opção desejada? (V para voltar) ")

        if sub == "1":
            print("\n----INSERIR PRODUTO----\n")
            criarProduto()
            
        elif sub == "2":
            print("\n----LISTAR PRODUTO----\n")
            listarProduto()
        
        elif sub == "3":
            print("\n----ATUALIZAR PRODUTO----\n")
            atualizarProduto()

        elif sub == "4":
            print("\n----DELETAR PRODUTO----\n")
            deletarProduto()
        
    elif key == '4':
        print("\n-----------------")
        print("\nMenu da Compra\n")
        print("1 - Comprar um Produto")
        print("2 - Listar Compras")
        sub = input("\nDigite a opção desejada? (V para voltar) ")

        if sub == "1":
            print("\n----COMPRAR UM PRODUTO----\n")
            criarCompra()
        
        if sub == "2":
            print("\n----LISTAR COMPRAS----\n")
            listarCompras()
    elif key == "S":
        break