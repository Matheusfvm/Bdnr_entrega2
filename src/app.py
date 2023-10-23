import modelo

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
        print("6 - Favoritar Produto")
        print("7 - Listar Favoritos")
        print("8 - Desfavoritar Produto")
        sub = input("\nDigite a opção desejada? (V para voltar) ")

        if sub == "1":
            print("\n----INSERIR USUÁRIO----\n")
            modelo.criarUsuario()
            
        elif sub == "2":
            print("\n----LISTAR USUÁRIO----\n")
            modelo.listarUsuario()
        
        elif sub == "3":
            print("\n----ATUALIZAR USUÁRIO----\n")
            modelo.atualizarUsuario()

        elif sub == "4":
            print("\n----DELETAR USUÁRIO----")
            modelo.deletarUsuario()
        
        elif sub == "5":
            print("\n----ADICIONAR ENDEREÇO----\n")
            modelo.criarEndereco()

        elif sub == "6":
            print("\n----FAVORITAR PRODUTO----\n")
            modelo.criarFavorito()

        elif sub == "7":
            print("\n----LISTAR FAVORITOS----\n")
            modelo.listarFavorito()

        elif sub == "8":
            print("\n----DESFAVORITAR PRODUTO----\n")
            modelo.deletarFavorito()
    
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
            modelo.criarVendedor()
            
        elif sub == "2":
            print("\n----LISTAR VENDEDOR----\n")
            modelo.listarVendedor()
        
        elif sub == "3":
            print("\n----ATUALIZAR VENDEDOR----\n")
            modelo.atualizarVendedor()

        elif sub == "4":
            print("\n----DELETAR VENDEDOR----")
            modelo.deletarVendedor()

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
            modelo.criarProduto()
            
        elif sub == "2":
            print("\n----LISTAR PRODUTO----\n")
            modelo.listarProduto()
        
        elif sub == "3":
            print("\n----ATUALIZAR PRODUTO----\n")
            modelo.atualizarProduto()

        elif sub == "4":
            print("\n----DELETAR PRODUTO----\n")
            modelo.deletarProduto()
        
    elif key == '4':
        print("\n-----------------")
        print("\nMenu da Compra\n")
        print("1 - Comprar um Produto")
        print("2 - Listar Compras")
        sub = input("\nDigite a opção desejada? (V para voltar) ")

        if sub == "1":
            print("\n----COMPRAR UM PRODUTO----\n")
            modelo.criarCompra()
        
        if sub == "2":
            print("\n----LISTAR COMPRAS----\n")
            modelo.listarCompra()
    elif key == "S":
        break