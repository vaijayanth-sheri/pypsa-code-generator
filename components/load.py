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
    st.markdown("### <span class='big-font'>🔌 Load Configuration</span>", unsafe_allow_html=True)
    errors = []
    code_valid = True

    name = st.text_input("Load Name *", key="load_name", placeholder="e.g., Load0")
    if not name:
        errors.append("Load name is required")
        code_valid = False

    bus = st.text_input("Bus *", key="load_bus", placeholder="Name of the bus to connect this load")
    if not bus:
        errors.append("Bus is required")
        code_valid = False

    p_set = st.number_input("Active Power (MW) *", key="load_p_set", value=0.0)
    if p_set <= 0:
        errors.append("Active Power must be greater than 0")
        code_valid = False

    comment = st.text_input("Comment", key="load_comment", placeholder="Optional: add a description")

    if errors:
        st.error("  \n".join(errors))
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {len(errors)}/3 Errors</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ Valid</span>", unsafe_allow_html=True)

    code = ""
    if st.button("Show Code", key="load_show_code_btn", disabled=not code_valid):
        params = dict(name=name, bus=bus, p_set=p_set, comment=comment)
        code = add_component_code("Load", params, mode="Basic")
        st.session_state["load_code"] = code
    elif "load_code" in st.session_state:
        code = st.session_state["load_code"]

    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["Load"])
