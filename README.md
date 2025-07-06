# networkx

# Examples in the "examples" folder from networkx.org

https://networkx.org/documentation/stable/auto_examples/

Light weighted graph, examples show easy implementation

- for config based, potentially create a config file and running python per node wanted to view edges to other nodes

- next steps mimic table lineage data with workflows and try graphing

# Lineage Phase 1 Learnings

topological_generations:
A topological generation is node collection in which ancestors of a node in each generation are guaranteed to be in a previous generation, and any descendants of a node are guaranteed to be in a following generation. Nodes are guaranteed to be in the earliest possible generation that they can belong to.

moreinfo
https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.dag.topological_generations.html#networkx.algorithms.dag.topological_generations

Topological_sort:
A topological sort is a nonunique permutation of the nodes of a directed graph such that an edge from u to v implies that u appears before v in the topological sort order. This ordering is valid only if the graph has no directed cycles.

https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.dag.topological_sort.html#networkx.algorithms.dag.topological_sort

Workflow_C -> Workflow_B -> Workflow_A
Workflow_E -> Workflow_D
