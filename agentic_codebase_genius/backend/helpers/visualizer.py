import os
import networkx as nx
import matplotlib.pyplot as plt

def make_diagram(graph, path):
    G = nx.Graph()
    for file, info in graph.items():
        G.add_node(file)
        for func in info.get("functions", []):
            G.add_node(func)
            G.add_edge(file, func)
    fig = plt.figure(figsize=(8,6))
    nx.draw(G, with_labels=True, node_size=400, font_size=8)
    outdir = os.path.join("outputs", os.path.basename(path))
    os.makedirs(outdir, exist_ok=True)
    plt.savefig(os.path.join(outdir,"diagram.png"))
    plt.close(fig)
