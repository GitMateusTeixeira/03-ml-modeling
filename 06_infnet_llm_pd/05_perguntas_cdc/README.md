# Projeto de Disciplina de Inteligência Artificial generativa para linguagem (Large Language Model) [25E2_3]

<img style='width:350px' src='./assets/logo_infnetv2.png' alt='Infnet logo' align='left'>
<br>
Projeto desenvolvido na disciplina de LLM para Aplicações Práticas em IA, com foco na criação de um sistema de perguntas e respostas sobre o Direito do Consumidor utilizando Streamlit, LangChain e modelos de linguagem generativa.

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

Este projeto foi desenvolvido no contexto da disciplina de Inteligência Artificial Generativa para Linguagem (Large Language Model), e visa demonstrar a aplicação de modelos de linguagem em ambientes interativos voltados à consulta jurídica. A proposta consistiu na construção de um aplicativo de perguntas e respostas sobre o Direito do Consumidor, utilizando Streamlit para interface, LangChain para orquestração do agente e modelos LLM hospedados via API. A aplicação permite realizar consultas sobre temas jurídicos, carregar arquivos complementares e acompanhar as fontes das respostas geradas pelo sistema.

## Tecnologias

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg' alt='Anaconda logo'> Anaconda v. 23.7.4

<img style='width:30px; vertical-align: middle; margin-right: 10px;' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg' alt='Jupyter logo'> Jupyter Notebook v. 5.7.2

<img style='width:30px; vertical-align: middle; margin-right: 10px' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' alt='Python logo'> Python v. 3.10.18

Principais bibliotecas:

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="./assets/general_lib.png" alt='fitz_logo'>Fitz

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg" alt='json_logo'>Json

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/langchain-ipuhh4qo1jz5ssl4x0g2a.png/langchain-dp1uxj2zn3752pntqnpfu2.png?_a=DATAdtAAZAA0" alt='langchain_logo'>Langchain

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" alt='numpy_logo'> Numpy 1.26.4

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='pandas_logo'> Pandas 2.2.3

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="./assets/general_lib.png" alt='pypdf2_logo'>PyPDF2

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pypi/pypi-original.svg"/> Pypi pip-tools

- <img style='width:30px; vertical-align: middle; margin-right: 10px'  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg" /> Streamlit 1.44.1

- <img style='width:30px; vertical-align: middle; margin-right: 10px' src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/yaml/yaml-original.svg" alt='yaml_logo'>Yaml


## Configuração inicial

⬆️ <a href='#índice'>Voltar ao início</a>

O projeto foi realizado no ambiente virtual '🌐 env_25E2_3_v1, instalado pelo Anconda.

Para garantir a instalação eficiente das dependências, utilizamos o pip-tools, uma ferramenta que permite gerenciar pacotes de forma controlada e reproduzível. Foi feita a compilação do arquivo '📄 requirements.in' com o comando `pip-compile requirements.in` e para a instalação dos pacotes, recomenda-se a utilização do comenado `pip install -r requirements.txt --user` para evitar erros de permissões.


## Fluxograma do projeto

O projeto segue o seguinte fluxograma (vamos mostrar por partes):

### Parte 01. Preparação e configuração

⬆️ <a href='#índice'>Voltar ao início</a>

O ambiente é preparado com os arquivos `config.yaml` e `requirements.txt`, onde são definidos o modelo Groq (LLM) e os pacotes necessários. A base legal é carregada a partir de arquivos do Código de Defesa do Consumidor, Código Civil e artigos complementares.


### Parte 02. Construção do agente com LangChain

⬆️ <a href='#índice'>Voltar ao início</a>

No arquivo `agent.py`, os documentos são transformados em embeddings e armazenados em uma base vetorial com FAISS. Um agente é criado utilizando ferramentas da LangChain, capaz de recuperar informações e responder consultas a partir do conteúdo carregado.


### Parte 03.  Interface com o usuário via Streamlit

⬆️ <a href='#índice'>Voltar ao início</a>

O `app.py` cria a interface com o usuário. A sidebar permite escolher perguntas-modelo, visualizar fontes, anexar arquivos adicionais e exportar o histórico. O usuário interage diretamente com o modelo enviando perguntas que são processadas em tempo real.


### Parte 04. Geração de resposta

⬆️ <a href='#índice'>Voltar ao início</a>

A pergunta é interpretada pelo agente, que busca os documentos mais relevantes na base vetorial e envia o prompt com contexto para o modelo da `Groq`. A resposta gerada é exibida ao usuário, junto com as fontes utilizadas para fundamentar a resposta.


## Conclusões Gerais

⬆️ <a href='#índice'>Voltar ao início</a>

O projeto demonstrou como modelos de linguagem podem ser utilizados em sistemas de perguntas e respostas em domínios específicos, como o Direito do Consumidor. 

A integração entre Streamlit, LangChain e LLMs permitiu construir uma aplicação funcional, capaz de recuperar informações jurídicas relevantes e apresentar respostas com base em documentos previamente carregados.

A experiência também evidenciou as possibilidades e limites dessas ferramentas. O sistema apresentou bons resultados em perguntas objetivas, mas exige cautela quanto à interpretação de situações mais complexas. Ainda assim, mostrou potencial como recurso complementar para fins educativos, organização de conteúdos jurídicos e apoio à consulta de informações normativas.


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