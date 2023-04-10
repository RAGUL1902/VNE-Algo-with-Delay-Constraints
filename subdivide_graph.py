from virtual_network import VirtualNetwork

def divide_graph_to_subgraphs(vn):
    # Create a dictionary to store the node ranks of all nodes
    node_ranks = {}
    
    # Calculate the node rank of each node in the VirtualNetwork object
    for node in vn.nodes:
        adjacent_nodes = vn.get_adjacent_nodes(node)
        bw_sum = 0
        for adj_node in adjacent_nodes:
            bw_sum += vn.get_link_bandwidth(node,adj_node)
        node_ranks[node] = node.cpu_capacity * bw_sum
    
    # Sort the nodes in the decreasing order of their node ranks
    sorted_nodes = sorted(node_ranks.keys(), key=lambda x: node_ranks[x], reverse=True)
    
    subgraphs = []
    
    # Iterate over the sorted nodes and create subgraphs for each node
    while sorted_nodes:

        hub = sorted_nodes[0]
        spokes = vn.get_adjacent_nodes(hub)
        subgraph_nodes = set([hub] + spokes)

        # Create a new VirtualNetwork object for the subgraph
        subgraph = VirtualNetwork()
        subgraph.maximum_delay = vn.maximum_delay
        
        # Add the nodes and links to the subgraph object
        for node in subgraph_nodes: 
            if node in sorted_nodes: 
                subgraph.add_node(node.node_id, node.cpu_capacity)
        for spoke in spokes: 
            if spoke in sorted_nodes:
                subgraph.add_link(hub, spoke, vn.get_link_bandwidth(hub, spoke))

        # Remove the hub and spokes from the sorted_nodes list
        for node in subgraph_nodes:
            if node in sorted_nodes:
                sorted_nodes.remove(node)
        
        subgraphs.append(subgraph)
    
    return subgraphs
