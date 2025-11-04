import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    layout="wide", 
    page_title="Monitor de Preços - Embed Centauro"
)

# 1. CONFIGURAÇÃO DE ESTILO: Oculta o cabeçalho e ajusta o padding superior
st.markdown(
    """
    <style>
        /* Oculta o cabeçalho padrão do Streamlit */
        [data-testid="stHeader"] {
            visibility: hidden;
            height: 0%;
        }
        
        /* Remove o padding superior padrão do corpo da aplicação Streamlit */
        .stApp {
            padding-top: 0px !important; 
        }

        /* ESTILO PARA O TÍTULO PRINCIPAL (menor e sem margem superior) */
        #titulo-principal {
            margin-top: 0px !important;
            padding-top: 15px !important; /* Pequeno padding superior para melhor visual */
            padding-bottom: 10px !important;
            margin-bottom: 10px !important; /* Separação do conteúdo abaixo */
            font-size: 2em !important; /* Reduzindo o tamanho da fonte do H1 (Era ~2.5em/3em padrão) */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 2. INSERÇÃO DO TÍTULO NO TOPO DA PÁGINA (ele rolará junto)
st.markdown(
    '<h1 id="titulo-principal">Monitor de Preços</h1>',
    unsafe_allow_html=True
)


FATOR_ZOOM = 0.5

LARGURA_BASE_PIXELS = "150%" 
ALTURA_BASE_PIXELS = 1000

BUFFER_ALTURA_STREAMLIT = 30 

ALTURA_FINAL_STREAMLIT = int(ALTURA_BASE_PIXELS * FATOR_ZOOM) + BUFFER_ALTURA_STREAMLIT

lista_de_urls = [
    "https://www.centauro.com.br/bermuda-masculina-oxer-ls-basic-new-984889.html?cor=04",
    "https://www.centauro.com.br/bermuda-masculina-oxer-mesh-mescla-983436.html?cor=MS",
]

# Usamos enumerate para obter o índice (i) e a URL (link_produto)
for i, link_produto in enumerate(lista_de_urls):
    
    nome_produto = f"#{i + 1}" 
    
    # Header para cada produto
    st.markdown(f"""
    <div style="display: flex; align-items: baseline; gap: 15px; margin-top: 20px; margin-bottom: -10px;">
        <h2 style="margin-bottom: 0;">{nome_produto}</h2>
        <p style="margin-bottom: 0;"><strong>Link Original:</strong> <a href="{link_produto}" target="_blank">{link_produto}</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    html_content = f"""
    <iframe 
        src="{link_produto}" 
        width="{LARGURA_BASE_PIXELS}px" 
        height="{ALTURA_BASE_PIXELS}px"
        style="
            border: 1px solid #ccc; 
            transform: scale({FATOR_ZOOM}); 
            transform-origin: top left;
            margin-top: 20px;
        " 
    ></iframe>
    """

    st.components.v1.html(html_content, height=ALTURA_FINAL_STREAMLIT)
    
    # SEPARADOR VISUAL entre os produtos
    st.markdown("---")
