import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

vertexes = ["A", "B", "C", "D", "E", "F", "G", "H"]
G.add_nodes_from(vertexes)

edges = [("A", "B"), ("A", "E"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "G"), ("C", "H"), ("D", "F"), ("D", "G"), ("D", "E"), ("C", "E")]
G.add_edges_from(edges)

nx.draw(G, node_size=600, with_labels=True)
plt.show()

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Ступені вершин:", dict(G.degree()))