# <img src='./assets/logo_infnetv1.png' alt='infnet_logo' style='width: 60px; vertical-align: middle; margin-right: 5px;'> Repositório de Machine Learning - Infnet

Este repositório contém projetos e modelos desenvolvidos ao longo do curso de Inteligência Artificial, Machine Learning e Deep Learning oferecido pelo INFNET, com metodologia do MIT.

Aqui, organizei os códigos e materiais das disciplinas concluídas, e o repositório será atualizado conforme avanço no curso.

## Índice

- <a href='#tecnologias'>1. Tecnologias</a>
- <a href='#progresso-do-curso'>2. Progresso do Curso</a>
- <a href='#estrutura-do-repositório'>3. Estrutura do Repositório</a>
- <a href='#trilha-de-aprendizado'>4. Trilha de Aprendizado</a>
    - <a href='#-algoritmos-de-inteligência-artificial-para-clusterização'>4.1. Algoritmos de Inteligência Artificial para Clusterização</a>
    - <a href='#-validação-de-modelos-de-clusterização'>4.2. Validação de Modelos de Clusterização</a>
    - <a href='#-algoritmos-de-inteligência-artificial-para-classificação'>4.3. Algoritmos de Inteligência Artificial para Classificação</a>
- <a href='#sobre-mim'>5. Sobre mim</a> 

## Tecnologias

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg' alt='anaconda_logo'> Anaconda v. 23.7.4

<img style='width:30px; vertical-align: middle; margin-right: 10px;' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg' alt='jupyter_logo'> Jupyter Notebook v. 5.7.2

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' alt='python_logo'> Python v. 3.12.4

Principais bibliotecas:

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" alt='matplotlib_logo'> Matplotlib

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" alt='numpy_logo'> Numpy

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='pandas_logo'> Pandas

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg' alt='scikit-learn_logo'> Scikit-learn

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://scipy.org/images/logo.svg" alt='scipy_logo'> Scipy

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt='seaborn_logo'> Seaborn

## Progresso do curso

🟦🟦🟦⬜⬜⬜⬜⬜ (3 de 8 matérias concluídas)

## Estrutura do repositório

Atualmente, temos os seguintes módulos concluídos:

➡️ <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_clustering_pd'>**infnet_clustering_pd**</a>: Algoritmos de Inteligência Artificial para Clusterização

➡️ <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_cluster_validation_pd'>**infnet_cluster_validation_pd**</a>: Validação de Modelos de Clusterização

➡️ <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_classification_pd'>**infnet_classification_pd**</a>: Algoritmos de Inteligência Artificial para Classificação

## Trilha de aprendizado

### 🟦 <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_clustering_pd'>Algoritmos de Inteligência Artificial para Clusterização</a>

⬆️ <a href='#índice'>Voltar ao início</a>

Nesta disciplina, aprendi a aplicar diferentes técnicas de clusterização (agrupamento) para segmentação de dados, explorando métodos baseados em partição, hierarquia e densidade, permitindo encontrar padrões ocultos sem a necessidade de rótulos. Além disso, compreendi como escolher o algoritmo mais adequado para diferentes tipos de conjuntos de dados e interpretar os resultados.

Pontos que aprendi:

- **K-Médias (K-Means)**: Algoritmo de clusterização baseado na minimização da distância entre pontos e centróides. Apliquei essa técnica para agrupar países com base em indicadores socioeconômicos.

- **K-Medóide (K-Medoid)**: Variante do K-Means que escolhe pontos reais do conjunto de dados como centróides, tornando-o mais robusto a outliers. Usei essa abordagem para reduzir o impacto de valores extremos nos agrupamentos.

- **Clusterização Hierárquica (HCluster)**: Método que constrói uma estrutura de agrupamento em formato de árvore. Usei essa abordagem para comparar diferentes estratégias de ligação entre clusters.

- **Agrupamento Espacial (DBSCAN)**: Algoritmo de clusterização baseado em densidade, robusto a outliers. Utilizei esse método para identificar grupos sem necessidade de definir o número de clusters previamente.

- **Agrupamento Espacial Denso (HDBSCAN)**: Extensão do DBSCAN que melhora a detecção de clusters com densidade variável. Apliquei essa técnica para segmentar dados em cenários onde os grupos possuíam diferentes tamanhos e formas.

- **Comparação de modelos**: Comparei e identifiquei as diferenças entre os métodos de clusterização

➡️ <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_clustering_pd'>Saiba mais</a>
<br>
<br>
### 🟦 <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_cluster_validation_pd'>Validação de Modelos de Clusterização</a>

⬆️ <a href='#índice'>Voltar ao início</a>

Nesta disciplina, aprofundei o conhecimento sobre métricas de avaliação para garantir a qualidade dos clusters gerados. Também explorei técnicas de pré-processamento para melhorar os resultados dos modelos.

Os principais pontos que aprendi foram:

- **Pré-processamento de Dados**: Etapa fundamental para melhorar a qualidade da clusterização. Apliquei técnicas como normalização, remoção de outliers e tratamento de dados ausentes para garantir melhores resultados nos agrupamentos. 

- **Índice de Silhueta (Silhouette)**: Mede a separação entre os clusters e ajuda a determinar o número ideal de agrupamentos. Comparei os resultados entre K-Means e DBSCAN para encontrar o melhor modelo.

- **Índice Davies-Bouldin**: Avalia a compacidade e separação dos clusters. Apliquei essa métrica para validar a segmentação de um conjunto de transações bancárias.

- **Clusterização de Séries Temporais**: Utilização de métodos como Correlação Cruzada e DTW (Dynamic Time Warping) para medir similaridade entre séries temporais.

➡️ <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_cluster_validation_pd'>Saiba mais</a>
<br>
<br>
### 🟦 <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_classification_pd'>Algoritmos de Inteligência Artificial para Classificação</a>

⬆️ <a href='#índice'>Voltar ao início</a>

Nesta disciplina, aprendi a utilizar algoritmos supervisionados para classificar dados em diferentes categorias. Trabalhei com técnicas de pré-processamento, construção e validação de modelos para melhorar a precisão das previsões. 

Alguns dos principais aprendizados foram:

- **Exploração de Dados**: análise e pré-processamento de um dataset real de vinhos portugueses.

- **Pré-processamento de Dados**: Transformação e normalização de variáveis para melhorar o desempenho dos modelos. Trabalhei com um conjunto de dados de vinhos portugueses, tratando valores ausentes e balanceando as classes.

- **Regressão Logística (Logistic Regression)**: Algoritmo estatístico para classificação binária. Treinei um modelo para prever a qualidade dos vinhos com base em suas propriedades físico-químicas.

- **Árvores de Decisão (Decision Tree)**: Método que divide os dados com base em perguntas hierárquicas. Usei essa técnica para analisar a importância de cada variável na classificação dos vinhos.

- **Máquinas Suportadas por Vetores (Support Vector Machine - SMV)**: Algoritmo que encontra o hiperplano ideal para separar as classes. Testei diferentes kernels para avaliar qual apresentava melhor desempenho no dataset.

- **Validação Cruzada (Cross Validation)**: Técnica para avaliar modelos de forma mais confiável. Apliquei Stratified K-Fold para garantir uma distribuição balanceada das classes nos treinamentos.

- **Otimização de Hiperparâmetros**: apliquei GridSearchCV para encontrar as melhores configurações para cada modelo.

- **Métricas de Desempenho**: Avaliei os modelos com diferentes métricas para entender sua eficácia:

    - **Acurácia (Accuracy)**: Mede a proporção de previsões corretas sobre o total de amostras.

    - **Precisão (Precision)**: Mede a taxa de verdadeiros positivos entre as previsões positivas do modelo. Essencial para problemas onde falsos positivos são críticos.

    - **Revocação (Recall)**: Mede a capacidade do modelo de identificar corretamente os verdadeiros positivos, importante em problemas onde falsos negativos devem ser minimizados.

    - **F1-Score**: Média harmônica entre precisão e recall, sendo útil quando há desbalanceamento de classes.

- **Curva ROC e AUC**: Comparação do desempenho dos modelos através da análise da taxa de verdadeiros e falsos positivos. Identifiquei que a Regressão Logística teve melhor performance na classificação dos vinhos.

➡️ <a href='https://github.com/GitMateusTeixeira/ml_models/tree/main/infnet_classification_pd'>Saiba mais</a>
<br>
<br>

### ⬜ Engenharia de Machine Learning

🔁 Em andamento.

### ⬜ Processamento de Linguagem Natural

🔁 Em andamento.

### ⬜ Inteligência Artificial Generativa para Linguagem (LLM)

🔁 Em andamento.

### ⬜ Redes Neurais

🔁 Em andamento.

### ⬜ Deep Learning

🔁 Em andamento.

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
