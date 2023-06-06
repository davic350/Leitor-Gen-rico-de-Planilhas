def aplicar_funcao(dados, coluna, funcao):
    '''
    Função auxiliar da Função 'data_grouper' e realiza operações com os índices numéricos agrupados.
    - par. 'dados': lista com o índice numérico agrupado que passará por alguma operação.
    - par. 'coluna': índice numérico agrupado.
    - par. 'funcao': string que indica a operação a ser realizada.
    - return: o resultado da operação escolhida com o índice numérico agrupado.
    '''
    if funcao == 'media':
        return media(dados, coluna)
    elif funcao == 'somatorio':
        return somatorio(dados, coluna)
    elif funcao == 'maior':
        return maior(dados, coluna)
    elif funcao == 'menor':
        return menor(dados, coluna)
    elif funcao == 'desvio':
        return desvio_padrao(dados, coluna)
 

def somatorio(dados, coluna):
    '''
    Função auxiliar da função 'aplicar_funções' que soma todos os valores de determinado índice numérico.
    - par. 'dados': lista com o índice numérico agrupado que terá o somatório realizado.
    - par. 'coluna': índice numérico agrupado.
    - return: a soma de todos os valores do índice desejado.
    '''
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma

def media(dados, coluna):
    '''
    Função auxiliar da função 'aplicar_funções' que tira a média dos valores de determinado índice numérico, 
    pela quantidade de ocorrências da lista do parâmetro 'dados'.
    - par. 'dados': lista com o índice numérico agrupado que terá sua média calculada.
    - par. 'coluna': índice numérico agrupado.
    - return: a média dos valores de determinado índice numérico, pela quantidade de ocorrências 
    da lista do parâmetro 'dados'.
    '''
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma / len(dados)

def maior(dados, coluna):
    '''
    Função auxiliar da função 'aplicar_funções' para calcular a maior valor de um determinado índice.
    - par. 'dados': lista com o índice numérico agrupado que terá seu maior valor retornado.
    - par. 'coluna': índice numérico agrupado.
    - return: o maior valor dentre os valores do índice escolhido.
    '''
    maior = 0
    
    for linha in dados:
        if linha[coluna] > maior:
            maior = linha[coluna]
    return maior

def menor(dados, coluna):
    '''
    Função auxiliar da função 'aplicar_funções' para calcular o menor valor de um determinado índice.
    - par. 'dados': lista com o índice numérico agrupado que terá seu menor valor retornado.
    - par. 'coluna': índice numérico agrupado.
    - return: o menor valor dentre os valores do índice escolhido.
    '''
    menor_indice = None
    for linha in dados:
        if menor_indice is None or linha[coluna] < menor_indice:
            menor_indice = linha[coluna]
    return menor_indice

def desvio_padrao(dados, coluna):
    '''
    Função para calcular o desvio padrão de uma amostra determinada por um índice.
    - par. 'dados': lista com o índice numérico agrupado que terá seu desvio padrão calculado.
    - par. 'coluna': índice numérico agrupado.
    - return: o desvio padrão de uma amostra determinada por um índice escolhido.
    '''

    from math import sqrt
    desvios = d = dp = 0
    m = media(dados, coluna)

    for linha in dados:
        d = (linha[coluna] - m) ** 2
        desvios += d
    dp = desvios / len(dados)
    return sqrt(dp)