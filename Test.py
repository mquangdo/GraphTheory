import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G = nx.Graph() #undirected graph
A = nx.DiGraph() #directed graph




D = np.linspace(1, 10, 100)
E = np.arange(1, 10, 0.5)

# print(A)
# print(D)
# print(E)

edge_list = [(1, 2), (2, 3), (3, 4)]
G.add_edge(1,2)
G.add_edge(2, 3, weight = 0.9)
G.add_edge(2, 1)
G.add_edge('A',' B')
G.add_edges_from(edge_list)


F = nx.Graph()
F.add_edge(1, 2)
F.add_edge(2, 3, weight = 1)
F.add_edge(3, 4)
F.add_edge(4, 5)
F.add_node('C')


edge_list = [(1, 2), (2, 3), (3, 1)]
E = nx.from_edgelist(edge_list)


B = np.ones((2, 2), dtype = int)     #ma trận kề
H = nx.from_numpy_array(B)

# nx.draw_spring(G, with_labels = True)
# nx.draw_spring(F, with_labels = True)

# nx.draw_spring(E, with_labels = True)
# print(nx.adjacency_matrix(E))     #ma tran ke cua E
# nx.draw_spring(F, with_labels = True)
# nx.draw_spring(H, with_labels = True)

# nx.draw_planar(F, with_labels = True)

I = nx.complete_graph(5)    # do thi thay du K_5
# nx.draw_planar(I)     #error vi K_5 khong phang
# nx.draw_spring(I)

J = nx.complete_bipartite_graph(3, 3)
nx.draw_spring(J, with_labels = True)

print(I.degree)

def check_bipartite(G):
    for i, v in G.degree:
        if v % 2 != 0:
            return 'This is not a bipartite graph'
        else:
            return 'This is a bipartite graph'

def is_hamiltonian(G):
    n = len(G.degree)
    for i in range(n):
        if G.degree[i] < n / 2:
            return 'Inconclusion'
        else:
            return 'Hamiltonian'

print(is_hamiltonian(I))

plt.show()


