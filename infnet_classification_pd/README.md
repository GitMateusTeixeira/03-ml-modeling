# Projeto de Disciplina de Algoritmos de Inteligência Artificial para Classificação

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo'>

Projeto de disciplina de clusterização, utilizando modelos de aprendizado não supervisionado.

## Índice

- <a href='#tecnologias'>1. Tecnologias</a>
- <a href='#contexto'>2. Contexto</a>
- <a href='#análises'>3. Análises</a>
    - <a href='#31-exploração-dos-dados'>3.1. Exploração de dados
    - <a href='#32-modelagem'>3.2. Modelagem
    - <a href='#33-validação-cruzada-k-fold-e-métricas-de-avaliação'>3.3. Validação Cruzada e Métricas de Avaliação
    - <a href='#34-comparação-de-modelos-e-resultados'>3.4. Comparação de modelos e resultados
- <a href='#sobre-mim'>4. Sobre mim</a> 

## Tecnologias

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg' alt='Anaconda logo'> Anaconda v. 23.7.4

<img style='width:30px; vertical-align: middle; margin-right: 10px;' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg' alt='Jupyter logo'> Jupyter Notebook v. 5.7.2

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' alt='Python logo'> Python v. 3.12.4

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg' alt='Python logo'> Scikit-learn

## Contexto

Este projeto foi desenvolvido como parte da disciplina de Algoritmos de Inteligência Artificial para Classificação. O objetivo principal é construir e avaliar modelos de machine learning capazes de classificar vinhos portugueses (tintos e brancos) com base em suas características físico-químicas.

Os dados utilizados foram extraídos do artigo:

- P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. _Modeling wine preferences by data mining from physicochemical properties_. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

A base contém diversas variáveis relacionadas à composição química dos vinhos e sua qualidade, avaliada em uma escala de 0 a 10. Para simplificar a classificação, a variável quality foi transformada na variável categórica opinion, onde:

- **0** → Vinhos considerados de qualidade inferior ou igual a 5;

- **1** → Vinhos considerados de qualidade superior a 5

O foco do estudo foi determinar a eficiência de diferentes modelos na classificação de vinhos com base nesses atributos, considerando métricas como F1-score e AUC-ROC.

## Análises

### 3.1. Exploração dos Dados

A análise exploratória revelou informações importantes sobre a base de dados. O conjunto de dados contém vinhos tintos e brancos e apresenta diversas variáveis físico-químicas, como acidez, teor alcoólico, nível de açúcar residual, pH e concentração de dióxido de enxofre. A variável original de qualidade (quality) foi convertida em uma variável categórica chamada opinion, onde vinhos com nota menor ou igual a 5 foram classificados como ruins (0) e os demais como bons (1).

Durante a análise, foram identificados valores nulos em sete colunas, além de linhas duplicadas, que foram removidas. Para lidar com os dados ausentes, foi aplicada uma estratégia de preenchimento baseada na média ou mediana, dependendo da distribuição dos valores.

O balanceamento dos dados também foi analisado, revelando que os vinhos brancos são mais desbalanceados (com predominância de vinhos de baixa qualidade), enquanto os vinhos tintos possuem uma distribuição mais equilibrada entre vinhos bons e ruins.

### 3.2. Modelagem

Para a classificação dos vinhos, foram testados três modelos de machine learning: Regressão Logística, Árvore de Decisão e Support Vector Machine (SVM).

#### Regressão Logística (Logistic Regression)

A Regressão Logística é um modelo estatístico usado para problemas de classificação binária. Ele estima a probabilidade de uma amostra pertencer a uma classe específica usando uma função sigmoide. Esse modelo é eficiente, rápido e fornece probabilidades bem calibradas, o que facilita a interpretação dos resultados.

No experimento, a Regressão Logística foi treinada com validação cruzada estratificada usando K-Fold (k=10). Além disso, foram testados diferentes hiperparâmetros, utilizando o Grid Search para encontrar a melhor configuração do modelo.

#### Árvore de Decisão (Decision Tree)

A Árvore de Decisão é um modelo baseado em regras de decisão hierárquicas, onde os dados são divididos de forma sucessiva com base em critérios como gini ou entropia. Esse modelo é altamente interpretável, mas pode sofrer de overfitting se não for corretamente ajustado.

Para melhorar o desempenho da Árvore de Decisão, foram testados hiperparâmetros como profundidade máxima, número mínimo de amostras por folha e critério de divisão. O ajuste foi feito utilizando Grid Search com validação cruzada K-Fold (k=10).

#### Máquinas Suportadas por Vetores (Support Vector Machine - SVM)

O modelo SVM busca encontrar um hiperplano de separação ótimo entre as classes, maximizando a margem entre os dados. Quando os dados não são linearmente separáveis, o SVM utiliza funções kernel (como RBF e polinomial) para mapear os dados para um espaço dimensional maior, onde a separação seja possível.

A SVM geralmente é um modelo mais computacionalmente custoso, especialmente em grandes volumes de dados. Para otimizar seu desempenho, foram ajustados hiperparâmetros como tipo de kernel, parâmetro C (penalização) e gamma, utilizando Grid Search com validação cruzada K-Fold (k=10).

### 3.3. Validação Cruzada (K-Fold) e Métricas de Avaliação

A validação cruzada estratificada (Stratified K-Fold) foi aplicada com k=10, garantindo que a distribuição das classes fosse mantida em todas as divisões do conjunto de treino e teste. Essa técnica permite avaliar o desempenho do modelo de forma mais confiável, reduzindo a influência de uma divisão específica dos dados.

Para avaliar o desempenho dos modelos de classificação, foram utilizadas cinco métricas principais: acurácia, precisão, recall, F1-score e AUC-ROC. Cada uma dessas métricas fornece uma visão diferente sobre a performance dos modelos, permitindo uma análise mais completa, especialmente considerando o desbalanceamento da base de dados.

- **Acurácia**: Mede a proporção de classificações corretas em relação ao total de amostras. Embora seja uma métrica amplamente utilizada, pode ser enganosa em bases desbalanceadas, pois um modelo pode ter alta acurácia apenas por favorecer a classe majoritária.

- **Precisão**: Mede a proporção de predições positivas que realmente pertencem à classe positiva. É útil em cenários onde falsos positivos devem ser minimizados, garantindo que apenas os vinhos corretamente classificados como "bons" sejam considerados.

- **Recall (Sensibilidade)**: Mede a capacidade do modelo de identificar corretamente os casos positivos dentro de todas as ocorrências reais da classe positiva. É uma métrica importante quando a prioridade é minimizar falsos negativos.

- **F1-score**: Representa a média harmônica entre precisão e recall, equilibrando ambos os aspectos. Como a base de dados é desbalanceada, essa métrica foi priorizada na comparação dos modelos, pois considera tanto os verdadeiros positivos corretamente identificados quanto os erros de classificação.

- **AUC-ROC (Área Sob a Curva ROC)**: Avalia a capacidade do modelo de distinguir entre as classes positiva e negativa. A curva ROC compara a taxa de verdadeiros positivos (sensibilidade) com a taxa de falsos positivos, permitindo visualizar o desempenho do modelo independentemente do limiar de decisão. Quanto mais próximo de 1, melhor a separação entre as classes.

<img style='width:500px' src='./assets/roc_curve.png' alt='ROC curve'>

Essas métricas foram analisadas em conjunto para garantir que os modelos escolhidos apresentassem um bom equilíbrio entre eficiência na classificação, minimização de erros e generalização.

### 3.4. Comparação de Modelos e Resultados

Como a base de dados era desbalanceada, o F1-score foi escolhido como métrica principal para avaliar o desempenho dos modelos.

A Regressão Logística apresentou os melhores resultados, com um F1-score médio de 63,77% no treino e 64,63% no teste, além de uma AUC-ROC de 80,30%. Seu desempenho consistente torna esse modelo a melhor escolha para uma eventual operação de classificação de vinhos.

## Sobre mim

<div style="display: flex; align-items: center;">
    <img src="https://avatars.githubusercontent.com/u/156105588?v=4" alt="Minha foto" style="width:150px; border-radius: 50%; margin-right: 15px;">
    <div>
        <div style="font-size: 16px; font-weight: bold">Mateus Teixeira</div>
        Pós-graduando em Inteligência Artifcial pela INFNET
        <br>
        <br>
        <a href="mailto:pessoal.mtr@gmail.com"
        target="_blank">
            <img 
            src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" 
            alt="E-mail" 
            style='height: 25px; margin-right: 10px; border-radius: 5px;'>
        </a>
        <a href="https://www.linkedin.com/in/mateusteixeira/" 
        target="_blank">
            <img 
            src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4Ij48cGF0aCBmaWxsPSIjMDA3NmIyIiBkPSJNMTE2IDNIMTJhOC45MSA4LjkxIDAgMDAtOSA4Ljh2MTA0LjQyYTguOTEgOC45MSAwIDAwOSA4Ljc4aDEwNGE4LjkzIDguOTMgMCAwMDktOC44MVYxMS43N0E4LjkzIDguOTMgMCAwMDExNiAzeiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yMS4wNiA0OC43M2gxOC4xMVYxMDdIMjEuMDZ6bTkuMDYtMjlhMTAuNSAxMC41IDAgMTEtMTAuNSAxMC40OSAxMC41IDEwLjUgMCAwMTEwLjUtMTAuNDlNNTAuNTMgNDguNzNoMTcuMzZ2OGguMjRjMi40Mi00LjU4IDguMzItOS40MSAxNy4xMy05LjQxQzEwMy42IDQ3LjI4IDEwNyA1OS4zNSAxMDcgNzV2MzJIODguODlWNzguNjVjMC02Ljc1LS4xMi0xNS40NC05LjQxLTE1LjQ0cy0xMC44NyA3LjM2LTEwLjg3IDE1VjEwN0g1MC41M3oiLz48L3N2Zz4=" 
            alt="LinkedIn" 
            style='height: 25px; margin-right: 10px; border-radius: 5px;'>
        </a>
        <a href="https://www.instagram.com/omateusteixeira" 
        target="_blank">
            <img 
            src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" 
            alt="Instagram" 
            style='height: 25px; border-radius: 5px;'>
        </a>
    </div>
</div>
