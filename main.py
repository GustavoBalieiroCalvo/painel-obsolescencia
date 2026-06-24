from analyzer import analisar_equipamentos
from report import exportar_relatorio

def main():
    dados = analisar_equipamentos()
    exportar_relatorio(dados)


if __name__ == '__main__':
    main()