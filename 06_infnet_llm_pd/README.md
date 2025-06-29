# Projeto de Disciplina de Inteligência Artificial generativa para linguagem (Large Language Model) [25E2_3]

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo' align='left'>
<br>
Projetos desenvolvidos na disciplina de LLM para Aplicações Práticas em IA, com foco em NER, análise de dados com transformers e sistemas interativos baseados em LangChain e Streamlit.

<br>
<br>
<br>

## Índice

- <a href='#contexto'>1. Contexto</a>
- <a href='#tecnologias'>2. Tecnologias</a>
- <a href='#configuração-inicial'>3. Configuração inicial</a>
- <a href='#estrutura-dos-arquivos'>4. Estrutura dos arquivos
- <a href='#análise-de-dados-com-ner'>5. Estrutura dos arquivos
- <a href='#aplicativo-de-perguntas-e-respostasr'>6. Aplicativo de perguntas e respostas
- <a href='#conclusões-gerais'>7. Conclusões gerais</a>
- <a href='#sobre-mim'>8. Sobre mim</a> 


## Contexto

Estes projetos foram desenvolvidos no contexto da disciplina de Inteligência Artificial Generativa para Linguagem (Large Language Model), e visam explorar, na prática, o potencial de modelos de linguagem na resolução de problemas reais. As atividades abrangeram desde o reconhecimento de entidades em textos jornalísticos usando transformers e NER, até o desenvolvimento de um sistema de perguntas e respostas interativo com LLMs, LangChain e Streamlit. O objetivo foi aplicar conceitos teóricos em soluções concretas e acessíveis, promovendo experimentação e pensamento crítico.


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

- <img style='width:30px; vertical-align: middle; margin-right: 10px'  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg" /> Streamlit 1.44.1

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://raw.githubusercontent.com/tqdm/img/47dd765d1c88d70f65a3d2ce08430ffb175a9d53/logo.svg" alt='tqdm_logo'> tqdm 4.67.1

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="./assets/general_lib.png" alt='wordcloud_logo'> Wordcloud 1.9.4


## Configuração inicial

⬆️ <a href='#índice'>Voltar ao início</a>

O projeto foi realizado no ambiente virtual '🌐 env_25E2_3_v2, instalado pelo Anconda.

Para garantir a instalação eficiente das dependências, utilizamos o pip-tools, uma ferramenta que permite gerenciar pacotes de forma controlada e reproduzível. Foi feita a compilação do arquivo '📄 requirements.in' com o comando `pip-compile requirements.in` e para a instalação dos pacotes, recomenda-se a utilização do comenado `pip install -r requirements.txt --user` para evitar erros de permissões.


## Estrutura dos arquivos

Como se tratam de dois projetos distintos. Esse repositório possui a seguinte estrutura:

- 📁 '02_quizzes_hugging_face/' : contendo os prints do curso de `NLP` da Hugging Face, contendo os quizes e o certificado do Módulo `Fundamentals of LLMs`.

- 📁 '03_analise_de_dados_com_ner/' : contendo os arquivos de análise textual com `NER`, do corpus retirado do Kaggle.

- 📁 '05_perguntas_cdc/' : contendo os arquivos do aplicativo de perguntas e respostas sobre Direito do Consumidor, utilizando `Streamlit`, `LLM` e `LangChain`.

- 📄 'mateusteixeiraramosdasilva_iagenerativaparalinguagem_pd.pdf': documento com as rspostas do PD.

- 📄'L9099.pdf': contendo a Lei dos Juizados Especiais (Lei n. 9.099/95) para teste de envio de documentos no aplicativo.

## Análise de dados com NER

⬆️ <a href='#índice'>Voltar ao início</a>

O projeto de Reconhecimento de Entidades Nomeadas (NER) teve como base o conjunto de dados da Folha UOL News Dataset, com foco nas notícias publicadas na seção “Mercado” durante o primeiro trimestre de 2015. 

Utilizando o modelo pré-treinado `monilouise/ner_pt_br`, as entidades foram extraídas por meio de um pipeline do Hugging Face Transformers, e posteriormente analisadas para identificar aquelas mais relevantes para o contexto econômico do período. O processo de extração foi cuidadosamente estruturado em etapas, desde a coleta e pré-processamento dos dados até a aplicação do modelo e consolidação dos resultados.

Com as entidades nomeadas obtidas, o projeto concentrou-se em isolar as organizações mencionadas nas notícias. Após diversos tratamentos de texto e limpezas semânticas, foi possível gerar um ranking das instituições mais citadas, entre as quais se destacaram HSBC, FGV e Apple. Além disso, visualizações gráficas — como gráficos de barras e nuvens de palavras — foram produzidas para tornar mais acessível a interpretação dos dados e reforçar visualmente os padrões encontrados no corpus analisado.

Como parte do relatório final, foram documentadas a metodologia adotada, as decisões de pré-processamento e os critérios utilizados na remoção de termos irrelevantes, como "Folha" e "Brasil", que não contribuíam para a análise específica de organizações. O projeto evidenciou o potencial de modelos NER aplicados a textos jornalísticos em português, servindo como base para aplicações futuras em análise de tendências, monitoramento de reputação e exploração de temas econômicos recorrentes na mídia nacional.

## Aplicativo de perguntas e respostas

⬆️ <a href='#índice'>Voltar ao início</a>

O projeto consistiu no desenvolvimento de uma aplicação de perguntas e respostas sobre o Direito do Consumidor. A interface foi construída com Streamlit e incluiu recursos como perguntas sugeridas, carregamento de arquivos adicionais, visualização das fontes utilizadas pelo modelo e exportação do histórico da conversa. O foco foi permitir que o usuário formulasse dúvidas e obtivesse respostas baseadas em conteúdos jurídicos relevantes.

A arquitetura utilizou LangChain para estruturar o agente responsável pelas respostas, integrando-o ao modelo da Groq. Os documentos de referência — como o Código de Defesa do Consumidor, o Código Civil e materiais complementares — foram carregados e organizados em uma base vetorial. A lógica de processamento ficou concentrada no arquivo agent.py, enquanto app.py definiu o fluxo e a interface da aplicação.

Nos testes realizados, o sistema respondeu perguntas relacionadas a procedimentos legais e prazos de forma adequada. Foi possível observar que, embora o modelo ofereça respostas coerentes a questões objetivas, ele não substitui a avaliação individualizada de um profissional do Direito. O uso do aplicativo reforça o papel dos modelos de linguagem como ferramentas auxiliares em contextos educativos e informativos.


## Conclusões Gerais

⬆️ <a href='#índice'>Voltar ao início</a>

Como conclusão geral, os projetos desenvolvidos ao longo da disciplina permitiram experimentar na prática o uso de modelos de linguagem em tarefas variadas, indo desde a análise de dados com reconhecimento de entidades até a criação de aplicações interativas com LLMs. 

Foi possível explorar fluxos de extração de informação, pré-processamento e visualização de resultados, além de estruturar agentes inteligentes com capacidade de consulta semântica e interação com o usuário.

Essas experiências demonstraram como ferramentas como LangChain, Streamlit e modelos hospedados via API podem ser combinadas para resolver problemas práticos e contextualizados. 

Ainda que existam limitações no uso de LLMs em domínios especializados como o jurídico, os resultados obtidos evidenciam o potencial dessas soluções para apoio educativo, organização de conhecimento e automação de consultas informacionais.


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