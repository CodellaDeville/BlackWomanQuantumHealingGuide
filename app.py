import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Quantum Healing Guide", layout="wide", initial_sidebar_state="expanded")
st.title("Quantum Healing Guide for Black Women")

st.markdown("""
<div style="font-size:1.2em; color:#e6f5e1; background:linear-gradient(135deg, #0d1e13 0%, #1e4632 100%); padding:1.5em; border-radius:1em; margin-bottom:2em;">
Welcome to your interactive Quantum Healing Guide. This guide blends science, sacred geometry, Afrofuturistic art, and practical tools for healing and empowerment.
</div>
""", unsafe_allow_html=True)

# Display HTML guide in an iframe
html_file = os.path.join(os.path.dirname(__file__), "index.html")
if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error("index.html not found. Please ensure your guide's main file is present.")

st.markdown("""
---
**PDF Export:** Use the export button in the guide to save your personalized PDF version.

**Note:** For best results, view this guide on a desktop or tablet for full interactivity and visual experience.
""")
