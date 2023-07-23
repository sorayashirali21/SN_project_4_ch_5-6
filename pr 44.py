
#44
import networkx as nx
import matplotlib.pyplot as plt

# Read the graph from a file
G = nx.read_edgelist('soc-Epinions1.txt', comments='#', delimiter='\t', create_using=nx.Graph(), nodetype=int)

avg_friends_of_friends = {}
for node in G.nodes():
    friends_of_friends = set()
    for neighbor in G.neighbors(node):
        friends_of_friends.update(G.neighbors(neighbor))
    friends_of_friends.discard(node)
    avg_friends_of_friends[node] = len(friends_of_friends) / len(list(G.neighbors(node))) if len(list(G.neighbors(node))) > 0 else 0


friends_of_friends_count = {}
for value in avg_friends_of_friends.values():
    if value not in friends_of_friends_count:
        friends_of_friends_count[value] = 0
    friends_of_friends_count[value] += 1

sorted_values = sorted(friends_of_friends_count.keys())

friends_of_friends_distribution = [friends_of_friends_count[value] for value in sorted_values]
