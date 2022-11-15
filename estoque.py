produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
print(produtos[0])
estoque = [800, 222, 555, 366, 365]
produto = input('Insira o produto em letras minuscula: ')

i = produtos.index(produto)
qtd_estoque = estoque[i]
 
if produto in produtos:
    i = produtos.index(produto)
    qtd_estoque = estoque[i]
    print(f'{produtos[i]} Quantidade em estoque: {qtd_estoque}')
else: 
    print(f'{produto} não existe no estoque')