import streamlit as st
import urllib.parse

## 🛠️ Streamlit Simulador de Navegador Móvel

st.set_page_config(layout="wide", page_title="Simulador de Navegador Móvel")

st.title("📱 Simulador de Navegador para Mobile")
st.markdown("""
    Este aplicativo usa um `<iframe>` para exibir um site.
    
    **Atenção:** Abrir o "F12" (Ferramentas do Desenvolvedor) diretamente de um **celular** dentro deste app **não é possível** diretamente pelo Streamlit, pois o Streamlit roda em um ambiente de servidor e o `<iframe>` é restrito.
    
    Para inspecionar o conteúdo abaixo como se estivesse no celular com F12, você precisará usar **Depuração Remota**:
    
    1.  **Abra este link no seu computador** (onde você roda o Streamlit ou um servidor de proxy) *em vez do celular*.
    2.  Use as Ferramentas do Desenvolvedor do seu **navegador desktop** (F12/Ctrl+Shift+I) e use a opção de **alternar a visualização móvel/tablet** (geralmente um ícone de celular/tablet).
""")

# --- Entrada da URL ---
default_url = "https://streamlit.io/"
url_input = st.text_input(
    "Insira a URL a ser visualizada:",
    value=default_url,
    help="Exemplo: https://www.google.com ou https://docs.python.org/"
)

# --- Validação e Preparação da URL ---
if url_input:
    # Garante que a URL tenha um esquema (http/https) para o iframe
    parsed_url = urllib.parse.urlparse(url_input)
    if not parsed_url.scheme:
        # Assume https se não houver esquema
        safe_url = "https://" + url_input
    else:
        safe_url = url_input
    
    # --- Exibição no Iframe ---
    st.subheader(f"Visualizando: {safe_url}")
    
    # Estilos para simular um dispositivo móvel (ajustando a largura/altura)
    # Ajuste os pixels (e.g., 375px de largura por 812px de altura para um iPhone X/11/12/13)
    iframe_style = f"""
        border: 10px solid black; 
        border-radius: 25px;
        width: 375px;
        height: 812px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    """

    # O elemento 'srcdoc' não é apropriado para URLs externas, usamos 'src'
    # srcdoc é apenas para conteúdo estático passado diretamente no código.
    
    st.markdown(f'<iframe src="{safe_url}" style="{iframe_style}"></iframe>', unsafe_allow_html=True)
    
    st.warning("Para **inspecionar** este conteúdo como no F12, abra o aplicativo em um **computador** e use as ferramentas do seu navegador desktop (F12) com a **visualização móvel ativada**.")

else:
    st.info("Por favor, insira uma URL para começar a navegação simulada.")
