import streamlit as st
from streamlit.components.v1 import html

# 🔧 CONFIGURAÇÃO INICIAL
st.set_page_config(
    layout="wide",
    page_title="Monitor de Preços - Embed Centauro"
)

# 🎨 CSS para SOBREPOR o cabeçalho e FIXAR o título no topo
st.markdown("""
<style>
/* Oculta ou reduz o cabeçalho padrão do Streamlit */
[data-testid="stHeader"] {
    visibility: hidden !important;
    height: 0px !important;
}

/* Remove padding automático do corpo da aplicação */
.stApp {
    padding-top: 0px !important;
}

/* 🔝 Força o título no topo absoluto da tela */
#titulo-principal {
    position: fixed;       /* Fixa no topo */
    top: 0;                /* Alinha no topo */
    left: 0;
    width: 100%;
    background-color: white;  /* Fundo branco para sobrepor o cabeçalho */
    z-index: 9999;         /* Sobrepõe tudo (inclusive o cabeçalho Streamlit) */
    text-align: center;
    padding: 10px 0;
    margin: 0;
    border-bottom: 2px solid #eee;
    font-size: 2rem;
}

/* Adiciona margem no corpo para evitar que o conteúdo fique escondido sob o título fixo */
body, .stApp {
    margin-top: 70px !important;  /* Ajuste conforme altura do título */
}

/* Ajuste visual dos containers de produtos */
.produto-header-container {
    margin-top: 10px;
    margin-bottom: -10px;
}
</style>
""", unsafe_allow_html=True)

# 🏷️ TÍTULO PRINCIPAL
st.markdown('<h1 id="titulo-principal">🛒 Monitor de Preços</h1>', unsafe_allow_html=True)

# ⚙️ CONFIGURAÇÕES DE ZOOM E DIMENSÕES
FATOR_ZOOM = 0.5
LARGURA_BASE_PIXELS = "150%"
ALTURA_BASE_PIXELS = 1000
BUFFER_ALTURA_STREAMLIT = 30
ALTURA_FINAL_STREAMLIT = int(ALTURA_BASE_PIXELS * FATOR_ZOOM) + BUFFER_ALTURA_STREAMLIT

# 🌐 LISTA DE PRODUTOS
lista_de_urls = [
    "https://www.centauro.com.br/bermuda-masculina-oxer-ls-basic-new-984889.html?cor=04",
    "https://www.centauro.com.br/bermuda-masculina-oxer-mesh-mescla-983436.html?cor=MS",
]

# 🔁 LOOP DE RENDERIZAÇÃO
for i, link_produto in enumerate(lista_de_urls):
    nome_produto = f"#{i + 1}"

    st.markdown(f"""
    <div class="produto-header-container" style="display: flex; align-items: baseline; gap: 15px;">
        <h2 style="margin-bottom: 0;">{nome_produto}</h2>
        <p style="margin-bottom: 0;"><strong>Link Original:</strong> 
            <a href="{link_produto}" target="_blank">{link_produto}</a>
        </p>
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

    st.markdown("---")
