from arquivo import file_loader, file_saver
from processamento import line_localizer, filter, projector, general_data_updater, single_data_updater, data_grouper

lista = file_loader('alunos.csv', ',', [str, int, str, float, float, int, float, bool])

linha = line_localizer(lista, 1, 0, 0)
#print(linha)

linhas = line_localizer(lista,0,1,25)
#print(linhas)

filtro = filter(lista, ['MONITORIA'], [True], ['=='])
#print(filtro)

filtros = filter(lista, ['MONITORIA', 'NOTA_EXAME', 'FALTAS'], [True, 6, 15], ['==', '>', '<'])
#print(filtros)

dados_projetados = projector(lista, ['NOME', 'ESCOLA', 'MONITORIA'])
#print(dados_projetados)

dados_agrupados = data_grouper(lista, 'ESCOLA', 'NOTA_EXAME', 'desvio')
#print(dados_agrupados)

#file_saver('dadosagrupados.csv', ',', dados_projetados)