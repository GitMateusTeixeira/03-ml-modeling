import pickle
import os
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import mlflow
from pathlib import Path
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss, precision_score, recall_score, f1_score

def trainer(X_train: pd.DataFrame, y_train: pd.DataFrame, X_test: pd.DataFrame, y_test: pd.DataFrame) -> dict:
    """
    Treina os modelos Decision Tree e Logistic Regression usando dados de desenvolvimento,
    avalia os resultados e registra parâmetros, métricas e artefatos no MLflow.

    Args:
        X_train: DataFrame com as features de treinamento.
        y_train: DataFrame com as labels de treinamento.
        X_test: DataFrame com as features de teste.
        y_test: DataFrame com as labels de teste.

    Returns:
        dict: Caminhos dos modelos e arquivo de resultados.
    """

    with mlflow.start_run(nested=True):

        # Diretório para salvar os modelos e resultados
        BASE_DIR = Path(__file__).resolve().parents[4]
        RESULTS_PATH = BASE_DIR / 'data' / '06_models'
        RESULTS_PATH.mkdir(parents=True, exist_ok=True)

        DT_MODEL_PATH = RESULTS_PATH / 'decision_tree_model.pkl'
        LR_MODEL_PATH = RESULTS_PATH / 'logistic_regression_model.pkl'
        
        print("Trainer parte 01 - Diretórios e caminhos configurados corretamente.")

        # Criar diretório para os gráficos
        REPORTING_PATH = BASE_DIR / 'data' / '08_reporting'
        REPORTING_PATH.mkdir(parents=True, exist_ok=True)
        RESULTS_FILE_PATH = REPORTING_PATH / 'results.csv'

        SCATTER_PLOT_LR = REPORTING_PATH / 'lr_predictions_scatter.png'
        SCATTER_PLOT_DT = REPORTING_PATH / 'dt_predictions_scatter.png'

        # Inicializar os modelos
        dt_model = DecisionTreeClassifier(
                                            random_state=17
                                            )
        
        lr_model = LogisticRegression(
                                        random_state=17, 
                                        max_iter=1000
                                        )

        print("Trainer parte 02 - Modelos inicializados.")

        # Treinar os modelos
        dt_model.fit(X_train, y_train)
        lr_model.fit(X_train, y_train)

        print("Trainer parte 03 - Modelos treinados com sucesso.")

        # Fazer previsões
        dt_predictions = dt_model.predict(X_test)
        lr_predictions = lr_model.predict(X_test)

        print("Trainer parte 04 - Previsões realizadas nos dados de teste.")

        # Registrar métricas no MLflow
        mlflow.log_metric("dt_accuracy", accuracy_score(y_test, dt_predictions))
        mlflow.log_metric("lr_accuracy", accuracy_score(y_test, lr_predictions))
        mlflow.log_metric("dt_log_loss", log_loss(y_test, dt_model.predict_proba(X_test)))
        mlflow.log_metric("lr_log_loss", log_loss(y_test, lr_model.predict_proba(X_test)))
        mlflow.log_metric("dt_precision", precision_score(y_test, dt_predictions, zero_division=0))
        mlflow.log_metric("lr_precision", precision_score(y_test, lr_predictions, zero_division=0))
        mlflow.log_metric("dt_recall", recall_score(y_test, dt_predictions, zero_division=0))
        mlflow.log_metric("lr_recall", recall_score(y_test, lr_predictions, zero_division=0))
        mlflow.log_metric("dt_f1_score", f1_score(y_test, dt_predictions, zero_division=0))
        mlflow.log_metric("lr_f1_score", f1_score(y_test, lr_predictions, zero_division=0))

        print("Trainer parte 05 - Métricas registradas no MLflow.")

        # Salvar os modelos como arquivos .pkl
        with open(DT_MODEL_PATH, "wb") as dt_file:
            pickle.dump(dt_model, dt_file)
        print(f"Trainer parte 06 - Modelo Decision Tree salvo em {DT_MODEL_PATH}, tipo: {type(dt_model)}")

        with open(LR_MODEL_PATH, "wb") as lr_file:
            pickle.dump(lr_model, lr_file)
        print(f"Trainer parte 07 - Modelo Logistic Regression salvo em {LR_MODEL_PATH}, tipo: {type(lr_model)}")

        # Registrar os arquivos .pkl no MLflow como artefatos
        mlflow.log_artifact(str(DT_MODEL_PATH))
        mlflow.log_artifact(str(LR_MODEL_PATH))

        print("Trainer parte 10 - Modelos salvos registrados como artefatos no MLflow.")

    # Salvar os resultados em um arquivo CSV
    results = {
            "Model": ["Decision Tree", "Logistic Regression"],
            "Accuracy": [accuracy_score(y_test, dt_predictions), accuracy_score(y_test, lr_predictions)],
            "Log Loss": [log_loss(y_test, dt_model.predict_proba(X_test)), log_loss(y_test, lr_model.predict_proba(X_test))],
            "Precision": [precision_score(y_test, dt_predictions, zero_division=0), precision_score(y_test, lr_predictions, zero_division=0)],
            "Recall": [recall_score(y_test, dt_predictions, zero_division=0), recall_score(y_test, lr_predictions, zero_division=0)],
            "F1-Score": [f1_score(y_test, dt_predictions, zero_division=0), f1_score(y_test, lr_predictions, zero_division=0)],
            }

    results_df = pd.DataFrame(results)

    print(f"Trainer parte 08 - Resultados criados e salvos como DataFrame.")

    # Registrar o CSV como artefato no MLflow
    results_df.to_csv(RESULTS_FILE_PATH, index=False)
    mlflow.log_artifact(str(RESULTS_FILE_PATH))

    print("Trainer parte 09 - Artefato CSV registrado no MLflow.")

    # Gerar gráfico para Logistic Regression
    plot_predictions(X_test, lr_predictions, BASE_DIR, 'lr_dev')

    # Gerar gráfico para Decision Tree
    plot_predictions(X_test, dt_predictions, BASE_DIR, 'dt_dev')

    # Retornar objetos para o pipeline
    return {
        "decision_tree_model": str(DT_MODEL_PATH),
        "logistic_regression_model": str(LR_MODEL_PATH),
        "results_file": str(RESULTS_FILE_PATH),  # Retornando o DataFrame diretamente
    }


def inference(decision_tree_model: str, logistic_regression_model: str, x_features_prod: pd.DataFrame, y_features_prod: pd.DataFrame) -> pd.DataFrame:
    
    # Diretório para salvar as previsões
    BASE_DIR = Path(__file__).resolve().parents[4]
    OUTPUT_PATH = BASE_DIR / 'data' / '07_model_output'
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    # Caminho do arquivo CSV final
    PREDICTIONS_FILE_PATH = OUTPUT_PATH / 'predictions_with_features.csv'

    # Criar diretório para os gráficos
    REPORTING_PATH = BASE_DIR / 'data' / '08_reporting'
    REPORTING_PATH.mkdir(parents=True, exist_ok=True)
    
    # Caminhos dos gráficos
    SCATTER_PLOT_LR = REPORTING_PATH / 'lr_prod_predictions_scatter.png'
    SCATTER_PLOT_DT = REPORTING_PATH / 'dt_prod_predictions_scatter.png'
    
    # Caminho do arquivo de métricas
    METRICS_FILE_PATH = REPORTING_PATH / 'inferences_metrics.csv'

    print("Inferencia parte 01 - Iniciando inferência")

    # Carregar os modelos diretamente dos caminhos recebidos
    with open(decision_tree_model, "rb") as dt_file:
        dt_model = pickle.load(dt_file)
    print(f"Modelo Decision Tree carregado corretamente: {type(dt_model)}")

    with open(logistic_regression_model, "rb") as lr_file:
        lr_model = pickle.load(lr_file)
    print(f"Modelo Logistic Regression carregado corretamente: {type(lr_model)}")

    # Verificar se 'shot_made_flag' está presente no DataFrame
    if "shot_made_flag" not in y_features_prod.columns:
        raise KeyError("A coluna 'shot_made_flag' não foi encontrada no DataFrame y_features_prod")
    
    # Realizar previsões
    dt_predictions = dt_model.predict(x_features_prod)
    lr_predictions = lr_model.predict(x_features_prod)

    print("Inferencia parte 02 - Previsões realizadas com sucesso.")

    # Adicionar as previsões como novas colunas no DataFrame original
    x_features_prod['decision_tree_hat'] = dt_predictions
    x_features_prod['logistic_regression_hat'] = lr_predictions

    print("Inferencia parte 03 - Colunas de previsões adicionadas ao DataFrame.")

    # Salvar o DataFrame com previsões em um arquivo CSV
    x_features_prod.to_csv(PREDICTIONS_FILE_PATH, index=False)
    print(f"Arquivo de previsões salvo em: {PREDICTIONS_FILE_PATH}")

    mlflow.log_artifact(str(PREDICTIONS_FILE_PATH))
    
    print("Inferencia parte 04 - registrado com sucessso.")

    y_prod = y_features_prod["shot_made_flag"]

    # Remover as colunas extras antes de usar predict_proba
    x_features_prod_cleaned = x_features_prod.drop(columns=["decision_tree_hat", "logistic_regression_hat"], errors="ignore")

    # Salvar os resultados em um arquivo CSV
    results = {
            "Model": ["Decision Tree", "Logistic Regression"],
            "Accuracy": [accuracy_score(y_prod, dt_predictions), 
                         accuracy_score(y_prod, lr_predictions)],
            "Log Loss": [log_loss(y_prod, dt_model.predict_proba(x_features_prod_cleaned)), 
                         log_loss(y_prod, lr_model.predict_proba(x_features_prod_cleaned))],
            "Precision": [precision_score(y_prod, dt_predictions, zero_division=0), 
                          precision_score(y_prod, lr_predictions, zero_division=0)],
            "Recall": [recall_score(y_prod, dt_predictions, zero_division=0), 
                       recall_score(y_prod, lr_predictions, zero_division=0)],
            "F1-Score": [f1_score(y_prod, dt_predictions, zero_division=0), 
                         f1_score(y_prod, lr_predictions, zero_division=0)],
            }

    # Registrar métricas no MLflow
    mlflow.log_metric("dt_accuracy", accuracy_score(y_prod, dt_predictions))
    mlflow.log_metric("lr_accuracy", accuracy_score(y_prod, lr_predictions))
    mlflow.log_metric("dt_log_loss", log_loss(y_prod, dt_model.predict_proba(x_features_prod_cleaned)))
    mlflow.log_metric("lr_log_loss", log_loss(y_prod, lr_model.predict_proba(x_features_prod_cleaned)))
    mlflow.log_metric("dt_precision", precision_score(y_prod, dt_predictions, zero_division=0))
    mlflow.log_metric("lr_precision", precision_score(y_prod, lr_predictions, zero_division=0))
    mlflow.log_metric("dt_recall", recall_score(y_prod, dt_predictions, zero_division=0))
    mlflow.log_metric("lr_recall", recall_score(y_prod, lr_predictions, zero_division=0))
    mlflow.log_metric("dt_f1_score", f1_score(y_prod, dt_predictions, zero_division=0))
    mlflow.log_metric("lr_f1_score", f1_score(y_prod, lr_predictions, zero_division=0))

    print("Inferencia parte 05 - Métricas registradas no MLflow.")

    print(f"Métricas salvas no arquivo: {METRICS_FILE_PATH}")
    results_df = pd.DataFrame(results)

    # Registrar o CSV como artefato no MLflow
    results_df.to_csv(METRICS_FILE_PATH, index=False)
    mlflow.log_artifact(str(METRICS_FILE_PATH))

    # Gerar gráficos
    plot_predictions(x_features_prod, lr_predictions, BASE_DIR, 'lr_prod')  # Logistic Regression gráfico de produção
    plot_predictions(x_features_prod, dt_predictions, BASE_DIR, 'dt_prod')  # Decision Tree gráfico de produção

    print(f"Inferencia parte 05 - Gráficos salvos e registrados no MLflow")

    return x_features_prod


def plot_predictions(X_test, predictions, base_dir, prefix_name):
    """
    Gera um gráfico com as previsões do modelo especificado
    e salva o gráfico em BASE_DIR / 'data' / '08_reporting' com um nome dinâmico.

    Args:
        X_test (pd.DataFrame): Dados de entrada com as features "lon" e "lat".
        predictions (pd.Series): Previsões do modelo (1 = Cesta, 0 = Erro).
        base_dir (Path): Diretório base onde o gráfico será salvo.
        prefix_name (str): Prefixo do nome do arquivo, como 'lr_dev' ou 'dt_prod'.
    """
    # Diretório onde o gráfico será salvo
    reporting_path = base_dir / 'data' / '08_reporting'
    reporting_path.mkdir(parents=True, exist_ok=True)

    # Nome do arquivo baseado no prefixo
    file_name = f"{prefix_name}_predictions_scatter.png"
    scatter_plot_path = reporting_path / file_name

    # Remover duplicatas para evitar sobreposições desnecessárias
    data = X_test.copy()
    data['predictions'] = predictions  # Adiciona as previsões ao DataFrame
    data = data.drop_duplicates()

    # Mapear valores de previsões para cores
    colors = data['predictions'].map({True: 'green', False: 'red'})  # 1 = Cesta, 0 = Erro

    # Criar o gráfico de dispersão com tamanho ajustado
    fig, ax = plt.subplots(figsize=(12, 10))  # Tamanho maior para melhor visibilidade

    # Obter o caminho base do módulo (trainer/nodes.py)
    module_dir = Path(__file__).resolve().parent

    # Caminho correto para o arquivo de imagem
    image_path = module_dir.parent / 'trainer' / 'assets' / 'basket_court2.png'

    # Carregar a imagem da quadra de basquete
    img = mpimg.imread(str(image_path))

    # Definir os limites da quadra
    lon_min, lon_max = -118.5, -118.04  # Ajuste conforme necessário
    lat_min, lat_max = 33.5, 34.1      # Ajustado para a escala do dataset

    # Exibir a imagem da quadra como fundo
    ax.imshow(img, extent=[lon_min, lon_max, lat_min, lat_max], aspect='auto')

    # Adicionar os dados de previsões no gráfico
    scatter = ax.scatter(
        data['lon'], data['lat'], c=colors, alpha=0.6, edgecolors='k'
    )

    # Adicionar uma legenda manual
    legend_labels = {'green': 'Cesta', 'red': 'Erro'}
    handles = [
        plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color)
        for color in legend_labels.keys()
    ]
    ax.legend(handles, legend_labels.values(), title="Previsão do Arremesso")

    # Configurar título e rótulos dos eixos
    model_type = "Decision Tree" if "dt" in prefix_name else "Logistic Regression"
    dataset_type = "Dados de Desenvolvimento" if "dev" in prefix_name else "Dados de Produção"
    ax.set_title(f"Previsões {model_type} - {dataset_type}")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle='--', alpha=0.5)

    # Ajustar limites do gráfico
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)

    # Salvar o gráfico como arquivo
    plt.savefig(scatter_plot_path, dpi=300)
    plt.close()

    print(f"Gráfico salvo em: {scatter_plot_path}")
