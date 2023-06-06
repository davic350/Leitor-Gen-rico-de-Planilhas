def data_converter(dados, tipo):
    """
    Conversor de dados de string para o tipo de determinado de cada dado.
    - par. 'dados': lista contendo os dados que serão convertidos.
    - par. 'tipo': lista com os tipos correspondentes de dados, elencados respectivamente às posições
    deles na lista
    - return: dado convertido ao seu tipo correspondente.
    """
    dado_convertido = dados
    if tipo == int:
        dado_convertido = int(dados)
    elif tipo == float:
        dado_convertido = float(dados)
    elif tipo == bool:
        dado_convertido = False
        if dados == 'TRUE':
            dado_convertido = True
    return dado_convertido


def file_loader(nome_aquivo, separador, tipos):
    """
    Função de abrir arquivos de tabelas/planilhas e converter os dados aos seus tipos correspondentes.
    - par. 'nome_arquivo': nome exato do arquivo que deseja abrir.
    - par. 'separador': caractere que irá separar um dado do outro dentro da lista que será criada.
    - par. 'tipos': lista com os tipos correspondentes de dados, elencados respectivamente às posições
    deles na lista
    - return: lista de dicionários com os dados convertidos aos seus tipos correspondentes.
    """
    lista = []
    file = open(nome_aquivo, 'r')
    linhas = file.readlines()

    cabecalho = linhas[0].replace('\n', '').split(separador)

    #percorre as linhas do arquivo
    for linha in linhas[1:]:
        dados = linha.upper().replace('\n', '').split(separador)
        alunos = {}

        #percorre as colunas de cada linha
        for coluna, tipo in enumerate(tipos):
            campo = cabecalho[coluna].upper()

            alunos[campo] = data_converter(dados[coluna], tipo)

        lista.append(alunos)
    return lista

def file_saver(nome_arquivo, separador, dados):
    """
    Função de armanezar listas de dicionários em arquivos de tabelas/planilhas.
    - par. 'nome_arquivo': nome exato do arquivo que deseja salvar.
    - par. 'separador': caractere que irá separar um dado do outro dentro da lista que será gerada 
    no arquivo final.
    - par. 'dados': lista que deseja armazenar no arquivo final.
    - return: sem retorno.
    """
    file = open(nome_arquivo, 'w')
    cabecalho_str = ''
    cabecalho = list(dados[0].keys())
    #criar um cabeçalho a partir das chaves contidas nos dicionários na lista do parâmetro 'dados'.
    for coluna in cabecalho:
        cabecalho_str += coluna 
        if coluna != cabecalho[-1]:
            cabecalho_str += separador
    cabecalho_str += '\n'

    file.write(cabecalho_str)
    #criar o corpo da lista com os valores contidos nos dicionários na lista do parâmetro 'dados'.
    for i , linha in enumerate(dados):
        linha_str = ''
        for coluna, valor in linha.items():
            linha_str += str(valor)
            if coluna != cabecalho[-1]:
                linha_str += separador
        if i < len(dados) - 1:        
            linha_str += '\n'
        file.write(linha_str)

    file.close