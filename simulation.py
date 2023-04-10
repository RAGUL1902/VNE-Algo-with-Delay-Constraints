from generate_vnr import generate_vnr
from subdivide_graph import divide_graph_to_subgraphs
from visualize_virtual_network import visualize_virtual_network


vnr = generate_vnr(1)

subsnet = generate_subsnet()

visualize_virtual_network(vnr[0])
clusters = divide_graph_to_subgraphs(vnr[0])
for i in clusters:
    visualize_virtual_network(i)

subs_noderank = compute_noderank(subsnet)

vnr_noderank = []
for cluster in clusters:
    vnr_noderank.append(compute_noderank(cluster))

# TODO: Sort subsnet node acc to noderank

