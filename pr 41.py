
#41
import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_edgelist('soc-Epinions1.txt', comments='#', delimiter='\t', create_using=nx.DiGraph(), nodetype=int)

wcc = nx.weakly_connected_components(G)

wcc_sizes = [len(component) for component in wcc]

wcc_size_count = {}
for size in wcc_sizes:
    if size not in wcc_size_count:
        wcc_size_count[size] = 0
    wcc_size_count[size] += 1


sorted_sizes = sorted(wcc_size_count.keys())


wcc_size_distribution = [wcc_size_count[size] for size in sorted_sizes]
