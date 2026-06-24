from analyzer import analisar_equipamentos
from datetime import datetime

prioridade = {
    'OK' : 1,
    'ATENCAO' : 2,
    'CRITICO' : 3
}

def exportar_relatorio(equipamentos):
    agora = datetime.now()
    equipamentos_ordenados = sorted(equipamentos, key=lambda d: prioridade[d["status"]])
    # print(equipamentos_ordenados)

    with open('relatorio.txt', 'w', encoding='utf-8') as f:
        titulo = f"RELATÓRIO DE OBSOLESCÊNCIA - {agora.strftime('%d/%m/%Y %H:%M')}"
        barra = '=' * len(titulo)
        f.write(titulo + '\n')
        f.write(barra + '\n')
        f.write("\n")
    
        for equipamento in equipamentos_ordenados:
            f.write(f"{equipamento['status']:<10} | {equipamento['nome']:<30} | Percentual de vida útil atingido: {equipamento['vida_percentual'] * 100:.0f}%\n")
