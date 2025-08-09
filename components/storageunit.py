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
    st.markdown("### <span class='big-font'>🔋 StorageUnit Configuration</span>", unsafe_allow_html=True)
    errors = []
    code_valid = True

    name = st.text_input("Storage Name *", key="storageunit_name", placeholder="e.g., Battery1")
    if not name:
        errors.append("Storage name is required")
        code_valid = False

    bus = st.text_input("Bus *", key="storageunit_bus", placeholder="Name of the bus to connect this storage")
    if not bus:
        errors.append("Bus is required")
        code_valid = False

    carrier = st.text_input("Carrier", key="storageunit_carrier", value="electricity", placeholder="e.g., electricity")
    p_nom = st.number_input("Power (MW) *", key="storageunit_p_nom", value=0.0)
    if p_nom <= 0:
        errors.append("Power must be greater than 0")
        code_valid = False

    max_hours = st.number_input("Max Hours", key="storageunit_max_hours", value=4.0)
    efficiency_store = st.number_input("Efficiency (Store)", key="storageunit_eff_store", value=0.9, min_value=0.0, max_value=1.0)
    efficiency_dispatch = st.number_input("Efficiency (Dispatch)", key="storageunit_eff_dispatch", value=0.9, min_value=0.0, max_value=1.0)
    cyclic_state_of_charge = st.checkbox("Cyclic State of Charge", key="storageunit_cyclic_soc", value=True)
    comment = st.text_input("Comment", key="storageunit_comment", placeholder="Optional: add a description")

    if errors:
        st.error("  \n".join(errors))
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {len(errors)}/3 Errors</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ Valid</span>", unsafe_allow_html=True)

    code = ""
    if st.button("Show Code", key="storageunit_show_code_btn", disabled=not code_valid):
        params = dict(
            name=name, bus=bus, carrier=carrier, p_nom=p_nom,
            max_hours=max_hours, efficiency_store=efficiency_store,
            efficiency_dispatch=efficiency_dispatch,
            cyclic_state_of_charge=cyclic_state_of_charge,
            comment=comment
        )
        code = add_component_code("StorageUnit", params, mode="Basic")
        st.session_state["storageunit_code"] = code
    elif "storageunit_code" in st.session_state:
        code = st.session_state["storageunit_code"]

    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["StorageUnit"])
