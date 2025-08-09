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
    st.markdown("### <span class='big-font'>🚌 Bus Configuration</span>", unsafe_allow_html=True)
    errors = []
    code_valid = True

    name = st.text_input("Bus Name *", key="bus_name", placeholder="e.g., Bus0")
    if not name:
        errors.append("Bus name is required")
        code_valid = False

    carrier = st.text_input("Carrier", key="bus_carrier", value="electricity", placeholder="e.g., electricity/heat/gas")
    v_nom = st.number_input("Nominal Voltage (kV)", key="bus_v_nom", min_value=0.0, value=110.0)
    comment = st.text_input("Comment", key="bus_comment", placeholder="Optional: add a description")

    if errors:
        st.error("  \n".join(errors))
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {len(errors)}/1 Errors</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ Valid</span>", unsafe_allow_html=True)

    code = ""
    if st.button("Show Code", key="bus_show_code_btn", disabled=not code_valid):
        params = dict(name=name, carrier=carrier, v_nom=v_nom, comment=comment)
        code = add_component_code("Bus", params, mode="Basic")
        st.session_state["bus_code"] = code
    elif "bus_code" in st.session_state:
        code = st.session_state["bus_code"]

    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["Bus"])
