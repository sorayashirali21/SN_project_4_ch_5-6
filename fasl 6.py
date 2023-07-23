#chapter 6

import networkx as nx
import random
import matplotlib.pyplot as plt


def generate_random_network(height, b, k, alpha):
    T = nx.balanced_tree(b, height)
    network = nx.DiGraph()

    for node in T.nodes():
        p = {v: b ** (-alpha * nx.shortest_path_length(T, source=node, target=v)) for v in T.nodes()}
        Z = sum(p.values())
        for _ in range(k):
            w = random.choices(list(p.keys()), list(p.values()))[0]
            network.add_edge(node, w)
            p[w] = 0
            Z -= p[w]
            if Z > 0:
                p = {v: p[v] / Z for v in p}

    return network


def decentralized_search(network, s, t):
    current_node = s
    path_length = 0

    while current_node != t:
        neighbors = list(network.neighbors(current_node))
        neighbors.sort(key=lambda x: nx.shortest_path_length(network, source=x, target=t))
        next_node = neighbors[0]

        if nx.shortest_path_length(network, source=current_node, target=t) > nx.shortest_path_length(network,
                                                                                                     source=next_node,
                                                                                                     target=t):
            current_node = next_node
            path_length += 1
        else:
            return float('inf')

    return path_length


# Set the parameters
height = 10
b = 2
k = 5
alphas = [0.1 * i for i in range(11)]
# alphas = [0.1 * i for i in range(2)]
num_pairs = 1000

# Run the experiment
average_path_lengths, search_success_probabilities = decentralized_search(height, b, k, alphas, num_pairs)

# Plot the results
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(alphas, average_path_lengths, marker='o')
plt.xlabel('Alpha')
plt.ylabel('Average Path Length')
plt.title('Average Path Length vs. Alpha')

plt.subplot(1, 2, 2)
plt.plot(alphas, search_success_probabilities, marker='o')
plt.xlabel('Alpha')
plt.ylabel('Search Success Probability')
plt.title('Search Success Probability vs. Alpha')

plt.tight_layout()
plt.show()