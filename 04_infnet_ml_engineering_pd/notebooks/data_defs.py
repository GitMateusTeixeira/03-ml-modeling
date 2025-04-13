import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import seaborn as sns

# detalhar a base de dados
def check(df):
    l = []
    colunas = df.columns
    
    for col in colunas:
        dtypes = df[col].dtypes
        nunique = df[col].nunique()
        sum_null = df[col].isnull().sum()

        # calcular a moda e a frequência da moda
        moda = df[col].mode().iloc[0] if not df[col].mode().empty else 'n/a'
        moda_freq = df[col].value_counts().iloc[0] if not df[col].value_counts().empty else 'n/a'

        if np.issubdtype(dtypes, np.number):
            status = df.describe(include='all').T
            media = status.loc[col, 'mean']
            std = status.loc[col, 'std']
            min_val = status.loc[col, 'min']
            quar1 = status.loc[col, '25%']
            median = df[col].median()
            quar3 = status.loc[col, '75%']
            max_val = status.loc[col, 'max']
                    
        else:
            # definir 'n/a' de 'não se aplica'
            status = media = std = min_val = quar1 = median = quar3 = max_val = 'n/a'

        l.append([col, dtypes, nunique, sum_null, media, std, min_val, quar1, median, quar3, max_val, moda, moda_freq])
    
    # criar o DataFrame com as novas colunas para exibição
    df_check = pd.DataFrame(l)
    df_check.columns = ['coluna', 'tipo', 'únicos', 'null_soma', 'media', 'desvio', 
                        'minimo', '25%', 'mediana', '75%', 'maximo', 'moda', 'frequência_moda']
    
    return df_check

def shape(df, df_name):
    # Função auxiliar para extrair as informações
    def get_info(df):
        return {
            "Total Linhas": df.shape[0],
            "Linhas Únicas": len(df) - df.duplicated().sum(),
            "Linhas Duplicadas": df.duplicated().sum(),
            "Linhas com Nulos": df.isnull().any(axis=1).sum(),
            "": "",  # pula uma linha
            "Total Colunas": df.shape[1],
            "Int64": sum(df.dtypes == "int64"),
            "Float64": sum(df.dtypes == "float64"),
            "Object": sum(df.dtypes == "object")
        }

    # Criar DataFrame com as informações do DataFrame fornecido
    summary_df = pd.DataFrame({
        df_name: get_info(df)
    })

    return summary_df


def plot_boxplots(data, title):
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    num_vars = len(numeric_columns)
    
    if num_vars == 0:
        print("Nenhuma variável numérica para plotar.")
        return
    
    # Encontrar os números mais próximos para dividir as variáveis em linhas e colunas
    rows = int(np.floor(np.sqrt(num_vars)))
    cols = int(np.ceil(num_vars / rows))

    # Criar a figura e os eixos
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(cols * 5, rows * 4))
    fig.suptitle(f"Distribuição Dinâmica das Variáveis - {title}", fontsize=16)
    
    axes = np.array(axes).flatten()  # Garantir que os eixos sejam tratados como lista

    # Criar os boxplots
    for i, column in enumerate(numeric_columns):
        sns.boxplot(data=data, y=column, ax=axes[i], color='gray')
        axes[i].set_title(column, fontsize=12)
        axes[i].set_xlabel('')
        axes[i].set_ylabel('')
    
    # Remover eixos não utilizados
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Ajustar espaçamento para evitar sobreposição
    plt.subplots_adjust(hspace=0.4, wspace=0.4)
    
    plt.show()

def plot_histograms(data, title):
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    num_vars = len(numeric_columns)
    
    if num_vars == 0:
        print("Nenhuma variável numérica para plotar.")
        return
    
    # Encontrar os melhores valores para linhas e colunas
    rows = int(np.floor(np.sqrt(num_vars)))
    cols = int(np.ceil(num_vars / rows))

    # Criar a figura e os eixos
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(cols * 5, rows * 4))
    fig.suptitle(f"Análise da Faixa Dinâmica das Variáveis - {title}", fontsize=16)
    
    axes = np.array(axes).flatten()  # Garantir que os eixos sejam tratados como lista

    # Plotar os histogramas
    for i, col in enumerate(numeric_columns):
        sns.histplot(data=data, x=col, color='gray', kde=True, ax=axes[i])

        # Ajustar os limites do eixo Y com base na maior frequência da coluna
        max_y = data[col].value_counts().max()
        axes[i].set_ylim(0, max_y + max_y * 0.1)  # Adiciona 10% para espaço visual

        # Configurar título e labels
        axes[i].set_title(col, fontsize=12)
        axes[i].set_xlabel('')
        axes[i].set_ylabel('')
        axes[i].grid(True, alpha=0.8)

    # Remover eixos não utilizados
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Ajustar espaçamento para evitar sobreposição
    plt.subplots_adjust(hspace=0.3, wspace=0.2)

    # Exibir os gráficos
    plt.show()

