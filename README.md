# Análise de Dados de E-commerce

Análise de 295 anúncios de vestuário de um e-commerce para entender o que explica o desempenho dos produtos (preço, desconto, avaliações e marca) e gerar recomendações comerciais. Projeto de Python com Pandas, SciPy e visualizações, mais um dashboard interativo em Dash/Plotly.

## Objetivo
Responder a três perguntas de negócio:
1. Quanto a receita está concentrada em poucos produtos e marcas?
2. Existe uma faixa de preço que concentra as vendas?
3. Descontos e avaliações estão associados a mais vendas?

## Dados
- **Arquivo:** `ecommerce_estatistica.csv` (295 linhas, 24 colunas).
- **Variáveis principais:** preço, desconto, nota, nº de avaliações, marca, material, gênero e quantidade vendida (em faixas: `+100`, `+1000`, `+10mil`).
- **Fonte:** [indicar a origem do dataset]

## Tecnologias
Python, Pandas, NumPy, SciPy, Matplotlib, Seaborn, Dash e Plotly.

## Tratamento dos dados
- Remoção de 74 duplicatas (mesmo título, marca e preço): 295 para 221 produtos únicos.
- Padronização de categorias de gênero e temporada.
- `Qtd_Vendidos` tratada como **piso** de unidades. A **receita mínima estimada** (preço x piso de unidades) é, portanto, conservadora.

## Principais resultados
| Indicador | Resultado |
|---|---|
| Receita mínima estimada | R$ 52,7 milhões |
| Participação dos 10 maiores produtos | 71,0% |
| Participação dos 20% maiores produtos (45) | 91,9% |
| Participação das 3 maiores marcas (de 108) | 65,3% |
| Correlação desconto x unidades vendidas (Spearman) | 0,04 (sem relação) |
| Correlação nº de avaliações x unidades vendidas | 0,91 |

## Insights
- A receita é muito concentrada: 10 produtos geram 71% do total.
- Não há faixa de preço "ideal": a mediana de unidades é a mesma (100) em todas as faixas. A faixa mais cara concentra 67,8% da receita por reunir kits de alto valor.
- Desconto não explica vendas. A nota também não.
- Avaliações acompanham vendas, mas isso é mais consequência do que causa.

## Limitações
- A quantidade vendida é um piso por faixa, então a receita é mínima.
- A base é uma foto sem datas: não mede tendência nem causalidade.
- Amostra de vestuário com muitos kits: não representa o e-commerce inteiro.

## Estrutura
```
├── analise_ecommerce.ipynb     # análise completa
├── projeto_visualizacao.py     # dashboard interativo (Dash/Plotly)
├── ecommerce_estatistica.csv   # dados
├── tabelas_dashboard/          # tabelas agregadas para Looker Studio / Power BI
├── figs/                       # gráficos da análise
└── relatorio_ecommerce.pdf     # relatório
```

## Como executar
```bash
pip install -r requirements.txt
jupyter notebook analise_ecommerce.ipynb   # análise
python projeto_visualizacao.py             # dashboard em http://127.0.0.1:8050
```

## Dashboard
[link do dashboard, quando publicado]

## Autor
Pedro de Jesus | [LinkedIn](https://www.linkedin.com/in/pedro-henrique-correia-de-jesus/) | [GitHub](https://github.com/pedrohenrique-jesus)
