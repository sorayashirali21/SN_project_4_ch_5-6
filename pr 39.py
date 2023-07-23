#39

import networkx as nx
import matplotlib.pyplot as plt

# Read the graph from a file
G = nx.read_edgelist('soc-Epinions1.txt', comments='#', delimiter='\t', create_using=nx.Graph(), nodetype=int)


num_runs = 10
degree_dist = {}

for _ in range(num_runs):
    degree_sequence = [degree for node, degree in G.degree()]
    degree_sequence = sorted(degree_sequence, reverse=True)

    for degree in degree_sequence:
        if degree in degree_dist:
            degree_dist[degree] += 1
        else:
            degree_dist[degree] = 1

total_nodes = G.number_of_nodes()
degree_dist_normalized = {degree: count / (num_runs * total_nodes) for degree, count in degree_dist.items()}

# Sort the degree distribution by degree values
sorted_degree_dist = sorted(degree_dist_normalized.items())

# Get the degrees and corresponding fractions
degrees, fractions = zip(*sorted_degree_dist)
