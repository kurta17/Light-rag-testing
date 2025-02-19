import networkx as nx
import matplotlib.pyplot as plt

# Load the GraphML file
G = nx.read_graphml("graph_chunk_entity_relation.graphml")

# Draw the graph
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", font_size=8)
plt.show()
