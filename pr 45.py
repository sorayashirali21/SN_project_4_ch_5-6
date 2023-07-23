
#45
import networkx as nx
import matplotlib.pyplot as plt

# Read the graph from a file
G = nx.read_edgelist('soc-Epinions1.txt', comments='#', delimiter='\t', create_using=nx.Graph(), nodetype=int)

avg_neighbor_degree = {}
for node in G.nodes():
    neighbors = list(G.neighbors(node))
    neighbor_degrees = [G.degree(neighbor) for neighbor in neighbors]
    avg_neighbor_degree[node] = sum(neighbor_degrees) / len(neighbors) if len(neighbors) > 0 else 0


neighbor_degree_count = {}
for value in avg_neighbor_degree.values():
    if value not in neighbor_degree_count:
        neighbor_degree_count[value] = 0
    neighbor_degree_count[value] += 1


sorted_values = sorted(neighbor_degree_count.keys())


neighbor_degree_distribution = [neighbor_degree_count[value] for value in sorted_values]
