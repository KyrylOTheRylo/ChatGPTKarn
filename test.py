import networkx as nx
import matplotlib.pyplot as plt

# Завантаження графа з файлу
G = nx.read_edgelist('graph.txt')
# Розташування вершин
edges = nx.dfs_edges(G)

# малювання графа з виділеними ребрами кістякового лісу
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, edgelist=list(edges), edge_color='r')
plt.savefig('graph2.png')
plt.clf()
edges = nx.dfs_edges(G)
components = list(nx.connected_components(G))

# open a file for writing the results
with open('results.txt', 'w') as f:
    # loop over the connected components
    for i, c in enumerate(components):
        # create a subgraph for the current component
        subgraph = G.subgraph(c)

        # calculate some metrics for the subgraph
        n_nodes = subgraph.number_of_nodes()
        n_edges = subgraph.number_of_edges()
        degrees = dict(subgraph.degree())
        eccentricities = nx.eccentricity(subgraph)
        radius = nx.radius(subgraph)
        diameter = nx.diameter(subgraph)

        # write the results to file
        f.write(f"Component {i + 1}: \n")
        f.write(f"Number of nodes: {n_nodes}\n")
        f.write(f"Number of edges: {n_edges}\n")
        f.write(f"Degrees: {degrees}\n")
        f.write(f"Eccentricities: {eccentricities}\n")
        f.write(f"Radius: {radius}\n")
        f.write(f"Diameter: {diameter}\n\n")

        if diameter > 1:
            # find a diameter for the subgraph
            path = [node for node in subgraph.nodes() if eccentricities[node] == diameter/2]
            # get the nodes and edges that belong to the diameter
            nodes_in_path = set(path)
            edges_in_path = set()
            for x in range(len(path) - 1):
                edges_in_path.add((path[x], path[x + 1]))

            # draw the subgraph with the diameter highlighted
            pos = nx.spring_layout(subgraph)
            nx.draw_networkx_nodes(subgraph, pos=pos, nodelist=nodes_in_path, node_color='r')
            nx.draw_networkx_edges(subgraph, pos=pos, edgelist=edges_in_path, edge_color='r')
            nx.draw_networkx(subgraph, pos=pos, with_labels=True)
            print(i)
            plt.savefig(f'component_{i + 1}_with_diameter.png')
            plt.clf()

    # draw the entire graph
    pos = nx.planar_layout(G)
    nx.draw_networkx(G, pos=pos)
    plt.savefig('graph1.png')