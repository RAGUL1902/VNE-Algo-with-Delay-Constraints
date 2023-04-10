class VirtualNode:
    """
    This class represents a virtual node in a Virtual Network.
    """
    def __init__(self, node_id, cpu_capacity):
        self.node_id = node_id
        self.cpu_capacity = cpu_capacity

class VirtualLink:
    """
    This class represents a virtual link in a Virtual Network.
    """
    def __init__(self, node1: VirtualNode, node2: VirtualNode, bandwidth :int):
        self.node1 = node1
        self.node2 = node2
        self.bandwidth = bandwidth

class VirtualNetwork:
    """
    This class represents a Virtual Network as weighted undirected graph with nodes as virtual nodes and edges as virtual links.
    """
    def __init__(self):
        self.nodes = []
        self.links = []
        self.maximum_delay = 0.07

    

    def add_node(self, node_id, cpu_capacity):
        """
        This method adds a virtual node to the graph with the given node id and CPU capacity request.
        """
        node = VirtualNode(node_id, cpu_capacity)
        self.nodes.append(node)

    def add_link(self, node1: VirtualNode, node2: VirtualNode, bandwidth):
        """
        This method adds a virtual link to the graph between the given nodes with the given bandwidth request weight.
        """
        link = VirtualLink(node1, node2, bandwidth)
        self.links.append(link)

    def get_node_by_id(self, node_id):
        """
        This method returns the virtual node object with the given node id.
        """
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    def get_adjacent_nodes(self, node):
        """
        This method returns a list of virtual nodes that are adjacent to the given node.
        """
        adjacent_nodes = []
        for link in self.links:
            if link.node1 == node:
                adjacent_nodes.append(link.node2)
            elif link.node2 == node:
                adjacent_nodes.append(link.node1)
        return adjacent_nodes
    
    def get_node_ids(self):
        """
        This method returns a list of all the node IDs in the graph.
        """
        node_ids = []
        for node in self.nodes:
            node_ids.append(node.node_id)
        return node_ids
    
class VirtualNetworkSubgraph:
    """
    This class represents a subgraph of a Virtual Network with a hub-spoke structure.
    """
    def __init__(self, hub_node_id, spoke_node_ids):
        self.hub_node = hub_node_id
        self.spoke_nodes = spoke_node_ids
