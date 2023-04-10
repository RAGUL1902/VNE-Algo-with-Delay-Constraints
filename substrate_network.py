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
    
    def get_node_ids(self):
        """
        This method returns a list of all the node IDs in the graph.
        """
        node_ids = []
        for node in self.nodes:
            node_ids.append(node.node_id)
        return node_ids







# import random

# class SubstrateNode:
#     def __init__(self, node_id, cpu_capacity):
#         self.node_id = node_id
#         self.cpu_capacity = cpu_capacity

# class Link:
#     def __init__(self, source, target, bandwidth, delay):
#         self.source = source
#         self.target = target
#         self.bandwidth = bandwidth
#         self.delay = delay

# class SubstrateNetwork:
#     def __init__(self):
#         self.nodes = []
#         self.links = []
#         self.maximum_delay = 0
    
#     def add_node(self, node):
#         self.nodes.append(node)
        
#     def add_link(self, link):
#         self.links.append(link)
#         self.maximum_delay = max(self.maximum_delay, link.delay)

# def generate_substrate_network(num_nodes):
#     substrate_network = SubstrateNetwork()

#     # create nodes with random cpu capacity
#     for i in range(num_nodes):
#         cpu_capacity = random.uniform(0, 100)
#         node = SubstrateNode(i, cpu_capacity)
#         substrate_network.add_node(node)

#     # connect nodes with probability 0.5
#     for i in range(num_nodes):
#         for j in range(i+1, num_nodes):
#             if random.random() < 0.5:
#                 bandwidth = random.uniform(0, 100)
#                 delay = random.uniform(0, 0.005)
#                 link = Link(i, j, bandwidth, delay)
#                 substrate_network.add_link(link)

#     return substrate_network
