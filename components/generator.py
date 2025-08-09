import streamlit as st
from utils.generators import add_component_code
from utils.docs_links import DOCS

def render():
    st.markdown(
        """
        <style>
        .big-font { font-size: 1.2rem !important; }
        .gen-code-block .stCode { font-size: 1.15rem !important; }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown("### <span style='color:#e6a100' class='big-font'>⚡ Generator Configuration</span>", unsafe_allow_html=True)
    mode = st.radio("Mode", options=["Basic", "Advanced"], horizontal=True, key="generator_mode")
    errors = []
    code_valid = True

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Generator Name *", key="generator_name", placeholder="e.g., Gas_Plant_1, Wind_Farm_1")
        if not name:
            errors.append("Generator name is required")
            code_valid = False

        bus = st.text_input("Connected Bus *", key="generator_bus", placeholder="e.g., Bus_1")
        if not bus:
            errors.append("Bus connection is required")
            code_valid = False

        p_nom = st.number_input("Nominal Power (MW) *", key="generator_p_nom", min_value=0.0, placeholder="e.g., 500")
        if p_nom <= 0:
            errors.append("Nominal power must be greater than 0")
            code_valid = False

        carrier_type = st.selectbox("Carrier Type", ["Solar PV", "Wind", "Gas", "Coal", "Hydro", "Other"], key="generator_carrier_type")
        marginal_cost = st.number_input("Marginal Cost (€/MWh)", key="generator_marginal_cost", value=50.0)

    with col2:
        if mode == "Advanced":
            efficiency = st.number_input("Efficiency (0-1)", key="generator_efficiency", value=1.0, min_value=0.0, max_value=1.0)
            min_pu = st.number_input("Min Power (p.u.)", key="generator_min_pu", value=0.0, min_value=0.0, max_value=1.0)
            max_pu = st.number_input("Max Power (p.u.)", key="generator_max_pu", value=1.0, min_value=0.0, max_value=1.0)
            ramp_up = st.text_input("Ramp Up Limit (MW/h)", key="generator_ramp_up", placeholder="Optional")
            ramp_down = st.text_input("Ramp Down Limit (MW/h)", key="generator_ramp_down", placeholder="Optional")
        else:
            efficiency = 1.0
            min_pu = 0.0
            max_pu = 1.0
            ramp_up = ""
            ramp_down = ""

    st.caption("<span class='big-font'>💡 Tip: Generators inject power into the network. Set appropriate marginal costs for economic dispatch—renewables typically have very low costs (0–10 €/MWh), while conventional plants vary (30–100 €/MWh).</span>", unsafe_allow_html=True)

    # Validation bar & error listing
    if errors:
        st.error("  \n".join(errors))
        valid_status = f"{len(errors)}/3 Errors"
        st.markdown(f"<span style='color:#d0342c;font-weight:bold;' class='big-font'>❗ {valid_status}</span>", unsafe_allow_html=True)
    else:
        valid_status = "Valid"
        st.markdown(f"<span style='color:#3bd34c;font-weight:bold;' class='big-font'>✔ {valid_status}</span>", unsafe_allow_html=True)

    # Show code logic and code panel
    code = ""
    if st.button("Show Code", key="generator_show_code_btn", disabled=not code_valid):
        params = dict(
            name=name, bus=bus, carrier=carrier_type, p_nom=p_nom,
            marginal_cost=marginal_cost,
            efficiency=efficiency, min_pu=min_pu, max_pu=max_pu,
            ramp_up=ramp_up, ramp_down=ramp_down
        )
        code = add_component_code("Generator", params, mode)
        st.session_state["generator_code"] = code
    elif "generator_code" in st.session_state:
        code = st.session_state["generator_code"]

    # Generated code output
    if code and code_valid:
        st.markdown("#### Generated Code", unsafe_allow_html=True)
        st.code(code, language="python")
        st.info("📋 Use the copy icon in the code box above to copy your generated PyPSA code.")

    st.markdown(DOCS["Generator"])
