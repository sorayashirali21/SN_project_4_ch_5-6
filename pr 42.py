#42
import networkx as nx
import matplotlib.pyplot as plt

# Read the graph from a file
G = nx.read_edgelist('soc-Epinions1.txt', comments='#', delimiter='\t', create_using=nx.DiGraph(), nodetype=int)


clustering_coeffs = nx.clustering(G)


# Count the number of nodes for each clustering coefficient
clustering_coeff_distribution = [clustering_coeffs[coeff] for coeff in sorted_coeffs]
