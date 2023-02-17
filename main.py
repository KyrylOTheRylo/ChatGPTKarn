import networkx as nx

# Створення графу
G = nx.Graph()

# Додавання вершин
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])

# Додавання ребер
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (5, 6), (5, 7), (6, 7), (4, 5)])

# Збереження графу у текстовий файл
nx.write_edgelist(G, "graph.txt")