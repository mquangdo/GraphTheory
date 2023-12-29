import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G = nx.Graph() #undirected graph
A = nx.DiGraph() #directed graph

edge_list = [(1, 2), (2, 3), (3, 4)]

B = np.ones((2, 2), dtype = int) #ma trận kề
D = np.linspace(1, 10, 100)
E = np.arange(1, 10, 0.5)

print(A)
print(D)
print(E)

G.add_edge(1,2)
G.add_edge(2, 3, weight = 0.9)
G.add_edge('A',' B')
G.add_edges_from(edge_list)

H = nx.from_numpy_array(B)


nx.draw_spring(G, with_labels = True)
nx.draw_spring(H, with_labels = True)
plt.show()
