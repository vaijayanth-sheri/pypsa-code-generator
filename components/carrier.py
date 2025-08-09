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
    st.markdown("### <span class='big-font'>🛤 Carrier Configuration</span>", unsafe_allow_html=True)
    errors = []
    code_valid = True

    name = st.text_input("Carrier Name *", key="carrier_name", value="electricity", placeholder="Unique carrier name")
    if not name:
        errors.append("Carrier name is required")
        code_valid = False

    co2_emissions = st.number_input("CO₂ Emissions (t/MWh)", key="carrier_co2", value=0.0)
    comment = st.text_input("Comment", key="carrier_comment", placeholder="Optional: add a description")

    if errors:
        st.error("  \n".join(errors))
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {len(errors)}/1 Errors</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ Valid</span>", unsafe_allow_html=True)

    code = ""
    if st.button("Show Code", key="carrier_show_code_btn", disabled=not code_valid):
        params = dict(name=name, co2_emissions=co2_emissions, comment=comment)
        code = add_component_code("Carrier", params, mode="Basic")
        st.session_state["carrier_code"] = code
    elif "carrier_code" in st.session_state:
        code = st.session_state["carrier_code"]

    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["Carrier"])
