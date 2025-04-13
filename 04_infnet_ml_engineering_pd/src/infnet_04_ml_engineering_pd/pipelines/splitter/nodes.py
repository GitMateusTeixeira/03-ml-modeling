import pandas as pd
import mlflow
from pathlib import Path
from sklearn.model_selection import train_test_split

def split_data(x_features_file: str, y_features_file: str) -> dict:
    """
    Lê os arquivos de X e y de features (dados de desenvolvimento), divide em treino e teste,
    salva os resultados e registra no MLflow.

    Args:
        x_features_file: Caminho para o arquivo de X (variáveis independentes).
        y_features_file: Caminho para o arquivo de y (variáveis dependentes).

    Returns:
        dict: Caminhos dos arquivos de treino e teste gerados.
    """

    with mlflow.start_run(nested=True):
        # Diretório base do projeto
        BASE_DIR = Path(__file__).resolve().parents[4]

        # Caminho para salvar os dados de treino e teste
        MODEL_INPUT_PATH = BASE_DIR / 'data' / '05_model_input'
        MODEL_INPUT_PATH.mkdir(parents=True, exist_ok=True)

        # Caminhos dos arquivos gerados
        X_TRAIN_FILE_PATH = MODEL_INPUT_PATH / 'model_input_x_train.parquet'
        X_TEST_FILE_PATH = MODEL_INPUT_PATH / 'model_input_x_test.parquet'
        Y_TRAIN_FILE_PATH = MODEL_INPUT_PATH / 'model_input_y_train.parquet'
        Y_TEST_FILE_PATH = MODEL_INPUT_PATH / 'model_input_y_test.parquet'

        print("Slitter 01 - ler os arquivos")
        
        # Ler os arquivos de features X e y
        try:
            X = x_features_file
            y = y_features_file

        except Exception as e:
            raise ValueError(f"Erro ao carregar os arquivos de entrada: {e}")
        
        print("Slitter 02 - separar os arquivos")

        # Separar em treino (80%) e teste (20%) de forma estratificada
        test_size = 0.2
        X_train, X_test, y_train, y_test = train_test_split(
                                                            X, y, 
                                                            test_size=test_size, 
                                                            random_state=17, 
                                                            stratify=y
                                                            )

        print("Slitter 03 - salvar os arquivos")

        # Salvar os arquivos separados de treino e teste
        try:
            X_train.to_parquet(X_TRAIN_FILE_PATH, index=False)
            X_test.to_parquet(X_TEST_FILE_PATH, index=False)
            y_train.to_parquet(Y_TRAIN_FILE_PATH, index=False)
            y_test.to_parquet(Y_TEST_FILE_PATH, index=False)
        
        except Exception as e:
            raise ValueError(f"Erro ao salvar os arquivos: {e}")

        # Registrar artefatos no MLflow
        mlflow.log_artifact(str(X_TRAIN_FILE_PATH))
        mlflow.log_artifact(str(X_TEST_FILE_PATH))
        mlflow.log_artifact(str(Y_TRAIN_FILE_PATH))
        mlflow.log_artifact(str(Y_TEST_FILE_PATH))

        # Registrar shapes no MLflow
        mlflow.log_metric("x_train_shape", X_train.shape[0])
        mlflow.log_metric("x_test_shape", X_test.shape[0])
        mlflow.log_metric("y_train_shape", y_train.shape[0])
        mlflow.log_metric("y_test_shape", y_test.shape[0])
        mlflow.log_metric("test_size", test_size)
        print("Shapes registrados no MLflow:\n" \
              f"x_train={X_train.shape}, x_test={X_test.shape}, y_train={y_train.shape}, y_test={y_test.shape}")

        print(f"Arquivos de treino e teste salvos em: {MODEL_INPUT_PATH}")

        return {
            "x_train": X_train,
            "x_test": X_test,
            "y_train": y_train,
            "y_test": y_test,
        }