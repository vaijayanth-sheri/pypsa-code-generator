import streamlit as st
from utils.generators import add_component_code
from utils.docs_links import DOCS

def render():
    st.markdown(
        """
        <style>
        .big-font { font-size: 1.2rem !important; }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown("### <span class='big-font'>🔗 Line Configuration</span>", unsafe_allow_html=True)
    errors = []
    code_valid = True

    name = st.text_input("Line Name *", key="line_name", placeholder="e.g., Line01")
    if not name:
        errors.append("Line name is required")
        code_valid = False

    bus0 = st.text_input("From Bus *", key="line_bus0", placeholder="Source bus")
    if not bus0:
        errors.append("From Bus is required")
        code_valid = False

    bus1 = st.text_input("To Bus *", key="line_bus1", placeholder="Target bus")
    if not bus1:
        errors.append("To Bus is required")
        code_valid = False

    s_nom = st.number_input("Nominal Capacity (MW) *", key="line_s_nom", value=0.0)
    if s_nom <= 0:
        errors.append("Nominal capacity must be greater than 0")
        code_valid = False

    x = st.number_input("Reactance (p.u.)", key="line_x", value=0.01)
    r = st.number_input("Resistance (p.u.)", key="line_r", value=0.0)
    length = st.number_input("Length (km)", key="line_length", value=1.0)
    comment = st.text_input("Comment", key="line_comment", placeholder="Optional: add a description")

    if errors:
        st.error("  \n".join(errors))
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {len(errors)}/4 Errors</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ Valid</span>", unsafe_allow_html=True)

    code = ""
    if st.button("Show Code", key="line_show_code_btn", disabled=not code_valid):
        params = dict(
            name=name, bus0=bus0, bus1=bus1, s_nom=s_nom,
            x=x, r=r, length=length, comment=comment
        )
        code = add_component_code("Line", params, mode="Basic")
        st.session_state["line_code"] = code
    elif "line_code" in st.session_state:
        code = st.session_state["line_code"]

    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["Line"])
