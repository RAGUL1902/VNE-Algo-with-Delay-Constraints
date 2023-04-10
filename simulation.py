from generate_vnr import generate_vnr
from subdivide_graph import subdivide_graph
from visualize_virtual_network import visualize_virtual_network


vnr = generate_vnr(1)
visualize_virtual_network(vnr[0])

clusters = subdivide_graph(vnr[0])
for i in clusters:
    visualize_virtual_network(i)
