import streamlit as st
from components import (
    bus, load, generator, storageunit, line, link, transformer, carrier
)
from utils.validators import get_system_warnings

st.set_page_config(page_title="PyPSA Code Generator", layout="wide")

st.markdown(
    """
    <style>
    .big-font { font-size: 1.3rem !important; }
    </style>
    """, unsafe_allow_html=True
)
st.markdown(
    """
    <h2 class='big-font'>⚡ PyPSA Component Builder</h2>
    <p style="font-size:1.13rem;color:#555;">Configure your PyPSA energy system components below. Each tab lets you create and preview code for one component at a time. Copy your results directly from the code block.</p>
    """,
    unsafe_allow_html=True,
)

COMPONENT_TABS = {
    "Bus": bus,
    "Load": load,
    "Generator": generator,
    "StorageUnit": storageunit,
    "Line": line,
    "Link": link,
    "Transformer": transformer,
    "Carrier": carrier,
}

tab_names = list(COMPONENT_TABS.keys())
tabs = st.tabs(tab_names)

for i, tab in enumerate(tabs):
    with tab:
        COMPONENT_TABS[tab_names[i]].render()

# Optional: Top-level system validation (expand as needed)
warnings = get_system_warnings()
if warnings:
    st.warning("  \n".join(warnings))

st.markdown(
    """
    <hr>
    <p style="color:#999;">Developed with ❤️ for PyPSA community. | <a href="https://pypsa.readthedocs.io/en/stable/" target="_blank">PyPSA Documentation</a></p>
    """,
    unsafe_allow_html=True
)
