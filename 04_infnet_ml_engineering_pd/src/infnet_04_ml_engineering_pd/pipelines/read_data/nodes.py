import os
import pandas as pd
from pathlib import Path

def read_data(file_name: str, output_suffix: str) -> str:
    """
    Lê e processa os dados de entrada (desenvolvimento ou produção), ajusta tipos, 
    remove valores ausentes e salva os dados processados.

    Args:
        file_name: Nome do arquivo bruto (parquet).
        output_suffix: Identificador para diferenciar desenvolvimento ('dev') e produção ('prod').

    Returns:
        Caminho do arquivo processado.
    """
    # Diretório base do projeto
    BASE_DIR = Path(__file__).resolve().parents[4]

    # Caminho onde os dados brutos estão armazenados
    DATA_PATH = BASE_DIR / 'data' / '01_raw'
    FILE_PATH = DATA_PATH / file_name

    # Ler o arquivo bruto
    data = pd.read_parquet(FILE_PATH)

    # Tratar os dados: ajustar tipos e remover valores ausentes
    data = data.assign(
        playoffs=lambda x: x['playoffs'].astype(bool),
        shot_made_flag=lambda x: x['shot_made_flag'].astype(bool)
    ).dropna(subset=['shot_made_flag'])

    # Caminho onde os dados processados serão armazenados
    PROCESSED_DATA_PATH = BASE_DIR / 'data' / '02_intermediate'
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    # Caminho do arquivo processado
    PROCESSED_FILE_PATH = PROCESSED_DATA_PATH / f'data_filtered_{output_suffix}.parquet'

    # Salvar os dados processados
    data.to_parquet(PROCESSED_FILE_PATH, index=False)

    print(f"Arquivo processado salvo em: {PROCESSED_FILE_PATH}")
    return str(PROCESSED_FILE_PATH)