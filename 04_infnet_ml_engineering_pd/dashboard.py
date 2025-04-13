import pandas as pd
from pathlib import Path
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Dashboard de Machine Learning 🧠",
    layout="wide"
)

# Título
st.title("Bem-vindo ao Dashboard de Machine Learning de lançamentos do Kobe Bryant! 🐍")

# Descrição
st.markdown("""
Este dashboard foi criado para monitorar e visualizar as previsões realizadas pelos modelos de Machine Learning. Será 
que nosso mamba negra acertou o arremesso? 🏀🗑️
""")

# Função para carregar dados de produção
@st.cache_data
def load_data():
    # Obter o caminho base do arquivo atual
    base_dir = Path(__file__).resolve()
    file_path = base_dir.parent / "data" / "07_model_output" / "predictions_with_features.csv"
    
    # Verificar existência do arquivo e carregar os dados
    if file_path.exists():
        return pd.read_csv(file_path)
    
    else:
        st.error(f"Arquivo não encontrado: {file_path}")
        return None

# Função para plotar o gráfico de dispersão
def plot_predictions(data, distance_filter, period_filter, playoff_filter, minutes_filter):
    """
    Gera um gráfico de dispersão com as previsões do modelo e salva a imagem.

    Args:
        data (pd.DataFrame): Dados a serem plotados.
        distance_filter (tuple): Intervalo de distância filtrado.
    """
    # Filtrar os dados pela distância e pelo filtro de playoffs
    filtered_data = data[
                        data["shot_distance"].between(distance_filter[0], distance_filter[1]) &
                        data["minutes_remaining"].between(minutes_filter[0], minutes_filter[1])
                    ]

    # Adicionar filtragem pelo período do jogo
    if period_filter != "Todos":
        filtered_data = filtered_data[filtered_data["period"] == int(period_filter)]

    if playoff_filter == "Sim":
        filtered_data = filtered_data[filtered_data["playoffs"] == 1]

    elif playoff_filter == "Não":
        filtered_data = filtered_data[filtered_data["playoffs"] == 0]

    # Remover a coluna 'logistic_regression_hat' dos dados filtrados
    if "logistic_regression_hat" in filtered_data.columns:
        filtered_data = filtered_data.drop(columns=["logistic_regression_hat"])

    # Carregar a imagem da quadra de basquete
    module_dir = Path(__file__).resolve().parent
    image_path = module_dir / 'src' / 'infnet_04_ml_engineering_pd'/ 'pipelines' / 'trainer' / 'assets' / 'basket_court4.png'

    # Garantir que a imagem existe
    if not image_path.exists():
        st.error(f"Imagem da quadra não encontrada em: {image_path}")
        return

    img = mpimg.imread(str(image_path))

    # Criar o gráfico de dispersão
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.imshow(img, extent=[-118.525, -118.015, 33.2, 34.23], aspect='auto')

    scatter = ax.scatter(
                            filtered_data["lon"],
                            filtered_data["lat"],
                            c=filtered_data["decision_tree_hat"].map({True: 'green', False: 'red'}),
                            alpha=0.6,
                            edgecolors="k"
                        )
    
    # Travar os limites do gráfico
    ax.set_xlim(-118.525, -118.015)  # Limites do eixo X
    ax.set_ylim(33.2, 34.23)         # Limites do eixo Y

    ax.set_title("Distribuição dos Arremessos")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle="--", alpha=0.5)
    
    # Exibir o gráfico na tela
    st.pyplot(fig)

# Carregar os dados
data = load_data()

# Seção do Dashboard
if data is not None:
    st.write("Visualize as previsões geradas pelo modelo de Machine Learning de Árvore de Decisão. 🌲")

    # Filtro para distância de arremesso
    st.sidebar.header("Configuração do Filtro")
    distance_filter = st.sidebar.slider(
                                        "Filtrar pela distância do arremesso:",
                                        min_value=float(data["shot_distance"].min()),
                                        max_value=float(data["shot_distance"].max()),
                                        value=(float(data["shot_distance"].min()), 
                                               float(data["shot_distance"].max()))
                                        )

    # Filtro para minutos restantes
    minutes_filter = st.sidebar.slider(
                                        "Filtrar por minutos restantes:",
                                        min_value=int(data["minutes_remaining"].min()),
                                        max_value=int(data["minutes_remaining"].max()),
                                        value=(int(data["minutes_remaining"].min()), 
                                                int(data["minutes_remaining"].max()))
                                        )

    # Filtro para período de jogo
    period_filter = st.sidebar.selectbox(
                                        "Período do jogo:",
                                        options=["Todos"] + list(map(str, sorted(data["period"].unique())))
                                        )

    # Filtro para "É Playoff?"
    playoff_filter = st.sidebar.selectbox(
                                        "É playoff?",
                                        options=["Todos", "Sim", "Não"]
                                        )
    
    # Filtrar os dados com base no slider e no filtro de playoffs
    filtered_data = data[
                        data["shot_distance"].between(distance_filter[0], distance_filter[1]) &
                        data["minutes_remaining"].between(minutes_filter[0], minutes_filter[1])
                        ]

    # Adicionar filtragem pelo período do jogo
    if period_filter != "Todos":
        filtered_data = filtered_data[filtered_data["period"] == int(period_filter)]

    if playoff_filter == "Sim":
        filtered_data = filtered_data[filtered_data["playoffs"] == True]
    elif playoff_filter == "Não":
        filtered_data = filtered_data[filtered_data["playoffs"] == False]

    # Remover a coluna 'logistic_regression_hat' antes de exibir a tabela filtrada
    if "logistic_regression_hat" in filtered_data.columns:
        filtered_data = filtered_data.drop(columns=["logistic_regression_hat"])

    # Exibir mensagem sobre os resultados
    if filtered_data["decision_tree_hat"].all():
        st.sidebar.success("Kobe acertou em cheio! 🏀🗑️")
    elif not filtered_data["decision_tree_hat"].any():
        st.sidebar.error("Kobe erra a cesta! ❌")
    else:
        success_rate = filtered_data["decision_tree_hat"].mean() * 100
        st.sidebar.info(f"Há {success_rate:.2f}% de chance do Kobe acertar, é hora de torcer! 🥁")

    # Exibição do filtro
    st.write("Amostra dos filtros escolhidos:")
    st.write(filtered_data.head())

    # Atualizar automaticamente o gráfico com a quadra
    st.header("Gráfico com a Quadra de Basquete")
    plot_predictions(data, distance_filter, period_filter, playoff_filter, minutes_filter)


