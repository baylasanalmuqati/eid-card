import streamlit as st
import streamlit.components.v1 as components

# 1. Expand the page to full width and set title
st.set_page_config(
    page_title="بطاقة عيد مبارك", 
    page_icon="🌙", 
    layout="wide"
)

# 2. Hide Streamlit's default styling (header, footer, padding)
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    iframe {
        display: block;
        width: 100%;
        border: none;
    }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 3. Read and display your HTML
with open("eid-card-maker.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Using a high height (1000px) to ensure your card and controls are visible
components.html(html_content, height=1000, scrolling=False)
