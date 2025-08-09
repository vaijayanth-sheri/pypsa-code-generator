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
    st.markdown("### <span class='big-font'>🔄 Transformer Configuration</span>", unsafe_allow_html=True)
    errors = []
    code_valid = True

    name = st.text_input("Transformer Name *", key="transformer_name", placeholder="e.g., Tr01")
    if not name:
        errors.append("Transformer name is required")
        code_valid = False

    bus0 = st.text_input("High Voltage Bus *", key="transformer_bus0", placeholder="High voltage side")
    if not bus0:
        errors.append("High Voltage Bus is required")
        code_valid = False

    bus1 = st.text_input("Low Voltage Bus *", key="transformer_bus1", placeholder="Low voltage side")
    if not bus1:
        errors.append("Low Voltage Bus is required")
        code_valid = False

    s_nom = st.number_input("Nominal Capacity (MW) *", key="transformer_s_nom", value=0.0)
    if s_nom <= 0:
        errors.append("Nominal Capacity must be greater than 0")
        code_valid = False

    x = st.number_input("Reactance (p.u.)", key="transformer_x", value=0.01)
    r = st.number_input("Resistance (p.u.)", key="transformer_r", value=0.0)
    tap_ratio = st.number_input("Tap Ratio", key="transformer_tap_ratio", value=1.0)
    comment = st.text_input("Comment", key="transformer_comment", placeholder="Optional: add a description")

    if errors:
        st.error("  \n".join(errors))
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {len(errors)}/4 Errors</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ Valid</span>", unsafe_allow_html=True)

    code = ""
    if st.button("Show Code", key="transformer_show_code_btn", disabled=not code_valid):
        params = dict(
            name=name, bus0=bus0, bus1=bus1, s_nom=s_nom, x=x, r=r,
            tap_ratio=tap_ratio, comment=comment
        )
        code = add_component_code("Transformer", params, mode="Basic")
        st.session_state["transformer_code"] = code
    elif "transformer_code" in st.session_state:
        code = st.session_state["transformer_code"]

    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["Transformer"])
