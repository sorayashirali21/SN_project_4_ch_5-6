
#40
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.read_edgelist('soc-Epinions1.txt', comments='#', delimiter='\t', create_using=nx.Graph(), nodetype=int)

num_walks = 1000
max_walk_length = 100

path_lengths = []
for node in G.nodes():
    for _ in range(num_walks):
        current_node = node
        walk_length = 0
        while walk_length < max_walk_length:
            neighbors = list(G.neighbors(current_node))
            if len(neighbors) > 0:
                next_node = np.random.choice(neighbors)
                current_node = next_node
                walk_length += 1
            else:
                break
        path_lengths.append(walk_length)

path_length_dist = {}
total_paths = len(path_lengths)
for length in path_lengths:
    if length in path_length_dist:
        path_length_dist[length] += 1
    else:
        path_length_dist[length] = 1

path_length_dist_normalized = {length: count / total_paths for length, count in path_length_dist.items()}

sorted_path_lengths = sorted(path_length_dist_normalized.items())

lengths, fractions = zip(*sorted_path_lengths)

plt.plot(lengths, fractions, marker='o')
plt.xlabel('Path Length')
plt.ylabel('Fraction')
plt.title('Path Length Distribution')
plt.show()
