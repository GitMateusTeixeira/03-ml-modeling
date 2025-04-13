import os
import pandas as pd
import mlflow
from pathlib import Path


def featuring(input_file: pd.DataFrame, feature_suffix: str) -> dict:
    """
    Lê os dados processados e separa as variáveis independentes (X) e dependentes (y),
    registrando no MLflow.

    Args:
        input_file: DataFrame contendo os dados de entrada.
        feature_suffix: Sufixo para diferenciar desenvolvimento ('dev') ou produção ('prod').

    Returns:
        dict: DataFrames contendo X e y gerados.
    """
    
    with mlflow.start_run(nested=True):
        # Diretório base do projeto
        BASE_DIR = Path(__file__).resolve().parents[4]

        # Caminho para salvar os arquivos de features
        FEATURE_DATA_PATH = BASE_DIR / 'data' / '04_feature'
        os.makedirs(FEATURE_DATA_PATH, exist_ok=True)

        # Caminhos dos arquivos de saída
        X_FEATURES_FILE_PATH = FEATURE_DATA_PATH / f'x_features_{feature_suffix}.parquet'
        Y_FEATURES_FILE_PATH = FEATURE_DATA_PATH / f'y_features_{feature_suffix}.parquet'

        # Usar diretamente o DataFrame recebido como input_file
        data = input_file

        # Selecionar as colunas que serão usadas para a extração de features
        features = ['lat', 'lon', 'minutes_remaining', 'period', 'playoffs', 'shot_distance', 'shot_made_flag']

        # Garantir que todas as colunas em 'features' existem no DataFrame
        missing_features = [col for col in features if col not in data.columns]
        if missing_features:
            raise ValueError(f"As seguintes colunas estão ausentes no arquivo de entrada: {missing_features}")

        # Separar X e y usando as colunas existentes
        X = data[features[:-1]].copy()  # Variáveis independentes (todas exceto a última)
        y = data[[features[-1]]].copy()  # Variável dependente (última coluna)

        # Salvar os arquivos (opcional para rastreabilidade)
        try:
            X.to_parquet(X_FEATURES_FILE_PATH, index=False)
            y.to_parquet(Y_FEATURES_FILE_PATH, index=False)  # Converte Series para DataFrame

        except Exception as e:
            raise ValueError(f"Erro ao salvar os arquivos de X e y: {e}")

        # Registrar artefatos no MLflow
        mlflow.log_artifact(str(X_FEATURES_FILE_PATH))
        mlflow.log_artifact(str(Y_FEATURES_FILE_PATH))

        # Retornar os próprios DataFrames
        return X, y