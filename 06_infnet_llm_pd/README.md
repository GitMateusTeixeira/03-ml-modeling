# Projeto de Disciplina de Inteligência Artificial generativa para linguagem (Large Language Model) [25E2_3]

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo' align='left'>
<br>
Projeto desenvolvido na disciplina de LLM para Aplicações Práticas em IA, com foco em reconhecimento de entidades nomeadas (NER) em notícias e análise de organizações mencionadas em textos jornalísticos.

<br>
<br>
<br>

## Índice

- <a href='#contexto'>1. Contexto</a>
- <a href='#tecnologias'>2. Tecnologias</a>
- <a href='#fluxograma-do-projeto'>3. Fluxograma do projeto</a>
    - <a href='#parte-01-pegar-os-dados'>3.1. Pegar os dados
    - <a href='#parte-02-processamento-inicial-dos-textos'>3.2. Processamento inicial dos textos
    - <a href='#parte-03-aplicação-do-modelo-de-ner'>3.3. Aplicação do modelo de NER
    - <a href='#parte-04-extração-de-organizações'>3.4. Extração de organizações
    - <a href='#parte-05-análise-estatística-e-visualização'>3.5. Análise estatística e visualização
- <a href='#conclusões-gerais'>4. Conclusões gerais</a>
- <a href='#sobre-mim'>5. Sobre mim</a> 


## Contexto

Este projeto foi desenvolvido no contexto da disciplina de Inteligência Artificial Generativa para Linguagem (Large Language Model), e visa aplicar técnicas de reconhecimento de entidades nomeadas (NER) em textos jornalísticos em português. 

A partir do modelo `monilouise/ner_pt_br`, foram extraídas entidades de notícias da seção “Mercado” da Folha UOL, publicadas no primeiro trimestre de 2015. 

O objetivo foi identificar as organizações mais citadas no período, utilizando ferramentas de processamento de linguagem natural, visualização de dados e análise estatística para revelar padrões de menções no contexto econômico.


## Tecnologias

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg' alt='Anaconda logo'> Anaconda v. 23.7.4

<img style='width:30px; vertical-align: middle; margin-right: 10px;' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg' alt='Jupyter logo'> Jupyter Notebook v. 5.7.2

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' alt='Python logo'> Python v. 3.10.18

Principais bibliotecas:

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kaggle/kaggle-original.svg" alt='kaggle_logo'> Kaggle 1.7.4.5

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" alt='matplotlib_logo'> Matplotlib 3.7.5

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" alt='numpy_logo'> Numpy 1.26.4

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='pandas_logo'> Pandas 2.2.3

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pypi/pypi-original.svg"/> Pypi pip-tools

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg' alt='scikit-learn_logo'> Scikit-learn 1.4.2

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt='seaborn_logo'> Seaborn 0.13.2

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg" alt='spacy_logo'> spaCy 3.8.4

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://raw.githubusercontent.com/tqdm/img/47dd765d1c88d70f65a3d2ce08430ffb175a9d53/logo.svg" alt='tqdm_logo'> tqdm 4.67.1

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="./assets/general_lib.png" alt='wordcloud_logo'> Wordcloud 1.9.4


## Fluxograma do projeto

O projeto segue o seguinte fluxograma (vamos mostrar por partes):

### Parte 01. Pegar os dados

⬆️ <a href='#índice'>Voltar ao início</a>

Os dados utilizados neste projeto foram obtidos a partir do Kaggle. O download foi realizado por meio de sua API, que permitiu acesso direto ao conjunto de notícias extraídas da seção "Mercado" da Folha UOL News Dataset.

Para isso, o comando `kaggle.api.dataset_download_files()` foi utilizado, garantindo que os arquivos fossem salvos no diretório especificado (`"../data/01-raw/"`). Esse processo facilita a manipulação dos dados no restante do pipeline de análise.


### Parte 02. Processamento inicial dos textos

⬆️ <a href='#índice'>Voltar ao início</a>

Os textos foram normalizados com limpeza básica: remoção de quebras de linha, caracteres indesejados e duplicidades. Foram também criadas colunas auxiliares para armazenar os resultados posteriores da etapa de NER.


### Parte 03. Aplicação do modelo de NER

⬆️ <a href='#índice'>Voltar ao início</a>

O modelo `monilouise/ner_pt_br`, baseado em transformers, foi aplicado para identificar entidades nomeadas nos textos. Essa etapa foi feita com pipeline do Hugging Face e uso de tqdm para monitorar o progresso.


### Parte 04. Extração de organizações

⬆️ <a href='#índice'>Voltar ao início</a>

A partir das entidades extraídas, foi feita a filtragem para reter apenas aquelas com classificação ligada a organizações (ORG). Também foi feita a reconstrução de tokens fragmentados (ex: “FG” + “##V”) e normalização dos nomes das entidades.


### Parte 05. Análise estatística e visualização

⬆️ <a href='#índice'>Voltar ao início</a>

Com os nomes de organizações limpos, foi gerado um ranking com as mais citadas. A visualização dos dados incluiu gráficos de barras e nuvens de palavras para destacar as principais instituições mencionadas.


## Conclusões Gerais

⬆️ <a href='#índice'>Voltar ao início</a>

Este projeto demonstrou a aplicação prática de modelos de linguagem para reconhecimento de entidades nomeadas em textos jornalísticos em português. Utilizando o modelo monilouise/ner_pt_br, foi possível identificar e filtrar organizações a partir das notícias da editoria “Mercado” da Folha UOL no primeiro trimestre de 2015, com foco na contagem e visualização das instituições mais citadas.

O processo incluiu etapas de coleta, limpeza, aplicação do modelo, reconstrução de tokens e análise estatística das entidades extraídas. As visualizações ajudaram a tornar os padrões mais visíveis e permitiram avaliar os dados de forma mais direta. O projeto também evidenciou limitações pontuais do modelo, como a fragmentação de nomes ou identificação imprecisa, indicando pontos a melhorar em futuros trabalhos


## Sobre mim

⬆️ <a href='#índice'>Voltar ao início</a>

<div>
    <img src="./docs/assets/logo_mt_ds.png" alt="mt_logo" style='width: 80px; vertical-align: middle;' align='left'>
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