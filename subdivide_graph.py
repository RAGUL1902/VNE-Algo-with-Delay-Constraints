from virtual_network import VirtualNetwork, VirtualNetworkSubgraph

# define a function to divide a graph into subgraphs of hub-spoke structure
def subdivide_graph(virtual_network: VirtualNetwork):
    # create a dictionary to store the adjacency list of the graph
    adjacency_dict = {}
    for node in virtual_network.nodes:
        node_id = node.node_id
        adjacency_dict[node_id] = []

    # add edges to the adjacency list
    for link in virtual_network.links:
        node1_id = link.node1.node_id
        node2_id = link.node2.node_id
        adjacency_dict[node1_id].append(node2_id)
        adjacency_dict[node2_id].append(node1_id)

    # calculate the degree centrality of each node
    centrality = {}
    for node in virtual_network.nodes:
        node_id = node.node_id
        adjacent_nodes = adjacency_dict[node_id]
        degree = len(adjacent_nodes)
        centrality[node_id] = degree

    # identify the nodes with the highest degree centrality
    hub_nodes = [node_id for node_id, degree in centrality.items() if degree >= 0.4]

    # divide the graph into subgraphs of hub-spoke structure
    subgraphs = []
    for hub_node in hub_nodes:
        subgraph = VirtualNetworkSubgraph((hub_node), [])
        subgraph.spoke_nodes.append(subgraph.hub_node)

        # remove the hub node and its edges from the original graph
        adjacency_dict.pop(hub_node)
        for node_id in adjacency_dict.keys():
            adjacency_dict[node_id] = [n for n in adjacency_dict[node_id] if n != hub_node]

        # add any remaining nodes to the subgraph as spokes
        spoke_nodes = []
        for node_id in adjacency_dict.keys():
            if node_id in subgraph.spoke_nodes:
                continue
            if any([node_id in adjacency_dict[n] for n in subgraph.spoke_nodes]):
                spoke_node = (node_id)
                subgraph.spoke_nodes.append(spoke_node)
                spoke_nodes.append(spoke_node)

        # repeat the process until all spokes are found
        while spoke_nodes:
            new_spoke_nodes = []
            for spoke_node in spoke_nodes:
                adjacent_nodes = virtual_network.get_adjacent_nodes(spoke_node)
                for node in adjacent_nodes:
                    if node in subgraph.spoke_nodes:
                        continue
                    if any([node.node_id in adjacency_dict[n] for n in subgraph.spoke_nodes]):
                        subgraph.spoke_nodes.append(node.node_id)
                        new_spoke_nodes.append(node.node_id)
            spoke_nodes = new_spoke_nodes

        subgraphs.append(subgraph)

    return subgraphs