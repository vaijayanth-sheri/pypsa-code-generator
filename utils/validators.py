import streamlit as st

def get_system_warnings():
    """
    Runs basic validation on the session state to warn about obvious misconfigurations.
    E.g., missing buses, unconnected loads/generators, duplicate names.
    :return: List of warning messages
    """
    warnings = []
    seen_names = set()
    bus_names = set()
    component_blocks = st.session_state.get("components", [])
    for code in component_blocks:
        if "network.add(\"Bus\"" in code or "network.add('Bus'" in code:
            # Extract the bus name
            name = parse_block_name(code, "Bus")
            if name:
                bus_names.add(name)
        else:
            # Try to extract name and bus references for validation
            name = parse_any_block_name(code)
            if name:
                if name in seen_names:
                    warnings.append(f"Duplicate component name detected: '{name}'")
                seen_names.add(name)
            bus_ref = parse_bus_ref(code)
            if bus_ref and bus_ref not in bus_names:
                warnings.append(f"Component '{name}' references undefined bus: '{bus_ref}'")

    return warnings

def parse_block_name(code, block_type):
    """
    Parses the name of a block from its add() code.
    """
    import re
    pat = rf'add\(["\']{block_type}["\'],\s*["\']([^"\']+)["\']'
    m = re.search(pat, code)
    return m.group(1) if m else None

def parse_any_block_name(code):
    """
    Extracts the first name argument from an add() call.
    """
    import re
    pat = r'add\(["\'][A-Za-z]+["\'],\s*["\']([^"\']+)["\']'
    m = re.search(pat, code)
    return m.group(1) if m else None

def parse_bus_ref(code):
    """
    Attempts to extract the bus/bus0/bus1 argument from add() code.
    """
    import re
    # Try bus=, bus0=, bus1=, in order of likelihood
    pat = r'bus[0-9]?=["\']([^"\']+)["\']'
    m = re.search(pat, code)
    return m.group(1) if m else None
