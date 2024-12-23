import networkx as nx
from itertools import combinations

def get_data(filename):
    G = nx.Graph()
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            node1, node2 = line.split("-")
            G.add_edge(node1, node2)
    return G

def is_correct_triplet(G, triplet):
    SG = G.subgraph(triplet)
    if len(list(SG.edges())) == 3:
        return True
    else:
        return False

def find_max_clique(G):
    cliques = list(nx.find_cliques(G))
    cliques.sort(key = len)
    return ",".join(sorted(cliques[-1]))

# Main Program
G = get_data("Input.txt")
l_nodes = list(G.nodes())
l_triplets = list(combinations(l_nodes, 3))
l_correct_triplets = []
for triplet in l_triplets:
    n1, n2, n3 = triplet
    if n1.startswith("t") or n2.startswith("t") or n3.startswith("t"):
        if is_correct_triplet(G, triplet):
            l_correct_triplets.append(triplet)

print("The number of triplets containing a t* is:", len(l_correct_triplets))
print("The maximum interconnected group is: ", find_max_clique(G))