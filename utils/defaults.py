# Default values for each component if you want to auto-fill forms or support future logic.

DEFAULTS = {
    "Bus": {
        "carrier": "electricity",
        "v_nom": 110.0,
        "comment": "",
    },
    "Load": {
        "p_set": 0.0,
        "comment": "",
    },
    "Generator": {
        "carrier": "electricity",
        "p_nom": 0.0,
        "p_max_pu": "1.0",
        "marginal_cost": 0.0,
        "build_year": 2025,
        "lifetime": 25,
        "comment": "",
    },
    "StorageUnit": {
        "carrier": "electricity",
        "p_nom": 0.0,
        "max_hours": 4.0,
        "efficiency_store": 0.9,
        "efficiency_dispatch": 0.9,
        "cyclic_state_of_charge": True,
        "comment": "",
    },
    "Line": {
        "s_nom": 0.0,
        "x": 0.01,
        "r": 0.0,
        "length": 1.0,
        "comment": "",
    },
    "Link": {
        "carrier": "electricity",
        "p_nom": 0.0,
        "efficiency": 0.9,
        "marginal_cost": 0.0,
        "comment": "",
    },
    "Transformer": {
        "s_nom": 0.0,
        "x": 0.01,
        "r": 0.0,
        "tap_ratio": 1.0,
        "comment": "",
    },
    "Carrier": {
        "name": "electricity",
        "co2_emissions": 0.0,
        "comment": "",
    }
}
