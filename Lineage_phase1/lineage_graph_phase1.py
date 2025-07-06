import uuid
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('workflows.csv')
print(df)
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip()


G = nx.from_pandas_edgelist(df, source='Workflow1', target='Workflow2', create_using=nx.DiGraph())


print(G.edges(data=True))

# G = nx.DiGraph(
#     [('WorkflowB', 'WorkflowA'), 
#      ('WorkflowC', 'WorkflowB'),
#      ('Workflow1', 'Workflow2')]
# )

# print(G.edges())

nx.set_node_attributes(G, "default_value", "property_name")

# Assign a numeric layer value to each node based on its topological order
# This is necessary for the multipartite_layout to work correctly.
for layer, nodes in enumerate(nx.topological_generations(G)):
    for node in nodes:
        G.nodes[node]["layer"] = layer

# Compute the multipartite_layout using the "layer" node attribute
# this layout in horizontal layers
pos = nx.multipartite_layout(G, subset_key="layer")

# fig = figure object/where graph is going to show
# ax = axes object which is the actual area data is plotted (x and y axis)
# plt = artist toolbox
# fig, ax = plt.subplots(2,2, figsize=(10, 10))
fig, ax = plt.subplots()
nx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color='lightblue', node_size=300)
nx.draw_networkx_labels(G, pos=pos, ax=ax, font_size=10)
nx.draw_networkx_edges(
    G,
    pos=pos,
    ax=ax,
    arrows=True,
    arrowsize=50,  # 🔺 Increase arrowhead size here
    edge_color='gray'
)

ax.set_title("DAG layout for Lineage of Workflows")
# fig.tight_layout()
unique_id = uuid.uuid4()

# saves file
fig.savefig(f"graph_images/lineage_plot_{unique_id}.png")
plt.show()