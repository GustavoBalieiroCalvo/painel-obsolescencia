import csv
import datetime

def analisar_equipamentos():
    data_hoje = datetime.date.today()

    with open('data/equipamentos.csv', mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = tuple(leitor)

    for equipamento in dados:
        if not equipamento['data_fabricacao']:
            continue
        diferenca = data_hoje - datetime.date.fromisoformat(equipamento['data_fabricacao'])
        idade_anos = diferenca.days / 365
        vida_util = int(equipamento['vida_util_anos'])
        vida_percentual = idade_anos / vida_util

        equipamento['vida_percentual'] = vida_percentual


        if vida_percentual < 0.75:
            print(f'{equipamento["nome"]:<30} | OK')
            equipamento['status'] = 'OK'
        elif 0.75 <= vida_percentual < 1:
            print(f'{equipamento["nome"]:<30} | ATENÇÃO')
            equipamento['status'] = 'ATENCAO'
        elif vida_percentual > 1:
            print(f'{equipamento["nome"]:<30} | CRÍTICO')
            equipamento['status'] = 'CRITICO'
    return dados
