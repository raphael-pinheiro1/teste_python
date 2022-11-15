
# FAZENDO UMA COPIA DO ARQUIVO

# with open(file='./banco-texto.txt', mode='r', encoding='utf8') as leitura:
#   with open(file='./banco-csv.csv', mode='w', encoding='utf8') as escrita:
#     linha = leitura.readline()
#     while linha:
#       escrita.write(linha)
#       linha = leitura.readline()



#CRIANDO UM ARQUIVO COM UMA FUNÇÃO

def escreve_arquivo_csv(nome: str, cabecalho: str, conteudos: list) -> bool:

  try: 

    with open(file=nome, mode='w', encoding='utf8') as fp:
      linha = cabecalho + '\n'
      fp.write(linha)
      for conteudo in conteudos:
        linha = str(conteudo) + '\n'
        fp.write(linha)

  except Exception as exc:
    
    print(exc)
    return False

  return True

nome = 'idades-funcao-erro.csv'
cabecalho = 'idade'
conteudos = ["Famoso, pica de meu", 33, 35, 30, 59, 35, 36, 39, 41, 43]
#conteudos = 10

