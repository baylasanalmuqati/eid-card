import streamlit as st
import streamlit.components.v1 as components

# Set page title and favicon
st.set_page_config(page_title="Eid Card Maker", page_icon="🌙")

# Read the HTML file
with open("eid-card-maker.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML component
# We use a height that fits your card design well
components.html(html_content, height=900, scrolling=True)
