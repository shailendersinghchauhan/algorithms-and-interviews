import networkx as nx
import matplotlib.pyplot as plt

# Define nodes and edges
nodes = [1, 2, 3, 4, 5, 6]
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 6), (5, 6)]

# Create network topology
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Draw network topology
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='r', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='b')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
plt.axis('off')
plt.show()