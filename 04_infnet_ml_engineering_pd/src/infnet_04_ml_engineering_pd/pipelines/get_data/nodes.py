import requests
from pathlib import Path

def get_data() -> None:
    """
    Baixa os arquivos de um repositório GitHub fixo e os salva no diretório especificado.
    """
    # Parâmetros fixos
    repo_url = "https://github.com/tciodaro/eng_ml/raw/main/data/"
    files = ["dataset_kobe_dev.parquet", "dataset_kobe_prod.parquet"]
    save_path = Path(__file__).resolve().parents[4] / 'data' / '01_raw'

    # Criação do diretório se não existir
    save_path.mkdir(parents=True, exist_ok=True)
    downloaded_files = []

    for file in files:
        file_url = repo_url + file
        file_path = save_path / file
        
        if not file_path.exists():
            print(f"Baixando {file}...")
            response = requests.get(file_url)
            
            if response.status_code == 200:

                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    
                print(f"{file} salvo em {file_path}")
                downloaded_files.append(str(file_path))

            else:
                print(f"Erro ao baixar {file}: {response.status_code}")

        else:
            print(f"{file} já existe em {file_path}. Pulando o download...")
    
    print("Download concluído!")
    return downloaded_files