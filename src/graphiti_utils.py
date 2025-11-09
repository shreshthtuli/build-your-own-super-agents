from rich.pretty import pprint

from graphiti_core.edges import EntityEdge

from falkordb import FalkorDB
from pyvis.network import Network
from collections import defaultdict

import re

def pretty_print(entity: EntityEdge | list[EntityEdge]):
    if isinstance(entity, EntityEdge):
        data = {k: v for k, v in entity.model_dump().items() if k != 'fact_embedding'}
    elif isinstance(entity, list):
        data = [{k: v for k, v in e.model_dump().items() if k != 'fact_embedding'} for e in entity]
    else:
        pprint(entity)
        return
    pprint(data)

def add_physics_stop_to_html(filepath):
    with open(filepath, 'r', encoding="utf-8") as file:
        content = file.read()

    # Search for the stabilizationIterationsDone event and insert the network.setOptions line
    pattern = r'(network.once\("stabilizationIterationsDone", function\(\) {)'
    replacement = r'\1\n\t\t\t\t\t\t  // Disable the physics after stabilization is done.\n\t\t\t\t\t\t  network.setOptions({ physics: false });'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Write the modified content back to the file
    with open(filepath, 'w', encoding="utf-8") as file:
        file.write(new_content)

def save_graph(filename: str = "assets/pokemon.html"):
    db = FalkorDB()
    g = db.select_graph("default_db")

    cypher = "MATCH (n)-[r]->(m) RETURN id(n), labels(n), properties(n), type(r), properties(r), id(m), labels(m), properties(m)"

    res = g.query(cypher)
    net = Network(height="1200px", width="100%", directed=True, notebook=False)
    net.repulsion(central_gravity=0.04, spring_length=150, spring_strength=0.04, damping=0.96)

    seen = set()

    PALETTE = [
        "#8ecae6", "#219ebc", "#f94144", "#ffb703", "#fb8500",
        "#b5179e", "#7209b7", "#4361ee", "#4cc9f0", "#2a9d8f",
        "#e76f51", "#00b4d8", "#90be6d", "#f94144", "#577590"
    ]
    label2color = defaultdict(lambda: "#999999")  # fallback color
    def color_for_label(lbl: str) -> str:
        if lbl not in label2color:
            label2color[lbl] = PALETTE[len(label2color) % len(PALETTE)]
        return label2color[lbl]

    def add_node(node_id, label, name, summary):
        net.add_node(
            node_id,
            label=name,
            color=color_for_label(label),
            title=summary,
            shape="dot",
            size=18,
        )
        seen.add(node_id)

    for row in res.result_set:
        # source node
        source_id = row[0]
        source_dict = row[2]
        if 'labels' not in source_dict: continue
        source_name, source_summary, source_label = source_dict['name'], source_dict['summary'], source_dict['labels'][0]

        # relation
        relation = row[4]['name']

        # destination node
        dest_id = row[5]
        dest_dict = row[7]
        if 'labels' not in dest_dict: continue
        dest_name, dest_summary, dest_label = dest_dict['name'], dest_dict['summary'], dest_dict['labels'][0]

        # create graph
        if source_id not in seen:
            add_node(source_id, source_label, source_name, source_summary)
        if dest_id not in seen:
            add_node(dest_id, dest_label, dest_name, dest_summary)
        
        net.add_edge(source_id, dest_id, label=relation, arrows="to")

    net.save_graph(filename)
    add_physics_stop_to_html(filename)