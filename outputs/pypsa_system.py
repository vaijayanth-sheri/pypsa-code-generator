# Auto-generated PyPSA network model
import pypsa
import pandas as pd
network = pypsa.Network()

network.add("Bus", "e_bus",
    carrier="electricity",
    v_nom=110.0)
network.add("Bus", "e_bus",
    carrier="electricity",
    v_nom=110.0)
network.add("Load", "",
    bus="",
    p_set=0.0)
network.add("Generator", "",
    bus="",
    carrier="electricity",
    p_nom=0.0,
    marginal_cost=0.0,
    build_year=2025,
    lifetime=25)
network.add("StorageUnit", "",
    bus="",
    carrier="electricity",
    p_nom=0.0,
    max_hours=4.0,
    efficiency_store=0.9,
    efficiency_dispatch=0.9,
    cyclic_state_of_charge=True)
# Define more components or run LOPF as needed
