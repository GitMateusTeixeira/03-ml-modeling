# Projeto de Disciplina de Processamento de Linguagem Natural com Python [25E2_2]

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo' align='left'>
<br>
Projeto desenvolvido na disciplina de Processamento de Linguagem Natural com Python para aplicar técnicas de análise de texto, extração de tópicos e modelagem de linguagem, utilizando ferramentas modernas como spaCy, NLTK e LDA.

<br>
<br>
<br>

## Índice

- <a href='#contexto'>1. Contexto</a>
- <a href='#tecnologias'>2. Tecnologias</a>
- <a href='#configuração-inicial'>3. Configuração inicial</a>
- <a href='#fluxograma-do-projeto'>4. Fluxograma do projeto
    - <a href='#parte-01-pegar-os-dados'>4.1. Pegar os dados
    - <a href='#parte-02-pré-processamento-dos-dados'>4.2. Pré-processamento dos dados
    - <a href='#parte-03-geração-de-documentos-spacy'>4.3. Geração de documentos `spaCy`
    - <a href='#parte-04-lematização'>4.4. Lematização
    - <a href='#parte-05-reconhecimento-de-entidades-nomeadas-ner'>4.5. Reconhecimento de Entidades Nomeadas (NER)
    - <a href='#parte-06-bag-of-words'>4.6. Bag of Words
    - <a href='#parte-07-extração-de-tópicos'>4.7. Extração de Tópicos
    - <a href='#parte-08-visualização-dos-dados'>4.8. Visualização dos dados
- <a href='#conclusões-gerais'>5. Conclusões gerais</a>
- <a href='#sobre-mim'>6. Sobre mim</a> 


## Contexto

Este projeto foi desenvolvido no contexto da disciplina de Processamento de Linguagem Natural com Python, e visa aplicar técnicas avançadas para análise de textos, extração de tópicos e modelagem semântica. Utilizando um conjunto de notícias da seção "Mercado" da Folha de S. Paulo (2016), exploramos métodos como TF-IDF, LDA e reconhecimento de entidades nomeadas, permitindo uma interpretação estruturada dos dados. Além disso, buscamos aprimorar a compreensão sobre vetorização de textos, aprendizado não supervisionado e visualização de informações, proporcionando uma abordagem prática e aprofundada na área de Processamento de Linguagem Natural.


## Tecnologias

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg' alt='Anaconda logo'> Anaconda v. 23.7.4

<img style='width:30px; vertical-align: middle; margin-right: 10px;' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg' alt='Jupyter logo'> Jupyter Notebook v. 5.7.2

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' alt='Python logo'> Python v. 3.11.11

Principais bibliotecas:

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kaggle/kaggle-original.svg" alt='kaggle_logo'> Kaggle 1.7.4.5

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" alt='matplotlib_logo'> Matplotlib 3.7.5

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="./assets/general_lib.png" alt='nltk_logo'> NLTK 3.9.1

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" alt='numpy_logo'> Numpy 1.26.4

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='pandas_logo'> Pandas 2.2.3


- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pypi/pypi-original.svg"/> Pypi pip-tools
          

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg' alt='scikit-learn_logo'> Scikit-learn 1.4.2

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt='seaborn_logo'> Seaborn 0.13.2

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg" alt='spacy_logo'> spaCy 3.8.4

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://raw.githubusercontent.com/tqdm/img/47dd765d1c88d70f65a3d2ce08430ffb175a9d53/logo.svg" alt='tqdm_logo'> tqdm 4.67.1

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="./assets/general_lib.png" alt='wordcloud_logo'> Wordcloud 1.9.4


## Configuração inicial

⬆️ <a href='#índice'>Voltar ao início</a>

O projeto foi realizado no ambiente virtual '🌐 env_25E2_2', instalado pelo Anconda.

Para garantir a instalação eficiente das dependências, utilizamos o pip-tools, uma ferramenta que permite gerenciar pacotes de forma controlada e reproduzível.


## Fluxograma do projeto

O projeto segue o seguinte fluxograma (vamos mostrar por partes):

### Parte 01. Pegar os dados

⬆️ <a href='#índice'>Voltar ao início</a>

Os dados utilizados neste projeto foram obtidos a partir do Kaggle. O download foi realizado por meio de sua API, que permitiu acesso direto ao conjunto de notícias extraídas da seção "Mercado" da Folha de S. Paulo.

Para isso, o comando `kaggle.api.dataset_download_files()` foi utilizado, garantindo que os arquivos fossem salvos no diretório especificado (`"../data/01-raw/"`) e extraídos automaticamente (`unzip=True`). Esse processo facilita a manipulação dos dados no restante do pipeline de análise.

### Parte 02. Pré-processamento dos dados

⬆️ <a href='#índice'>Voltar ao início</a>

O pré-processamento dos textos é visa garantir a qualidade da análise de tópicos. Nesse processo, foi aplicado diversas técnicas de limpeza e transformação dos dados, garantindo que as informações estejam organizadas e prontas para os modelos de aprendizado de máquina. Dentre elas estão:

- **Remoção de caracteres especiais e pontuação**: onde símbolos irrelevantes são eliminados para evitar ruídos no modelo;

- **Normalização de texto**: convertendo tudo para letras minúsculas para padronizar a análise;

- **Tokenização**: o texto é separado em tokens individuais, para segmentar as palavras;

- **Remoção de stopwords e filtragem de palavrs indesejadas**: excluímos palavras muito frequentes e sem relevância semântica, como 'o', 'é' e 'de'. Além da remoção de palavras sem muito valor semêntico para a análise, como 'chegar', 'haver', 'ficar';

- **Stemming e Lemmatização**: redução das palavras à sua raiz ou forma base, preservando seu significado.

Além disso, foram criadas as seguinte colunas no dataset para realizar a análise dos dados:

- `nltk` – Contém a versão tokenizada do texto, utilizando nltk.word_tokenize();

- `tokenizer` – Representa as palavras já filtradas, sem stopwords e caracteres especiais;

- `stemmer` – Apresenta as palavras reduzidas à sua forma radical, aplicando o algoritmo RSLP do NLTK.

Essas transformações ajudam a reduzir a dimensionalidade do texto e melhorar sua estrutura, facilitando etapas posteriores como extração de tópicos e vetorização.


### Parte 03. Geração de documentos `spaCy`

⬆️ <a href='#índice'>Voltar ao início</a>

A utilização do `spaCy` permite processar textos de forma eficiente e estruturada, fornecendo uma análise linguística robusta para cada documento. Nesta etapa, cada texto do dataset foi convertido em um objeto spaCy, o que facilitou operações como tokenização, lematização, reconhecimento de entidades nomeadas (NER) e diversas análises linguísticas.

Para realizar essa conversão, utilizou-se o modelo `pt_core_news_lg`, um dos mais avançados para a língua portuguesa. Esse modelo foi carregado e seu processamento foi aplicado em cada texto do dataset, gerando uma nova coluna chamada `spacy_doc`. Essa coluna contém os objetos `spaCy` correspondentes aos textos, permitindo que as análises subsequentes sejam feitas diretamente sobre essas representações linguísticas.

A aplicação do modelo foi realizada por meio da função `progress_apply(nlp)`, garantindo eficiência no processamento de um grande volume de dados. Embora essa operação possa levar alguns minutos para ser concluída, ela é essencial para preparar os textos para análises posteriores, como extração de tópicos, reconhecimento de entidades nomeadas e vetorização dos textos.

### Parte 04. Lematização

⬆️ <a href='#índice'>Voltar ao início</a>

A `lematização` é uma técnica de processamento de linguagem natural que transforma palavras (ex: 'trabalhou') em suas formas base (ex: 'trabalhar'), garantindo que variações morfológicas sejam reduzidas sem perder o significado do texto. Ao contrário do `stemming`, que apenas corta sufixos, a `lematização` usa conhecimento linguístico para encontrar a forma mais apropriada de cada termo, tornando a análise mais precisa.

Nesta etapa, o `spaCy` foi utilizado, já que fornece suporte nativo à lematização em português, algo que o `NLTK` não possui. Para garantir um pré-processamento eficiente, criamos uma lista combinada de stopwords provenientes do `NLTK` e do `spaCy`, removendo palavras muito frequentes que não agregam significado à análise de tópicos.

Além disso, foi implemetado um filtro que exclui tokens indesejados, garantindo que os lemmas extraídos sejam relevantes para o estudo. A função `lemma()` aplica esse processamento a cada documento no dataset, gerando a coluna `spacy_lemma`, que contém os tokens lematizados de cada texto. 

Essa transformação melhora a qualidade dos dados para extração de tópicos e análise semântica, reduzindo ruídos e tornando os vetores textuais mais representativos.

### Parte 05. Reconhecimento de Entidades Nomeadas (NER)

⬆️ <a href='#índice'>Voltar ao início</a>

O Reconhecimento de Entidades Nomeadas (NER) é uma técnica essencial no Processamento de Linguagem Natural, utilizada para identificar e categorizar elementos importantes dentro de um texto, como pessoas, organizações, locais e datas. Essa abordagem permite estruturar informações não estruturadas, facilitando a análise de relações entre entidades.

Nesta etapa, o modelo do `spaCy` é utilizado para extrair organizações mencionadas nos textos. Para isso, a função `NER()` percorre cada documento e identifica entidades classificadas como `"ORG"`, armazenando-as na coluna `spacy_ner` do dataset. Esse processo possibilita a visualização das empresas, instituições ou marcas mais citadas nos textos, auxiliando na identificação de padrões e tendências do mercado.

### Parte 06. Bag of Words

⬆️ <a href='#índice'>Voltar ao início</a>

A técnica de Bag of Words (BoW) é um método utilizado para representar textos numericamente, transformando-os em vetores baseados na frequência de ocorrência de palavras. Essa abordagem ignora a estrutura gramatical e a ordem das palavras, focando apenas na presença e frequência dos termos, o que facilita análises estatísticas e aprendizado de máquina.

Nesta etapa, o `TF-IDF` (Term Frequency-Inverse Document Frequency) é utilizado para atribuir pesos aos termos, destacando aqueles que são mais representativos no contexto dos documentos. Para isso, foi criada a coluna `tfidf` no dataframe `news_2016`, utilizando a coluna `spacy_lemma` como base para o cálculo dos vetores `TF-IDF`.

O número máximo de características consideradas no modelo é 5000, e um token precisa ter aparecido pelo menos 10 vezes (`min_df`) nos documentos para ser incluído na matriz. Para garantir que os dados estejam organizados, uma classe `Vectorizer` foi implementada para pré-processar os textos e transformar listas de tokens em vetores, utilizando a biblioteca scikit-learn (`TfidfVectorizer`).

A função `tokens2tfidf()` converte os tokens lematizados em vetores TF-IDF, permitindo que sejam armazenados na coluna `tfidf` do dataset. Essa representação melhora a análise de tópicos e possibilita identificar padrões de relevância semântica no conjunto de dados.

### Parte 07. Extração de Tópicos

⬆️ <a href='#índice'>Voltar ao início</a>


A extração de tópicos é uma técnica que permite identificar padrões semânticos e agrupar documentos por temas latentes. Para isso, o Latent Dirichlet Allocation (LDA) é utilizado, um modelo probabilístico que associa palavras a tópicos, gerando uma estrutura interpretável do conjunto de textos.

Nesta etapa, a implementação do LDA disponível no scikit-learn foi utilizada para identificar 9 tópicos presentes nos textos da seção "Mercado". Para garantir um processamento robusto, o número máximo de iterações foi definido como 100 (`max_iter`), permitindo uma convergência mais precisa dos tópicos, e um valor de `random_seed` foi aplicado para garantir reprodutibilidade nos resultados.

O corpus textual é convertido em uma matriz numérica (`tfidf`), que serve de entrada para o algoritmo LDA. Após o treinamento, cada documento recebe um tópico predominante, identificado através da função `get_topic()`, que calcula a distribuição de tópicos do documento e seleciona aquele de maior relevância. Esse resultado é armazenado na coluna `topic`, permitindo a segmentação dos textos conforme os temas gerados pelo modelo.


### Parte 08. Visualização dos dados

⬆️ <a href='#índice'>Voltar ao início</a>

Para interpretar os resultados da análise de tópicos, foram utilizadas técnicas de visualização gráfica e de nuvens de palavras, permitindo explorar a distribuição dos temas extraídos do conjunto de notícias.

- **8.1. Gráfico de Número de Documentos vs Tópicos**

    O gráfico gerado exibe a distribuição dos tópicos nas notícias, mostrando quantos documentos foram classificados em cada tema identificado pelo modelo LDA. As barras horizontais representam a frequência de documentos por tópico, e a escala logarítmica no eixo X ajuda a visualizar diferenças significativas na quantidade de notícias por categoria.

    Esse tipo de visualização facilita a interpretação dos tópicos mais recorrentes e quais temas tiveram maior presença no conjunto de textos analisados.

- **8.2. Nuvem de Palavras por Tópicos**

    A nuvem de palavras é uma técnica de visualização que destaca os termos mais frequentes dentro de cada tópico identificado pelo modelo LDA. Quanto maior a palavra na imagem, maior sua relevância dentro daquele contexto específico, facilitando a interpretação dos principais temas abordados nos documentos.

    Nesta etapa, as colunas `spacy_lemma` e `topic` são utilizadas para gerar nuvens de palavras para cada um dos 9 tópicos identificados. A função `plot_wordcloud_for_a_topic()` extrai os termos lematizados pertencentes a cada tópico e os converte em uma visualização gráfica utilizando a biblioteca `WordCloud`.

    Cada gráfico gerado representa visualmente os termos mais recorrentes no respectivo tópico, auxiliando na análise semântica e na interpretação dos temas abordados nos textos.

- **8.3. Nuvem de Palavras por Entidades**

    Já a nuvem de palavras por entidades é uma técnica de visualização que destaca organizações mencionadas em cada tópico identificado pelo modelo `LDA`. Essa abordagem facilita a análise da frequência e relevância das entidades dentro dos textos, ajudando a compreender quais instituições ou empresas são mais citadas em cada contexto.

    Nesta etapa, as colunas `spacy_ner` e `topic` também foram utilizadas para criar as nuvens de palavras por entidades nomeadas. 
    
    A função `plot_wordcloud_entities_for_a_topic()` processa os documentos e extrai organizações mencionadas, substituindo espaços em nomes compostos por "_" para melhor exibição na nuvem de palavras.

    Cada tópico recebe uma nuvem de entidades nomeadas, permitindo uma visualização intuitiva das instituições mais recorrentes nos textos analisados.


## Conclusões Gerais

⬆️ <a href='#índice'>Voltar ao início</a>

Este projeto demonstrou a importância do Processamento de Linguagem Natural na extração de tópicos e análise de grandes volumes de texto. A partir de técnicas como TF-IDF, LDA e reconhecimento de entidades nomeadas, foi possível estruturar e interpretar os dados textuais, identificando padrões relevantes nos documentos analisados.

A aplicação de pré-processamento com NLTK e spaCy garantiu 
que os textos fossem preparados de forma a permitir que os tópicos fossem segmentados através do modelo LDA. Além disso, a utilização de Bag of Words e vetorização TF-IDF possibilitou uma representação quantitativa dos textos, facilitando sua análise computacional.

O projeto também demonstrou a diferença entre `lematização` e `stemming` no tratamento dos termos. 

Enquanto a lematização, realizada com spaCy, transforma as palavras em suas formas base considerando contexto gramatical e significado, o stemming, utilizado via NLTK, aplica um recorte mais simples dos sufixos das palavras sem levar em conta sua estrutura linguística completa. Essa distinção se reflete diretamente na qualidade da análise semântica, tornando a lematização mais apropriada para tarefas que exigem maior precisão na interpretação dos textos.

Por fim, as visualizações gráficas, como distribuição dos tópicos, nuvem de palavras e entidades nomeadas, ajudaram a tornar os resultados mais compreensíveis e acessíveis. A estruturação dos dados e os métodos aplicados reforçaram o potencial das técnicas de PLN na interpretação de grandes corpora textuais, trazendo insights para a análise semântica.


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