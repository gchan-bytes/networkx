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

for layer, nodes in enumerate(nx.topological_generations(G)):
    for node in nodes:
        G.nodes[node]["layer"] = layer

# Compute the multipartite_layout using the "layer" node attribute
pos = nx.multipartite_layout(G, subset_key="layer")

fig, ax = plt.subplots()
nx.draw_networkx(G, pos=pos, ax=ax)
ax.set_title("DAG layout in topological order")
fig.tight_layout()
plt.show()