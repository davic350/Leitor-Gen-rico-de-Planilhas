from operacoes import aplicar_funcao

def line_localizer(dados, linha = None, inicio = None , fim = None):
    """
    Função que filtra as linhas que o usuário deseja acessar por valor exato da linha ou por um intervalo.
    - par. 'dados': lista contendo os dados que serão filtrados por linha.
    - par. 'linha': valor exato da linha a ser acessada na lista.
    - par. 'inicio': valor exato da linha inicial do intervalo de linhas a ser acessado.
    - par. 'fim': valor exato da linha final do intervalo de linhas a ser acessado.
    - return: lista constando apenas a(s) linha(s) que o usuário deseja acessar.
    """
    quantidade_registros = len(dados)
    if linha != 0 and linha < quantidade_registros:
        return dados[linha]
    elif linha == 0 and inicio != 0 and fim != 0:
        for registros in dados:
            return dados[inicio:fim]
    else:
        print('Índice superior à quantidade de registros.')
        return {}
    
def tester(valor_teste, operacao, valor_comparado):
    """
    Função que auxilia a Função 'Filter' na comparação de índices a serem filtrados e armazenados em uma
    nova lista.
    - par. 'valor_teste': valor que consta inicialmente disposto na lista.
    - par. 'operação': string que indica o tipo de comparação que será realizada seguindo as nomenclaturas 
    utilizadas em Python.
    - par. 'valor_comparado': valor a ser comparado ao parâmetro 'valor_teste'.
    - return: operação correspondente ao que usuário especificou no parâmetro 'operação' ou resultado de
    teste 'False', caso o usuário tenha digitado algo diferente da relação de comparações.
    """
    if operacao == '==':
        return valor_teste == valor_comparado
    elif operacao == '>':
        return valor_teste > valor_comparado
    elif operacao == '<':
        return valor_teste < valor_comparado
    elif operacao == '>=':
        return valor_teste >= valor_comparado
    elif operacao == '<=':
        return valor_teste <= valor_comparado
    elif operacao == '!=':
        return valor_teste != valor_comparado 
    return False

def filter(dados, coluna, valor, operacao):
    """
    Função que filtra uma lista a partir de um ou mais índices.
    - par. 'dados': lista que terá os dados filtrados por um  índice.
    - par. 'coluna': índice ou lista de índices que serão armazenados na nova lista.
    - par. 'valor': valor ou lista de valores dos índices que serão armazenados na nova lista.
    - par. 'operacao': string ou lista de strings que indicam o tipo de comparação que será realizada seguindo
    as nomenclaturas utilizadas em Python.
    - return: lista constando apenas o(s) índice(s) desejado(s).
    """
    dados_filtrados = []

    for linha in dados:
        teste = True
        for c, v, o in zip(coluna, valor, operacao):
            if not tester(linha[c], o, v):
                teste = False
        if teste == True:
            dados_filtrados.append(linha)
    return dados_filtrados
   
def projector(dados, colunas):
    """
    Função que projeta em uma nova lista, apenas os índices desejados pelo usuário.
    - par. 'dados': lista que terá os dados projetados.
    - par. 'colunas': índice ou lista de índices que serão projetados.
    - return: lista constando apenas com o(s) índice(s) desejados.
    """
    dados_projetados = []
    for linha in dados:
        linha_projetada = {}
        for campo, valor in linha.items():
            if campo in colunas:
                linha_projetada[campo] = valor
        dados_projetados.append(linha_projetada)
    return dados_projetados

def general_data_updater(dados, colunas, dado_antigo, dado_novo):
    """
    Função que atualiza as informações que constam em determinado índice, apagando a informação antiga e 
    dispondo uma nova.
    - par. 'dados': lista que terá os dados modificados.
    - par. 'colunas': índice que terá seus valores atualizados.
    - par. 'dado_antigo': valor do índice escolhido que será substituído.
    - par. 'dado_novo': valor que substituirá o dado apagado.
    - return: lista com os valores atualizados/corrigidos do índice desejado.
    """
    for linha in dados:
        if linha[colunas] == dado_antigo:
            linha[colunas] = dado_novo
    return dados

def single_data_updater(dados, linha, coluna, dado_novo):
    """
    Função que atualiza a informação que esteja em uma célula de uma linha específica.
    - par. 'dados': lista que terá o dado modificado.
    - par. 'linha': valor exato da linha em que consta a célula que terá seu dado atualizado.
    - par. 'coluna': valor do índice escolhido que será substituído.
    - par. 'dado_novo': valor que substituirá o dado apagado.
    - return: lista com o valor atualizado/corrigido do índice, na linha desejada.
    """
    linha_buscada = line_localizer(dados, linha)
    linha_buscada[coluna] = dado_novo
    return dados

def data_grouper(dados, coluna=None, coluna2=None, funcao=None):
    """
    Função que agrupa índices titulares (strings) e/ou valores numéricos aplicando neles um tipo 
    de operação.
    - par. 'dados': lista que terá os índices agrupados.
    - par. 'coluna': índice não numérico que será agrupado.
    - par. 'coluna2': índice numérico que será operacionado de acordo com a função desejada.
    - par. 'funcao': operação o qual será submetido o índice numérico agrupado.
    - return: dicionário(s) com o índice e/ou o valor numérico agrupado.
    """
    dados_agrupados = {}

    for linha in dados:
        valor_celula = linha[coluna]
        if dados_agrupados.get(linha[coluna]) is None:
            dados_agrupados[valor_celula] = []
        dados_agrupados[valor_celula].append(linha) 

    for chave, lista in dados_agrupados.items():
         dados_agrupados[chave] = aplicar_funcao(lista, coluna2, funcao)
    
    return dados_agrupados
