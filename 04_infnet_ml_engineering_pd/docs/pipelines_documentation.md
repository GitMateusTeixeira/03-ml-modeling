# Documentação da pipeline do Kedro

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo' align='left'>
<br>
Esta pipeline treina dois modelos de aprendizado de máquina (árvore de decisão e regressãol logística) para prever se um arremesso foi convertido em cesta, utilizando uma base de dados de arremessos do Kobe Bryant 🏀.
<br>
<br>
<br>

## Índice

- <a href='#contexto'>1. Contexto</a>
- <a href='#tecnologias'>2. Tecnologias</a>
- <a href='#nós-da-pipeline'>3. Nós da Pipeline</a>
    - <a href='#baixar-os-dados-get_data'>3.1. Baixar os dados (get_data)
    - <a href='#ler-e-tratar-dos-dados-read_data'>3.2. Ler e tratar dos dados (read_data)
    - <a href='#separar-as-features-featuring'>3.3. Separar as features (featuring)
    - <a href='#dividir-os-dados-de-produção-em-treino-e-teste-splitter'>3.4. Dividir os dados de produção em treino e teste (splitter)
    - <a href='#treinar-os-modelos-de-regressão-logística-logistic-regression-e-de-árvore-de-decisão'>3.5.a. Treinar os modelos de Regressão Logística (Logistic Regression) e de Árvore de Decisão (Decision Tree) - (trainer)
    - <a href='#árvore-de-decisão-decision-tree'>3.5.b. Realizar a inferência com os dados de produção (trainer)
- <a href='#métricas-de-validação'>4. Métricas de validação
    - <a href='#validação-cruzada-k-fold'>4.1. Validação Cruzada (K-Fold)
    - <a href='#acurácia'>4.2. Acurácia
    - <a href='#precisão'>4.3. Precisão
    - <a href='#recall-sensibilidade'>4.4. Recall (Sensibilidade)
    - <a href='#f1-score'>4.5. F1-Score
    - <a href='#logloss'>4.6. Logloss
- <a href='#outras-considerações'>5. Comparação entre os modelos
- <a href='#conclusões-gerais'>6. Conclusões gerais</a>
- <a href='#sobre-mim'>7. Sobre mim</a> 


## Contexto

Este projeto foi desenvolvido como parte da disciplina de Engenharia de Machine Learning. O objetivo principal é construir, avaliar, documentar e monitorar modelos de machine learning capazes de prever se um atleta irá ou não acertar a cesta com base nas características dos jogos.

## Tecnologias

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg' alt='Anaconda logo'> Anaconda v. 23.7.4

<img style='width:30px; vertical-align: middle; margin-right: 10px;' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg' alt='Jupyter logo'> Jupyter Notebook v. 5.7.2

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' alt='Python logo'> Python v. 3.11.11

Principais bibliotecas:

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="data:image/svg+xml;utf8,%3Csvg%20role%3D%22img%22%20viewBox%3D%220%200%2024%2024%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20id%3D%22Kedro--Streamline-Simple-Icons%22%20height%3D%2224%22%20width%3D%2224%22%3E%3Cdesc%3EKedro%20Streamline%20Icon%3A%20https%3A%2F%2Fstreamlinehq.com%3C%2Fdesc%3E%3Ctitle%3EKedro%3C%2Ftitle%3E%3Cpath%20d%3D%22m12%200%2012%2012%20-12%2012L0%2012%2012%200z%22%20fill%3D%22%23ffc900%22%20stroke-width%3D%221.0000%22%3E%3C%2Fpath%3E%3C%2Fsvg%3E" alt='kedro_logo'> Kedro 0.19.12

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" alt='matplotlib_logo'> Matplotlib 3.7.5

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://github.com/mlflow-automation.png" alt='mlflow_logo'> MlFlow 2.12.2

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" alt='numpy_logo'> Numpy 1.26.4

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='pandas_logo'> Pandas

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg' alt='scikit-learn_logo'> Scikit-learn 1.4.2

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt='seaborn_logo'> Seaborn

## Nós da Pipeline

### Baixar os dados (get_data)

⬆️ <a href='#índice'>Voltar ao início</a>

Esse nó se propõe a se conectar com o <a href= 'https://github.com/tciodaro/eng_ml/raw/main/data/'>repositório do GitHub</a>, baixar os arquivos "dataset_kobe_dev.parquet", "dataset_kobe_prod.parquet" para análises e salvar em '../data/01_raw/'.


### Ler e tratar dos dados (read_data)

⬆️ <a href='#índice'>Voltar ao início</a>

Esse nó carrega os dados baixados, ajusta os tipos das colunas ('playoffs' e 'shot_made_flag' para bool), remove os valores nulos das linhas e salva os arquivos em '../data/02_intermediate/' no formato '.parquet'.


### Separar as features (featuring)

⬆️ <a href='#índice'>Voltar ao início</a>

Esse nó carrega os dados de '../data/02_intermediate/', seleciona as colunas:

- 'lat': posição verrtical do atleta na quadra,
- 'lon': posição horizontal do atleta na quadra, 
- 'minutes_remaining': tempo faltante de jogo,
- 'period': período do jogo,
- 'playoffs': se é ou não um jogo eliminatório,
- 'shot_distance': a distância do arremesso,
- 'shot_made_flag': se o atleta acertou ou não o arremesso (será nosso 'y')

Separa os dados em 'X' (o dataset que vamos usar para realizar as predições) e 'y' (nosso target de predição), registra os arquivos como artefatos no MlFlow e salva os mesmos em '../data/04_feature/' no formato '.parquet'.


### Dividir os dados de produção em treino e teste (splitter)

⬆️ <a href='#índice'>Voltar ao início</a>

Esse nó se aplica apenas aos dados de desenvolvimento. Ele carrega os dados de '../data/04_feature/', separa os dados em:

- X_train: dados de treino, 
- X_test: dados de teste,
- y_train: alvo de predição de treino,
- y_test: alvo de predição de teste

Registra no MlFlow e salva cada um dos arquivos em '../data/05_model_input/' no formato '.parquet'.

### Treinar os modelos de Regressão Logística (Logistic Regression) e de Árvore de Decisão 

⬆️ <a href='#índice'>Voltar ao início</a>

Esse nó é dividido em duas partes: o treino dos modelos (que se aplica apenas aos dados de desenvolvimento) e a inferência dos mesmos (que se aplica apenas aos dados de produção).

Na parte de treino (trainer()), esse nó recebe os dados de '../data/05_model_input/', treina os modelos de:

- Árvore de Decisão (Decision Tree): A Árvore de Decisão é um modelo baseado em regras de decisão hierárquicas, onde os dados são divididos de forma sucessiva com base em critérios como gini ou entropia. Esse modelo é altamente interpretável, mas pode sofrer de overfitting se não for corretamente ajustado.

- Regressão Logística (Logistic Regression): A Regressão Logística é um modelo estatístico usado para problemas de classificação binária. Ele estima a probabilidade de uma amostra pertencer a uma classe específica usando uma função sigmoide. Esse modelo é eficiente, rápido e fornece probabilidades bem calibradas, o que facilita a interpretação dos resultados.

Registra as métricas de validação no MlFlow (accuracy, precision, recall, f1-score e logloss - serão explicados mais a frente), salva os modelos no formato '.pkl' em '../data/06_models/' e salva os resultados 'results.csv' das validações e os gráficos das predições '{prefix_name}_predictions_scatter.png' em '../data/08_reporting/'.

### Realizar a inferência com os dados de produção (trainer) 

⬆️ <a href='#índice'>Voltar ao início</a>

A segunda parte desse nó (inference()) recebe os dados de '../data/04_feature/' e:

- carrega os modelos.pkl de '../data/06_models/';
- realiza a inferência dos modelos;
- salva o arquivo de produção como '.csv', juntamente com as colunas contendo as predições dos modelos inferidos;
- registra as métricas de validação no MlFlow (accuracy, precision, recall, f1-score e logloss - serão explicados mais a frente);
- registra os resultados como artefato no MlFlow; e
- salva os gráficos das predições '{prefix_name}_predictions_scatter.png' em '../data/08_reporting/'

## Métricas de Validação

⬆️ <a href='#índice'>Voltar ao início</a>

Para avaliar o desempenho dos modelos de classificação, foram utilizadas cinco métricas principais: acurácia, precisão, recall, F1-score e AUC-ROC. Cada uma dessas métricas fornece uma visão diferente sobre a performance dos modelos, permitindo uma análise mais completa, especialmente considerando o desbalanceamento da base de dados.

### Validação Cruzada (K-Fold)

A validação cruzada estratificada (Stratified K-Fold) foi aplicada com k=10, garantindo que a distribuição das classes fosse mantida em todas as divisões do conjunto de treino e teste. Essa técnica permite avaliar o desempenho do modelo de forma mais confiável, reduzindo a influência de uma divisão específica dos dados.

### Acurácia

A acurácia mede a proporção total de classificações corretas feitas pelo modelo em relação ao total de observações. Ela é frequentemente usada como métrica principal em problemas de classificação, mas pode ser enganosa quando há desbalanceamento de classes. Isso ocorre porque um modelo pode parecer ter um bom desempenho apenas por favorecer a classe majoritária.

A acurácia foi calculada para cada modelo, servindo como uma métrica geral de desempenho. No entanto, devido ao desbalanceamento dos dados, ela não foi usada isoladamente para escolher o melhor modelo.

### Precisão

A precisão (precision) mede a proporção de previsões positivas que realmente pertencem à classe positiva. Em outras palavras, indica quantos dos vinhos classificados como "bons" realmente possuem alta qualidade. Essa métrica é essencial em cenários onde falsos positivos podem ser problemáticos, ou seja, quando um erro pode levar a decisões equivocadas, como recomendar um vinho de baixa qualidade como se fosse premium.

No projeto, a precisão foi usada para avaliar se os modelos estavam classificando corretamente os vinhos de qualidade superior. Como a base de dados era desbalanceada, um modelo com alta precisão pode indicar que ele é conservador e evita atribuir rótulos positivos quando há incerteza.

### Recall (Sensibilidade)

O recall (ou sensibilidade) mede a proporção de amostras realmente positivas que foram corretamente classificadas pelo modelo. Ele indica a capacidade do modelo de identificar corretamente todos os vinhos de qualidade superior. Essa métrica é especialmente importante quando o objetivo é minimizar falsos negativos, ou seja, evitar que vinhos bons sejam classificados erroneamente como ruins.

O recall foi essencial para garantir que vinhos de boa qualidade não fossem subestimados pelo modelo. Como havia um desbalanceamento na base de dados, o recall ajudou a verificar se os modelos estavam conseguindo detectar corretamente a minoria dos vinhos classificados como bons.

### F1-score

O F1-score é a média harmônica entre a precisão e o recall, fornecendo um equilíbrio entre essas duas métricas. Ele é especialmente útil quando há um trade-off entre minimizar falsos positivos e falsos negativos. Um F1-score alto indica que o modelo tem um bom desempenho tanto na identificação dos vinhos bons quanto na redução de erros na classificação.

Como a base de dados era desbalanceada, o F1-score foi escolhido como a métrica principal para comparar os modelos. Ele ajudou a encontrar o modelo que conseguia equilibrar bem a classificação correta dos vinhos bons sem comprometer a precisão ou o recall.

### Logloss

A métrica Logarithmic Loss (Logloss) avalia modelos de classificação probabilística, medindo o quão bem as previsões refletem os valores reais. Ela penaliza fortemente previsões erradas feitas com alta confiança, incentivando modelos a serem cautelosos em cenários de incerteza.

A Logloss foi empregada no projeto para avaliar a precisão probabilística dos modelos preditivos utilizados na previsão de acertos de arremessos. Durante o pipeline, a Logloss foi utilizada para ajustar e comparar modelos como Árvore de Decisão e a Regressão Logística, garantindo que os modelos não apenas acertassem as classificações, mas também produzissem probabilidades confiáveis para cada arremesso. Valores menores da métrica indicaram melhorias no desempenho e maior confiança nas previsões.


## Outras considerações

⬆️ <a href='#índice'>Voltar ao início</a>

Demais considerações estarão presentes na documentação sobre artefatos e no README.md geral do projeto.

## Conclusões Gerais

⬆️ <a href='#índice'>Voltar ao início</a>

O projeto demonstrou como pipelines de Machine Learning podem ser estruturadas e monitoradas de maneira eficiente para resolver problemas reais. Através da utilização de modelos de classificação como Regressão Logística e Árvore de Decisão, foi possível prever com boa precisão se um atleta acertaria ou não o arremesso. Métricas como Logloss e F1-score forneceram insights sobre o desempenho dos modelos, enquanto ferramentas como Kedro e MLflow garantiram a rastreabilidade e documentação de cada etapa.

Além disso, os resultados indicaram que, ao compreender características do jogo como posição na quadra, tempo restante e contexto de playoffs, os modelos puderam oferecer previsões confiáveis. O uso de técnicas como validação cruzada contribuiu para a robustez dos resultados. Esse trabalho exemplifica como a Engenharia de Machine Learning pode ser aplicada para criar soluções impactantes e bem-calibradas.

## Sobre mim

⬆️ <a href='#índice'>Voltar ao início</a>

<div style="display: flex; align-items: center;">
    <img src="https://avatars.githubusercontent.com/u/156105588?v=4" alt="Minha foto" align='left' style="width:150px; border-radius: 50%; margin-right: 15px;">
    <div>
        <div>
            <img src="./assets/logo_mt_ds.png" alt="mt_logo" style='width: 80px; vertical-align: middle;' align='left'>
            <span style="">Mateus Teixeira</span>
        </div>
        Cientista de dados
        <br>
        Pós-graduando em Inteligência Artifcial pela INFNET
        <br>
        <br>
        <a href="mailto:pessoal.mtr@gmail.com"
        target="_blank">
            <img 
            src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&labelColor=555&logoColor=white" 
            alt="E-mail" 
            height='25'/>
        </a>
        <a href="https://www.linkedin.com/in/mateusteixeira/" 
        target="_blank">
            <img 
            src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&labelColor=555&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAABNklEQVR4nO3XSUoDQRgG0NrFTRyiuBA8lARvIujanROKnigICh5AVASHkDPECZ60yULFVDqamEqoB73rGj6q6q/uELIsmz6o4QgPeEUTx1gMEzL5Kz+7xnxIGQ7F7YWU6WybmNuQMrz0CfAcUobHPgHuQ8p0qk/MfpiAKnTTY/KXyVehApZw0q3/xT1whwMsfLyQZVNMCcNohxVsoNEt3U9o4RRbWE0yACrYLnFhtrGLmWQCYA4XBnOO5VQCnA04+c/tKikE+IudSQ/QLnWwEw5Q2EwhQFEy66h2n7XIH+B3jXEHKCZf6/EB2SzRvjXuAPXIuOsl2r+NO0A1Mu7sb8f+twCjGvuLHCAi9GEIfeQViMkrIG+hjlEdQEPoIx/imLwC8hbqyIe4ByWEUXWSTIAsy8JEeQd/X93eUJrQcwAAAABJRU5ErkJggg==" 
            alt="LinkedIn" 
             height='25'/>
        </a>
        <a href="https://www.instagram.com/omateusteixeira" 
        target="_blank">
            <img 
            src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&labelColor=555&logoColor=white" 
            alt="Instagram" 
             height='25'/>
        </a>
    </div>
</div>