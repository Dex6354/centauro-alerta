import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    layout="wide", 
    page_title="Monitor de Preços - Embed Centauro"
)

# Dimensões para a visualização (ajuste conforme necessário)
ALTURA_IFRAME = 500  # Altura em pixels para a visualização
LARGURA_IFRAME = "100%" # Largura total da coluna
BUFFER_ALTURA_STREAMLIT = 30 # Buffer para acomodar títulos/espaçamento no Streamlit

# Lista contendo APENAS as URLs dos produtos que você deseja monitorar.
lista_de_urls = [
    "https://www.centauro.com.br/bermuda-masculina-oxer-ls-basic-new-984889.html?cor=04",
    "https://www.centauro.com.br/bermuda-masculina-oxer-mesh-mescla-983436.html?cor=MS",
]

st.title("Monitor de Preços")

# Usamos enumerate para obter o índice (i) e a URL (link_produto)
for i, link_produto in enumerate(lista_de_urls):
    
    # Define um título baseado no índice (Ex: Produto 1, Produto 2, etc.)
    nome_produto = f"Produto Monitorado #{i + 1}" 
    
    st.header(nome_produto)
    
    # Exibe o link original
    st.markdown(f"**Link Original:** [{link_produto}]({link_produto})", unsafe_allow_html=True)

    # Criação do conteúdo HTML para o iFrame
    html_content = f'<iframe src="{link_produto}" width="{LARGURA_IFRAME}" height="{ALTURA_IFRAME}px"></iframe>'

    # Exibe o componente HTML/iFrame
    st.components.v1.html(html_content, height=ALTURA_IFRAME + BUFFER_ALTURA_STREAMLIT)
    
    # SEPARADOR VISUAL entre os produtos
    st.markdown("---")
