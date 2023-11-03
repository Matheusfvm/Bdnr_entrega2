import conexao
from datetime import datetime
import servicos.produto as produto
import servicos.vendedor as vendedor
import servicos.usuario as usuario


global minhaColecao
db = conexao.conectar()
minhaColecao = db.Compra


def criarCompra():
    dataCompra = datetime.now()
    dataCompraFormatada = dataCompra.strftime("%d/%m/%Y %H:%M")
    listaProduto = []        
    produtoObjeto = {}
    valortotalCompra = 0
    key = "S"
    while key == "S":        
        produtoEscolhido = produto.consultaProduto()
        if produtoEscolhido["quantidade"] != 0:
            quantidadeProdutoCompra = int(input(f"Unidades de produtos compradas(max = {produtoEscolhido["quantidade"]}): "))        
            quantidadeProdutoCompraFinal = produto.diminuirQuantidadeProduto(quantidadeProdutoCompra, produtoEscolhido)
            vendedor.alterarQuantidadeProdutoVendedor(quantidadeProdutoCompraFinal[1], produtoEscolhido)
            produtoObjeto = {
                "descricao": produtoEscolhido["descricao"],
                "preco": produtoEscolhido["preco"],
                "quantidade_produto_compra": quantidadeProdutoCompraFinal[0],
                "vendedor": produtoEscolhido["vendedor"] 
            }
            listaProduto.append(produtoObjeto)    
            valortotalCompra += produtoEscolhido["preco"] * quantidadeProdutoCompraFinal[0]    
        else:
            print(f"Produto {produtoEscolhido["descricao"]} está em falta!")
        key = str(input("Deseja comprar um outro produto(S/N)? "))
    dataCompraEntrega = str(input("Data da entrega(dd/mm/AAAA): "))
    listaNomeEmailUsuario = usuario.vinculaCompraUsuario(listaProduto, dataCompraEntrega, valortotalCompra)  
    usuarioObjeto = {
        "nome": listaNomeEmailUsuario[0],
        "email": listaNomeEmailUsuario[1]
    }
    compra = {
        "usuario": usuarioObjeto,
        "lista_produto": listaProduto,
        "data_compra": dataCompraFormatada,
        "data_entrega_compra": dataCompraEntrega,
        "valor_total_compra": valortotalCompra
    }
    minhaColecao.insert_one(compra)
    print(f'\nCompra realizada com sucesso!\n')
        

def listarCompras():    
    listaCompra = []
    for compra in minhaColecao.find():
      listaCompra.append(compra)
    indiceCompra = 1
    for compra in listaCompra:
        print(f"\n{indiceCompra}º Compra\n")
        print(f"Usuário email: {compra["usuario"]["email"]}")
        print(f"Data e hora da compra: {compra["data_compra"]}")
        print(f"Data entrega: {compra["data_entrega_compra"]}\n")
        print(f"Valor total da compra: R${compra["valor_total_compra"]:.2f}")
        print("\nProdutos\n")
        for produto in compra["lista_produto"]:
            print(f"Descrição: {produto["descricao"]}")
            print(f"Preço: {produto["preco"]:.2f}")
            print(f"Quantidade: {produto["quantidade_produto_compra"]}")
            print("\n---------------------------------------\n")
            
            