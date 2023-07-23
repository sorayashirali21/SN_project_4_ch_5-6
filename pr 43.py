
#43
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('soc-Epinions1.txt', comments='#', delimiter='\t', create_using=nx.Graph(), nodetype=int)

core_numbers = nx.core_number(G)

core_number_count = {}
for number in core_numbers.values():
    if number not in core_number_count:
        core_number_count[number] = 0
    core_number_count[number] += 1

# Sort the core numbers in ascending order
sorted_numbers = sorted(core_number_count.keys())

# Count the number of nodes for each core number
core_number_distribution = [core_number_count[number] for number in sorted_numbers]
