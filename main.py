import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    layout="wide", 
    page_title="Monitor de Preços"
)

st.markdown(
    """
    <style>
    [data-testid="stHeader"] {
            visibility: hidden;
            height: 0%;
        }
        .block-container { padding-top: 0rem; }
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

FATOR_ZOOM = 0.5

LARGURA_BASE_PIXELS = "150%" # Tamanho base para o conteúdo caber
ALTURA_BASE_PIXELS = 1000  # Tamanho base para o conteúdo caber

BUFFER_ALTURA_STREAMLIT = 30 # Espaço extra para a rolagem do componente

# Calcula a altura final do componente Streamlit (altura base escalada + buffer)
ALTURA_FINAL_STREAMLIT = int(ALTURA_BASE_PIXELS * FATOR_ZOOM) + BUFFER_ALTURA_STREAMLIT

# --- ESTRUTURA DE DADOS UTILIZADA (LISTA DE TUPLAS) ---
# A tupla é: (Preço, Link)
precos_e_links = [
    ("R$ 31,72", "https://www.centauro.com.br/bermuda-masculina-oxer-ls-basic-new-984889.html?cor=04"),
    ("R$ 53,99", "https://www.centauro.com.br/bermuda-masculina-oxer-mesh-mescla-983436.html?cor=MS"),
    ("R$ 31,49", "https://www.centauro.com.br/calcao-masculino-adams-liso-978059.html?cor=02"), # Não há conflito aqui
    ("R$ 1794", "https://shopee.com.br/Xiaomi-Poco-X7-Pro-512GB-256GB-12-Ram-5G-Vers%C3%A3o-Global-NFC-Original-Lacrado-e-Envio-Imediato-ADS-i.1351433975.20698075298"), # Corrigido abaixo
]
# --- FIM DA ESTRUTURA ---

# Título principal diminuído (usando h2 em vez de h1)
st.markdown("<h6>🔎 Monitor de Preço</h6>", unsafe_allow_html=True)

# Iteramos sobre a lista de tuplas: (Preço, Link)
for i, (preco_desejado, link_produto) in enumerate(precos_e_links):
    
    # CORREÇÃO APLICADA AQUI:
    # Se o link for da Shopee, adicionamos o parâmetro para forçar a visualização na web
    if "shopee.com.br" in link_produto:
        # Como o seu link da Shopee não tem '?', podemos adicionar o parâmetro diretamente
        link_produto += "?is_from_app=false" 
        
    nome_produto = f"{i + 1}" # Número de ordem
    
    # Exibição: O preço (primeiro elemento da tupla) é exibido em destaque e o link é oculto no texto "Acessar Produto"
    st.markdown(f"""
    <div style="display: flex; align-items: baseline; gap: 15px; margin-bottom: -10px;">
        <h2 style="margin-bottom: 0;">{nome_produto})</h2>
        <p style="margin-bottom: 0; font-size: 1.2em; font-weight: bold; color: green;">
            {preco_desejado}  </p>
        <p style="margin-bottom: 0; font-size: 0.8em; max-width: 600px; overflow-wrap: break-word;">
            <a href="{link_produto}" target="_blank">Acessar Produto</a> </p>
    </div>
    """, unsafe_allow_html=True)
    
    html_content = f"""
    <iframe 
        src="{link_produto}" 
        width="{LARGURA_BASE_PIXELS}px" 
        height="{ALTURA_BASE_PIXELS}px"
        style="
            border: 1px solid #ddd; /* Borda mais suave */
            transform: scale({FATOR_ZOOM}); 
            transform-origin: top left;
            margin-top: 5px; 
        " 
    ></iframe>
    """

    # Exibe o componente HTML/iFrame
    st.components.v1.html(html_content, height=ALTURA_FINAL_STREAMLIT)
    
    # SEPARADOR VISUAL entre os produtos
    st.markdown("---")
