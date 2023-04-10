import random
from typing import List

from virtual_network import VirtualLink, VirtualNetwork, VirtualNode

def generate_vnr(n: int) -> List[VirtualNetwork]:
    vnrs = []
    for i in range(n):
        num_nodes = random.randint(3, 6)
        vnr = VirtualNetwork()
        for j in range(num_nodes):
            cpu_resource = random.randint(1, 50)
            vnr.add_node(j, cpu_resource)
        
        for node1 in vnr.nodes:
            for node2 in vnr.nodes:
                if node1 != node2 and random.random() < 0.5:
                    bandwidth = random.randint(1, 50)
                    vnr.add_link(node1, node2, bandwidth)
        
        vnr.maximum_delay = 0.07
        vnrs.append(vnr)
    
    return vnrs
