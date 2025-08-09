import jinja2
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', 'templates')

def add_component_code(component, params, mode="Basic"):
    params["mode"] = mode  # Ensure mode is present for template rendering
    filename = f"{component.lower()}_template.j2"
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template(filename)
    code = template.render(**params)
    return code

def export_full_system_code():
    import streamlit as st
    code_blocks = []
    # Collect codes from all supported components if present in session
    for key in [
        "bus_code", "load_code", "generator_code", "storageunit_code",
        "line_code", "link_code", "transformer_code", "carrier_code"
    ]:
        if key in st.session_state:
            code_blocks.append(st.session_state[key])
    header = (
        "# Auto-generated PyPSA network model\n"
        "import pypsa\nimport pandas as pd\nnetwork = pypsa.Network()\n\n"
    )
    footer = "\n# Define more components or run LOPF as needed\n"
    return header + "\n".join(code_blocks) + footer
