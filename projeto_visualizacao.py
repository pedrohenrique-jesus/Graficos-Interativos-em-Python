import pandas as pd
from dash import dash, html, dcc
import plotly.express as px

df = pd.read_csv('ecommerce_estatistica.csv')

def cria_graficos(df):
    # Gráfico de Histograma - Distribuição de Notas

    fig1 = px.histogram(
        df,
        x='Nota',
        nbins=5,  # número de faixas (intervalos)
        labels={'Nota': 'Notas dos Produtos', 'count': 'Frequência'},
        title='Distribuição de Notas',
        color_discrete_sequence=['skyblue']
    )
    fig1.update_traces(marker_line_color='black', marker_line_width=1, opacity=0.7)
    fig1.update_xaxes(tickvals=[1, 2, 3, 4, 5])

    # Gráfico de Dispersão - Relação Entre Notas e Descontos

    fig2 = px.scatter(
        df,
        x='Desconto',
        y='Nota',
        title='Dispersão: Desconto vs Nota dos Produtos',
        labels={'Desconto': 'Desconto (%)', 'Nota': 'Nota'},
        opacity=0.7,
        color_discrete_sequence=['mediumslateblue']
    )
    fig2.update_layout(
        xaxis_gridcolor='rgba(0,0,0,0.3)',
        yaxis_gridcolor='rgba(0,0,0,0.3)',
    )

    # Gráfico de Barras - Quantidade de Avaliações por gênero
    # Agrupando e criando DataFrame para Plotly
    avaliacoes = df.groupby('Gênero')['N_Avaliações'].sum().reset_index()

    fig3 = px.bar(
        avaliacoes,
        x='Gênero',
        y='N_Avaliações',
        title='Quantidade Total de Avaliações por Gênero',
        labels={'Gênero': 'Gênero', 'N_Avaliações': 'Total de Avaliações'},
        color_discrete_sequence=['steelblue']
    )

    fig3.update_traces(marker_line_color='black', marker_line_width=1)
    fig3.update_layout(
        xaxis_tickangle=45,
        yaxis_gridcolor='rgba(0,0,0,0.3)'
    )

    # Gráfico de pizza -Contagem de produtos por gênero
    # Agrupa gêneros com menos de 5% em "Outros"
    # preparativos:
    contagem_genero = df['Gênero'].value_counts(normalize=True)
    categorias_principais = contagem_genero[contagem_genero > 0.05].index
    df['Gênero_agrupado'] = df['Gênero'].apply(lambda x: x if x in categorias_principais else 'Outros')
    contagem_agrupada = df['Gênero_agrupado'].value_counts().reset_index()
    contagem_agrupada.columns = ['Gênero_agrupado', 'Quantidade']

    # gráfico com plotly:
    fig4 = px.pie(
        contagem_agrupada,
        names='Gênero_agrupado',
        values='Quantidade',
        title='Distribuição dos Produtos por Gênero',
        color_discrete_sequence=px.colors.qualitative.Pastel,  # parecida com Pastel1 do matplotlib
        hole=0  # pizza inteira, hole=0.3 vira gráfico de rosca
    )

    fig4.update_traces(textinfo='percent+label', pull=[0.05] * len(contagem_agrupada))  # mostra % + rótulos

    fig4.update_layout(
        showlegend=True,
        legend_title_text='Gênero',
        margin=dict(t=70, b=30, l=30, r=30)
    )

    # Gráfico de Densidade - Distribuição de Notas por Gênero
    fig5 = px.violin(
        df,
        x="Gênero",
        y="Nota",
        color="Gênero",
        box=False,  # não mostra o boxplot, apenas a distribuição
        points=False,  # não mostra os pontos individuais
        title="Densidade das Notas por Gênero",
        labels={"Nota": "Nota", "Gênero": "Gênero"}
    )
    fig5.update_traces(meanline_visible=True, opacity=0.6)
    fig5.update_layout(
        xaxis_title="Gênero",
        yaxis_title="Nota",
        legend_title_text="Gênero",
        yaxis_gridcolor='rgba(0,0,0,0.3)',
        plot_bgcolor='white'
    )

    # Gráfico de Regressão - Relação entre Desconto e Nota
    fig6 = px.scatter(
        df,
        x='Desconto',
        y='Nota',
        trendline="ols",  # Adiciona linha de regressão linear
        opacity=0.6,
        title='Regressão: Desconto vs Nota dos Produtos',
        labels={'Desconto': 'Desconto (%)', 'Nota': 'Nota'},
        color_discrete_sequence=['mediumslateblue']
    )
    # Personaliza a cor da linha de regressão (trendline)
    fig6.update_traces(marker=dict(opacity=0.6))  # Opacidade dos pontos

    # Deixa a linha sempre bem visível ajustando layout/traces!
    for d in fig6.data:
        if d.mode == 'lines':
            d.line.color = 'crimson'
            d.line.width = 2

    fig6.update_layout(
        xaxis_title='Desconto (%)',
        yaxis_title='Nota',
        yaxis_gridcolor='rgba(0,0,0,0.3)',
        xaxis_gridcolor='rgba(0,0,0,0.3)'
    )

    return fig1, fig2, fig3, fig4, fig5, fig6

def cria_app(df):
#cria App
    app = dash.Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)
    ])
    return app

# Executa App
if __name__ == '__main__':
    app = cria_app(df)
    app.run(debug=True, port=8050) #Default 8050