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
    st.markdown("### <span class='big-font'>🔀 Link Configuration</span>", unsafe_allow_html=True)
    errors = []
    code_valid = True

    name = st.text_input("Link Name *", key="link_name", placeholder="e.g., Link01")
    if not name:
        errors.append("Link name is required")
        code_valid = False

    bus0 = st.text_input("From Bus *", key="link_bus0", placeholder="Source bus")
    if not bus0:
        errors.append("From Bus is required")
        code_valid = False

    bus1 = st.text_input("To Bus *", key="link_bus1", placeholder="Target bus")
    if not bus1:
        errors.append("To Bus is required")
        code_valid = False

    carrier = st.text_input("Carrier", key="link_carrier", value="electricity", placeholder="e.g., electricity")
    p_nom = st.number_input("Nominal Power (MW) *", key="link_p_nom", value=0.0)
    if p_nom <= 0:
        errors.append("Nominal Power must be greater than 0")
        code_valid = False

    efficiency = st.number_input("Efficiency", key="link_efficiency", value=0.9, min_value=0.0, max_value=1.0)
    marginal_cost = st.number_input("Marginal Cost (€/MWh)", key="link_marginal_cost", value=0.0)
    comment = st.text_input("Comment", key="link_comment", placeholder="Optional: add a description")

    if errors:
        st.error("  \n".join(errors))
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {len(errors)}/4 Errors</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ Valid</span>", unsafe_allow_html=True)

    code = ""
    if st.button("Show Code", key="link_show_code_btn", disabled=not code_valid):
        params = dict(
            name=name, bus0=bus0, bus1=bus1, carrier=carrier,
            p_nom=p_nom, efficiency=efficiency, marginal_cost=marginal_cost,
            comment=comment
        )
        code = add_component_code("Link", params, mode="Basic")
        st.session_state["link_code"] = code
    elif "link_code" in st.session_state:
        code = st.session_state["link_code"]

    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["Link"])
