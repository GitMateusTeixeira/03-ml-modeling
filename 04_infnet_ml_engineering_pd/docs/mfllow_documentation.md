# Documentação do MlFlow

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo' align='left'>
<br>
Monitoramento completo e rastreamento de experimentos e modelos aplicados ao projeto Kobe Bryant 🏀.
<br>
<br>
<br>

## Índice

- <a href='#contexto'>1. Contexto</a>
- <a href='#tecnologias'>2. Tecnologias</a>
- <a href='#principais-componentes'>3. Principais componentes
- <a href='#artefatos'>4. Artefatos
    - <a href='#métricas-de-validação'>4.1. Métricas de validação
    - <a href='#modelos-treinados'>4.2. Modelos treinados
    - <a href='#gráficos-de-predições'>4.3. Gráficos de predições
    - <a href='#arquivos-de-inferência'>4.4. Arquivos de inferência
- <a href='#conclusões-gerais'>5. Conclusões gerais</a>
- <a href='#sobre-mim'>6. Sobre mim</a> 


## Contexto

O MLflow foi utilizado no projeto como ferramenta principal para rastrear experimentos de machine learning, armazenar métricas de validação e registrar modelos preditivos. Por meio dele, foi possível garantir a reprodutibilidade e a rastreabilidade de todas as etapas, desde o pré-processamento dos dados até a inferência dos modelos, promovendo um fluxo de trabalho organizado e monitorado.

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

## Principais componentes

O MLflow foi utilizado em diferentes aspectos do projeto, garantindo rastreabilidade e organização em cada etapa do ciclo de vida de aprendizado de máquina. Seus principais componentes ajudam na implementação e monitoramento da pipeline de Machine Learning feita pelo Kedro, assegurando que todos os experimentos fossem documentados e os modelos gerenciados.

### Rastreamento (tracking)

⬆️ <a href='#índice'>Voltar ao início</a>

O componente de rastreamento serve para capturar os parâmetros, métricas e artefatos gerados ao longo do pipeline. Cada execução foi registrada como um "run", permitindo que as etapas de pré-processamento, treino e inferência fossem monitoradas. 

<p align="center">
<img style='width:350px' src='./assets/mlflow_runs.png' alt='metrics'> 
</p>

Durante os treinamentos dos modelos de Regressão Logística e Árvore de Decisão, métricas como Logloss, acurácia, F1-score, precisão e recall foram calculadas e registradas, fornecendo uma visão clara da performance dos modelos. 

O tracking também permitiu armazenar gráficos de dispersão das predições e arquivos de validação, facilitando a análise dos resultados e a identificação do melhor modelo.


### Fluxo de projeto

⬆️ <a href='#índice'>Voltar ao início</a>

O MLflow Projects foi utilizado para estruturar o fluxo do projeto de forma organizada e reprodutível. Cada etapa do pipeline, desde o pré-processamento dos dados até a inferência, foi definida como um módulo claro e independente, permitindo que fosse executada e testada em ambientes diferentes. Isso garante que o projeto possa ser replicado.


### Modelos

⬆️ <a href='#índice'>Voltar ao início</a>

O registro e gerenciamento de modelos foram realizados por meio do componente Models. Após o treinamento dos modelos, eles foram salvos no formato .pkl, garantindo que as versões dos modelos fossem armazenadas e estivessem disponíveis para inferência futura. 


## Artefatos 

⬆️ <a href='#índice'>Voltar ao início</a>

Durante o desenvolvimento do projeto, diversos artefatos foram gerados ao longo das etapas do pipeline. Esses artefatos desempenham papéis fundamentais na análise, validação e inferência dos modelos.

### Métricas de validação

⬆️ <a href='#índice'>Voltar ao início</a>

Capturam os resultados das avaliações de desempenho dos modelos, como acurácia, F1-score e Logloss, e são salvos em formatos como '.csv'. Esses arquivos permitem análises e comparações entre os modelos, auxiliando na escolha do melhor candidato.

<p align="center">
<img style='width:350px' src='./assets/mlflow_metrics.png' alt='metrics'> 
</p>

### Modelos treinados

⬆️ <a href='#índice'>Voltar ao início</a>

Os modelos de Regressão Logística e Árvore de Decisão são armazenados em arquivos '.pkl'. Esses artefatos são importantes para inferências futuras, garantindo reprodutibilidade e acesso às versões validadas.

### Gráficos de predições

⬆️ <a href='#índice'>Voltar ao início</a>

Gerados para visualizar os resultados das inferências, os gráficos exibem a distribuição das predições e são salvos como imagens 'scatter.png'. Eles fornecem uma representação visual clara da performance dos modelos.

<p align="center">
<img style='width:450px' src='./assets/mfllow_scatter.png' alt='dt_scatter'> 
</p>

### Arquivos de inferência

São arquivos '.csv' que contêm as previsões feitas pelos modelos aplicados aos dados de produção:

<p align="center">
<img style='width:700px' src='./assets/mlflow_inference.png' alt='metrics'> 
</p>

Além dos resultados das métricas de validação obtidos:

<p align="center">
<img style='width:300px' src='./assets/mlflow_inference_metrics.png' alt='metrics'> 
</p>

Note que o modelo de Regressão Logística obteve valor 0 em 'Precisão', 'Recall' e 'F1-Score', isso por que todos os dados de produção referem-se a arremessos longos, cujo resultado obtido pelo modelo foi de 100% de erros.


## Outras considerações

⬆️ <a href='#índice'>Voltar ao início</a>

Demais considerações estarão presentes na documentação sobre pipeline e no README.md geral do projeto.


## Conclusões Gerais

⬆️ <a href='#índice'>Voltar ao início</a>

O uso do MLflow no projeto foi essencial para organizar e monitorar todas as etapas do ciclo de vida de machine learning. Ele garantiu rastreabilidade, permitindo revisões detalhadas dos experimentos e resultados. Essa abordagem mostrou-se valiosa para reprodutibilidade e análise, criando um fluxo de trabalho robusto e transparente para o desenvolvimento e aplicação de modelos preditivos.

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