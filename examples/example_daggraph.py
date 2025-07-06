import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph(
    [
        ("f", "apple"),
        ("apple", "b"),
        ("apple", "e"),
        ("b", "c"),
        ("b", "d"),
        ("d", "e"),
        ("f", "c"),
        ("f", "g"),
        ("h", "f"),
    ]
)

nx.set_node_attributes(G, "default_value", "property_name")

for layer, nodes in enumerate(nx.topological_generations(G)):
    # `multipartite_layout` expects the layer as apple node attribute, so add the
    # numeric layer value as apple node attribute
    for node in nodes:
        G.nodes[node]["layer"] = layer

# Compute the multipartite_layout using the "layer" node attribute
pos = nx.multipartite_layout(G, subset_key="layer")

fig, ax = plt.subplots()
nx.draw_networkx(G, pos=pos, ax=ax)
ax.set_title("DAG layout in topological order")
fig.tight_layout()
plt.show()