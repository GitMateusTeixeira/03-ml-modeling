# Projeto de Disciplina de Validação de Modelos de Clusterização

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo'>

Projeto desenvolvido como parte da disciplina de Validação de Modelos de Clusterização, aplicando técnicas para avaliar a qualidade dos agrupamentos gerados por algoritmos de aprendizado não supervisionado.

## Índice

- <a href='#tecnologias'>1. Tecnologias</a>
- <a href='#contexto'>2. Contexto</a>
- <a href='#análises'>3. Análises</a>
    - <a href='#análise-exploratória'>3.1. Análise exploratória</a>
    - <a href='#k-means'>3.2. K-Means</a>
    - <a href='#dbscan'>3.3. DBSCAN</a>
    - <a href='#comparação-entre-os-modelos'>3.4. Comparação entre os modelos
- <a href='#conclusões-gerais'>4. Conclusões gerais</a>
    - <a href='#conclusões-da-análise-do-k-means'>4.1. Conclusões da análise do K-Means</a>
    - <a href='#conclusões-da-análise-do-dbscan'>4.2. Conclusões da análise do DBSCAN</a>
- <a href='#sobre-mim'>5. Sobre mim</a> 

## Tecnologias

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg' alt='Anaconda logo'> Anaconda v. 23.7.4 (ambiente virtual chamado '⚙️ venv_clusterizacao2')

<img style='width:30px; vertical-align: middle; margin-right: 10px;' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg' alt='Jupyter logo'> Jupyter Notebook v. 5.7.2

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' alt='Python logo'> Python v. 3.11.11

Principais bibliotecas:

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" alt='matplotlib_logo'> Matplotlib

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" alt='numpy_logo'> Numpy

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='pandas_logo'> Pandas

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg' alt='scikit-learn_logo'> Scikit-learn

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://scipy.org/images/logo.svg" alt='scipy_logo'> Scipy

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt='seaborn_logo'> Seaborn


## Contexto

⬆️ <a href='#índice'>Voltar ao início</a>

A clusterização é amplamente utilizada para segmentar dados, mas a qualidade dos agrupamentos gerados pode variar conforme o modelo e os hiperparâmetros utilizados. Este projeto tem como objetivo validar os clusters formados a partir dos algoritmos K-Means e DBSCAN, utilizando métricas como índice de Silhueta, coeficiente de similaridade e redução de dimensionalidade para avaliar a coesão e separação entre os grupos.

O conjunto de dados utilizado contém informações sobre transações bancárias, incluindo idade, saldo da conta, valor da transação e localização do cliente. A validação dos clusters é essencial para compreender se os agrupamentos refletem padrões reais ou se são apenas artefatos estatísticos.

O arquivo possui as seguintes colunas:

- _id_transacao_ (TransactionID): Id da transferência feita
- _id_cliente_ (CustomerID): Id do cliente
- _idade_calculada_ (CustomerDOB): Idade do cliente no período da transferência
- _genero_ (CustGender): Gênero sexual do cliente
- _localizazao_ (CustLocation): Localização do cliente
- _saldo_ (CustAccountBalance): Saldo da conta do cliente após a transferência
- _data_transacao_ (TransactionDate): Data da transferência
- _hora_transacao_ (TransactionTime): Hora da transferência em timestamp Unix (o número de segundos que se passaram desde a data da coluna anterior)
- _quantia_transacao (INR)_ (TransactionAmount (INR)): Valor da transferência em rúpias indianas (INR)


## Análises

⬆️ <a href='#índice'>Voltar ao início</a>

### Análise Exploratória

Antes de aplicar os modelos de clusterização, realizamos uma análise exploratória dos dados para entender sua distribuição e identificar possíveis outliers. Foram utilizados boxplots para visualizar a dispersão das variáveis numéricas, permitindo observar padrões como a variação dos saldos dos clientes e os valores das transações.

Os gráficos revelaram que algumas variáveis apresentavam grande variação, sugerindo a presença de valores discrepantes que poderiam influenciar os agrupamentos. Essa análise inicial foi fundamental para ajustar os parâmetros dos modelos e garantir uma segmentação mais precisa dos clientes.

<p align='center'> <img style='max-width:100%; height:auto; align:center' src='./assets/boxplot.png' alt="Boxplot dos dados"> </p>

### K-Means

O K-Means segmentou os clientes em grupos distintos com base em idade, saldo e valor das transações. A análise dos clusters revelou padrões importantes: clientes com maior retenção de saldo foram agrupados separadamente dos que possuem maior movimentação financeira.

O modelo mostrou-se eficiente na formação de agrupamentos homogêneos, mas foi sensível a outliers. Alguns clientes com padrões de transação atípicos acabaram influenciando a definição dos centroides, o que pode comprometer a separação dos grupos. Para resolver essa questão, técnicas de normalização e remoção de valores discrepantes podem ser aplicadas antes da clusterização.

<p align='center'> <img style='max-width:85%; height:auto; align:center' src='./assets/kmeans.png' alt="Kmeans plot"> </p>

### DBSCAN

O DBSCAN identificou clusters baseados na densidade dos dados, separando clientes que apresentam comportamento mais homogêneo daqueles que possuem padrões de transação únicos. Um dos grandes benefícios do DBSCAN foi a capacidade de detectar outliers automaticamente, eliminando ruídos que poderiam distorcer os agrupamentos.

Por outro lado, a escolha dos hiperparâmetros eps e MinPts se mostrou crucial para o desempenho do modelo. Valores inadequados desses parâmetros resultaram em clusters excessivamente fragmentados ou na falha do algoritmo em detectar agrupamentos significativos. Com o ajuste correto, o DBSCAN conseguiu segmentar os clientes de forma mais flexível do que o K-Means.

<p align='center'> <img style='max-width:85%; height:auto; align:center' src='./assets/dbscan.png' alt="DBSCAN plot"> </p>

### Comparação entre os Modelos

A comparação entre os modelos revelou que o K-Means foi mais eficiente na definição de clusters compactos e bem separados, enquanto o DBSCAN foi melhor na identificação de padrões de comportamento atípico. O índice de Silhueta mostrou que, em certos cenários, o K-Means obteve melhores resultados em termos de separação entre clusters, mas sua sensibilidade a outliers foi uma limitação.

O DBSCAN, por sua vez, demonstrou maior adaptabilidade, identificando grupos mais flexíveis sem a necessidade de definir um número fixo de clusters. No entanto, seu desempenho variou significativamente conforme a escolha dos hiperparâmetros. Em aplicações práticas, a combinação das abordagens pode ser útil para obter um panorama mais completo da segmentação dos clientes.


## Conclusões gerais

⬆️ <a href='#índice'>Voltar ao início</a>

### Conclusões da análise do K-Means

Da análise, pode-se depreender que o K-Means clusterizou os clientes da seguinte forma:

- Cluster 0: em sua maioria, homens de 22 a 31 anos de MUMBAI e BANGALORE, que retem cerca de 72% a 90% de seu saldo;

- Cluster 1: em sua maioria, homens de 22 a 33 anos de NEW DELHI e MUMBAI, que retem cerca de 20% a 47% de seu saldo;

- Cluster 2: em sua maioria, homens de 21 a 31 anos de MUMBAI e BANGALORE, que retem cerca de 0% a 20% de seu saldo;

- Cluster 3: em sua maioria, homens de 22 a 31 anos de MUMBAI e NEW DELHI, que retem cerca de 90% a 100% de seu saldo;

- Cluster 4: em sua maioria, homens de 22 a 31 anos de MUMBAI  e BANGALORE, que retem cerca de 47% a 73% de seu saldo;

- Cluster 5: em sua maioria, homens de 38 a 48 anos de MUMBAI e BANGALORE, que retem cerca de 68% a 100% de seu saldo;

Os clientes do _Cluster 0_, _Cluster 3_ e parte dos clientes do _Cluster 4_ e _Cluster 5_ possuem, em geral um ótimo perfil para oferecimento de produtos de investimento e linhas de crédito, pois retem boa parte de seu saldos bancários e suas contas (em torno de 68% a 100%), não oferecendo risco de inadimplência, por exemplo;

Os clientes do _Cluster 2_ e parte do _Cluster 1_ não são tão indicados para esses produtos, possuindo muito mais capital de giro do que retendo patrimônio (entre 0% e 20%), oferencendo um alto risco de inadimplência.

E ainda que não faça parte da moda, observou-se que os clientes mais velhos (de 60 a 85 anos) possuem uma maior retenção de seu saldo (entre 80% e 100%), como evidenciado no _Cluster 5_.

### Conclusões da análise do DBSCAN

O DBSCAN, por sua vez, agrupou os dados da seguinte forma:

- Cluster 0: em sua maioria, homens de 22 a 31 anos de MUMBAI e NEW DELHI, que retem cerca de 48% a 100% de seu saldo;

- Cluster 1: em sua maioria, homens de 22 a 31 anos de MUMBAI e BANGALORE, que retem cerca de 0% a 18% de seu saldo;

- Cluster 2: em sua maioria, homens de 23 a 29 anos de NEW DELHI e DELHI, que retem cerca de 24% a 31% de seu saldo;

- Cluster 3: em sua maioria, homens de 25 a 27 anos de NEW DELHI e BANGALORE, que retem cerca de 34% a 37% de seu saldo;

- Cluster 4: em sua maioria, homens de 25 a 27 anos de NEW DEHLI e DEHLI, que retem cerca de 44% a 47% de seu saldo;

Segundo o DBSCAN, os clientes do _Cluster 1_ e do _Cluster 2_ são clientes que possuem um alto capital de giro e não retem quase nada de seu patrimônio.

Já os clientes do _Cluster 0_ são clientes que retem muito mais patrimônio, sendo mais indicados para oferecer produtos de investimento e também confirmando o perfil traçado pelo KMeans.

## Sobre mim

⬆️ <a href='#índice'>Voltar ao início</a>

<div style="display: flex; align-items: center;">
    <img src="https://avatars.githubusercontent.com/u/156105588?v=4" alt="Minha foto" style="width:150px; border-radius: 50%; margin-right: 15px;">
    <div>
        <div style="font-size: 16px; font-weight: bold">Mateus Teixeira</div>
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
