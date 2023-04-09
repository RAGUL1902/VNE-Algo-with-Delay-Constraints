class SubstrateNode:
    """
    This class represents a substrate node in a Substrate Network.
    """
    def __init__(self, node_id, cpu_capacity):
        self.node_id = node_id
        self.cpu_capacity = cpu_capacity

class Link:
    """
    This class represents an edge/link in a Substrate Network
    """
    def __init__(self, node1, node2, bandwidth, delay):
        self.node1 = node1
        self.node2 = node2
        self.bandwidth = bandwidth
        self.delay = delay

class SubstrateNetwork:
    """
    This class represents a weighted undirected graph as Substrate Network with nodes as substrate nodes and edges as links.
    """
    def __init__(self):
        self.nodes = []
        self.links = []

    def add_node(self, node_id, cpu_capacity):
        """
        This method adds a node to the graph with the given node id and CPU capacity.
        """
        node = SubstrateNode(node_id, cpu_capacity)
        self.nodes.append(node)

    def add_link(self, node1, node2, bandwidth, delay):
        """
        This method adds an edge/link to the graph between the given nodes with the given bandwidth and delay weights.
        """
        link = Link(node1, node2, bandwidth, delay)
        self.links.append(link)

    def get_node_by_id(self, node_id):
        """
        This method returns the node object with the given node id.
        """
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    def get_adjacent_nodes(self, node):
        """
        This method returns a list of nodes that are adjacent to the given node.
        """
        adjacent_nodes = []
        for link in self.links:
            if link.node1 == node:
                adjacent_nodes.append(link.node2)
            elif link.node2 == node:
                adjacent_nodes.append(link.node1)
        return adjacent_nodes
