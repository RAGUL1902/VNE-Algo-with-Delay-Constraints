def compute_noderank(graph):
    """
    This function computes the noderank of each node in the given WeightedGraph.

    Parameters:
        graph (WeightedGraph): The graph for which to compute noderank.

    Returns:
        dict: A dictionary mapping node IDs to their corresponding noderank values.
    """
    # Calculate the sum of outgoing bandwidth for each node
    outgoing_bandwidth_sums = {}
    for node in graph.nodes:
        outgoing_bandwidth_sum = 0
        for link in node.links:
            outgoing_bandwidth_sum += link.bandwidth
        outgoing_bandwidth_sums[node.node_id] = outgoing_bandwidth_sum

    # Calculate the noderank of each node
    noderanks = {}
    noderank_sum = 0
    for node in graph.nodes:
        noderank = outgoing_bandwidth_sums[node.node_id] * node.cpu_capacity
        noderanks[node.node_id] = noderank
        noderank_sum += noderank

    # Normalize the noderank values
    for node_id in noderanks:
        noderanks[node_id] /= noderank_sum

    return noderanks