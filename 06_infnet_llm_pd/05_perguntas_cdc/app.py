"""

=================================================================================
# Aplicativo de perguntas e respostas sobre Direito do Consumidor via Streamlit #
=================================================================================

Funcionalidades:
- lê o Código Civil, o Código de Defesa do Consumidor e uma revista pública com artigos acadêmicos sobre o tema
- perguntas-modelo para testar a funcionalidade
- possibilidade de enviar um arquivo acessório para fazer perguntas específicas

"""


import streamlit as st
import os
import pandas as pd
import json
from PyPDF2 import PdfReader
from langchain.docstore.document import Document
from agent import gerar_resposta, base_vetorial

# 1. inicializar sessão
if "chat_historico" not in st.session_state:
    st.session_state["chat_historico"] = []

if "pergunta_exemplo" not in st.session_state:
    st.session_state["pergunta_exemplo"] = None

# 2. funções auxiliares

# 2.1. função de upar arquivos
def carregar_texto_pdf(uploaded_pdf):
    reader = PdfReader(uploaded_pdf)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text() or ""
    return texto

def carregar_texto_csv(uploaded_csv):
    df = pd.read_csv(uploaded_csv)
    return df.to_string()

def carregar_texto_excel(uploaded_excel):
    df = pd.read_excel(uploaded_excel)
    return df.to_string()

# 2.2. função de exportar a conversa
def exportar_historico_txt(historico):
    return "\n".join(f"{role.upper()}: {msg}" for role, msg in historico)

def exportar_historico_json(historico):
    return json.dumps(historico, indent=2, ensure_ascii=False)

# 2.3. função de exibir o histórico
def exibir_conversa():
    for role, msg in st.session_state["chat_historico"]:
        with st.chat_message(role):
            st.markdown(msg)


# 3. utilidades da sidebar

# 3.1. apresentação
st.sidebar.title("⚖️ Specter – Assistente Jurídico")

# 3.2. temas sugeridos
st.sidebar.markdown("""
Converse com o **Specter**, assistente de IA especializado em Direito do Consummidor.

➡️ Temas sugeridos:
- Direito de arrependimento
- Responsabilidade pelo produto
- Publicidade enganosa
- Garantia e assistência técnica
""")

# 3.3. exemplos de perguntas-modelo
with st.sidebar.expander("📝 Conceitos Básicos", expanded=False):
    st.markdown("Exemplos sobre conceitos fundamentais sobre o Direito do Consumidor.")

    if st.button("Direitos básicos do consumidor"):
        st.session_state["pergunta_exemplo"] = "Quais são os direitos básicos do consumidor, como o direito à informação, ao arrependimento, à proteção contra práticas abusivas, etc.?"

    if st.button("Publicidade enganosa"):
        st.session_state["pergunta_exemplo"] = "O que caracteriza uma publicidade enganosa?"

    if st.button("Prazos de garantia"):
        st.session_state["pergunta_exemplo"] = "Quais são os prazos de garantia para os produtos e serviços e quais são as implicações para o consumidor?"

with st.sidebar.expander("❔Principais dúvidas", expanded=False):
    st.markdown("Principais perguntas sobre o Direito do Consumidor.")

    if st.button("Direito de arrependimento"):
        st.session_state["pergunta_exemplo"] = "Como funciona o Direito de arrependimento?"
    
    if st.button("Desistência de contrato"):
        st.session_state["pergunta_exemplo"] = "Quais são as condições para o consumidor desistir de um contrato e quais são as consequências para o fornecedor?"

    if st.button("Direito de informação"):
        st.session_state["pergunta_exemplo"] = "Quais são os direitos do consumidor em relação à informação sobre os produtos e serviços e quais são as obrigações dos fornecedores em relação à transparência?"

    if st.button("Consumidor vulnerável"):
        st.session_state["pergunta_exemplo"] = "Quais são as proteções específicas para os consumidores vulneráveis, como idosos, crianças e pessoas com deficiência?"

# 3.4. exibir as fontes que o modelo está usando
with st.sidebar.expander("📕 Fontes e Estudo", expanded=False):
    st.markdown("Entenda de onde vem o conhecimento do assistente.")

    if st.button("Fontes de dados"):
        st.session_state["pergunta_exemplo"] = "Quais as fontes de dados que utiliza para responder?"

# 3.5. enviar um arquivo acesssório
st.sidebar.markdown("### 📎 Adicionar Documento")
TIPOS_SUPORTADOS = {
    "application/pdf": carregar_texto_pdf,
    "text/csv": carregar_texto_csv,
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": carregar_texto_excel,
    "application/vnd.ms-excel": carregar_texto_excel,
}

uploaded_file = st.sidebar.file_uploader("Envie um arquivo (PDF, CSV, Excel)", type=["pdf", "csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.type in TIPOS_SUPORTADOS:
            texto = TIPOS_SUPORTADOS[uploaded_file.type](uploaded_file)

            if texto.strip():
                base_vetorial.add_documents([Document(page_content=texto)])
                st.sidebar.success("✅ Documento adicionado à base de conhecimento.")

            else:
                st.sidebar.warning("⚠️ Hm.. não consegui seu arquivo contém dados que eu não consigo ler. Tente adicionar outro.")

        else:
            st.sidebar.error("❌ Formato de arquivo não suportado.")

    except Exception as e:
        st.sidebar.error(f"❌ Erro ao processar o arquivo: {e}")

# 3.6. exportar o histórico de conversa
with st.sidebar.expander("💬 Exportar Histórico"):
    if st.button("⬇️ Exportar no formato .txt"):
        txt = exportar_historico_txt(st.session_state["chat_historico"])
        st.download_button("Baixar .txt", txt, file_name="chat_irineu.txt")

    if st.button("⬇️ Exportar no formato .json"):
        js = exportar_historico_json(st.session_state["chat_historico"])
        st.download_button("Baixar .json", js, file_name="chat_irineu.json")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, 'assets', 'logo_mt_ds.png')

# 3.7. seção de Autoria
st.sidebar.markdown("Feito por")
st.sidebar.image(str(image_path), width=100)
st.sidebar.markdown("""
**Mateus Teixeira**  
Cientista de Dados  
Pós-graduando em Inteligência Artificial pela INFNET

<a href="mailto:pessoal.mtr@gmail.com" target="_blank">
    <img 
        src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&labelColor=555&logoColor=white" 
        alt="E-mail" 
        height='25'/>
</a>
<a href="https://www.linkedin.com/in/mateusteixeira/" target="_blank">
    <img 
        src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&labelColor=555&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAABNklEQVR4nO3XSUoDQRgG0NrFTRyiuBA8lARvIujanROKnigICh5AVASHkDPECZ60yULFVDqamEqoB73rGj6q6q/uELIsmz6o4QgPeEUTx1gMEzL5Kz+7xnxIGQ7F7YWU6WybmNuQMrz0CfAcUobHPgHuQ8p0qk/MfpiAKnTTY/KXyVehApZw0q3/xT1whwMsfLyQZVNMCcNohxVsoNEt3U9o4RRbWE0yACrYLnFhtrGLmWQCYA4XBnOO5VQCnA04+c/tKikE+IudSQ/QLnWwEw5Q2EwhQFEy66h2n7XIH+B3jXEHKCZf6/EB2SzRvjXuAPXIuOsl2r+NO0A1Mu7sb8f+twCjGvuLHCAi9GEIfeQViMkrIG+hjlEdQEPoIx/imLwC8hbqyIe4ByWEUXWSTIAsy8JEeQd/X93eUJrQcwAAAABJRU5ErkJggg==" 
        alt="LinkedIn" 
        height='25'/>
</a>
<a href="https://www.instagram.com/omateusteixeira" target="_blank">
    <img 
        src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&labelColor=555&logoColor=white" 
        alt="Instagram" 
        height='25'/>
</a>
""", unsafe_allow_html=True)


# 4. título principal

# 4.1. apresentação
st.title("Specter - Assistente Inteligente Jurídico (AIJ)")
st.markdown("Converse com o assistente de IA sobre **temas jurídicos**, com base em documentos técnicos confiáveis.")

# 4.2. iniciar uma nova conversa=
if st.button("🔄 Nova Conversa"):
    st.session_state["chat_historico"] = []
    st.session_state["pergunta_exemplo"] = None
    st.success("✅ Nova conversa iniciada.")


# 5. entrada do usuário
entrada_usuario = st.chat_input("Digite sua dúvida jurídica aqui...")
pergunta = entrada_usuario or st.session_state["pergunta_exemplo"]


# 6. processar um nova pergunta considerando o histórico
if pergunta and (
    len(st.session_state["chat_historico"]) == 0 or
    st.session_state["chat_historico"][-1] != ("user", pergunta)
):
    st.session_state["chat_historico"].append(("user", pergunta))
    historico_formatado = [
        f"{'Usuário' if role == 'user' else 'Assistente'}: {msg}"
        for role, msg in st.session_state["chat_historico"]
    ]
    try:
        resposta = gerar_resposta(pergunta, historico_formatado)
        st.session_state["chat_historico"].append(("assistant", resposta))
    except Exception as e:
        st.session_state["chat_historico"].append(("assistant", f"Erro ao gerar resposta: {e}"))
    st.session_state["pergunta_exemplo"] = None


# 7. renderizar o histórico do chat
exibir_conversa()