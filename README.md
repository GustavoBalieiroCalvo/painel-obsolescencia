# Painel de Obsolescência Industrial

Script Python que lê um CSV de equipamentos industriais, calcula o percentual de vida útil consumida de cada um e classifica por nível de risco. Exporta um relatório formatado em txt pronto pra uso.

Projeto desenvolvido como parte de estudos em sistemas de manufatura — a vaga que motivou esse projeto cita literalmente "atualizar plano de obsolescência" nas responsabilidades.

---

## O que ele faz

Equipamentos industriais têm vida útil estimada. Saber quais estão perto do limite — ou já passaram dele — é essencial pra planejar manutenção e evitar paradas não programadas.

O sistema:
- Lê o dataset de equipamentos em CSV
- Calcula a idade atual de cada máquina
- Classifica por risco: OK, ATENÇÃO ou CRÍTICO
- Exporta um relatório ordenado por prioridade

---

## Critério de classificação

| Status | Condição |
|---|---|
| OK | menos de 75% da vida útil consumida |
| ATENÇÃO | entre 75% e 100% |
| CRÍTICO | acima de 100% — passou da vida útil estimada |

---

## Estrutura

```
painel-obsolescencia/
├── data/
│   └── equipamentos.csv   # dataset de entrada
├── analyzer.py            # lê o CSV e classifica os equipamentos
├── report.py              # exporta o relatório em txt
├── main.py                # ponto de entrada
└── README.md
```

---

## Como rodar

Só Python 3.8+, sem dependências externas.

```bash
git clone https://github.com/seu-usuario/painel-obsolescencia.git
cd painel-obsolescencia
python main.py
```

O arquivo `relatorio.txt` é gerado automaticamente na raiz do projeto.

---


## Autor

Gustavo Calvo — estudante de Engenharia da Computação na FESA e Inteligência Artificial na Univesp.
