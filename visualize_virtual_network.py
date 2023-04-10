import networkx as nx
import matplotlib.pyplot as plt

def visualize_virtual_network(virtual_network):
    # Create an empty graph object
    G = nx.Graph()

    # Add nodes to the graph
    for node in virtual_network.nodes:
        G.add_node(node.node_id, cpu_capacity=node.cpu_capacity)

    # Add edges to the graph
    for link in virtual_network.links:
        G.add_edge(link.node1.node_id, link.node2.node_id, bandwidth=link.bandwidth, delay=virtual_network.maximum_delay)

    # Define node and edge attributes for plotting
    node_labels = nx.get_node_attributes(G, 'cpu_capacity')
    edge_labels = nx.get_edge_attributes(G, 'bandwidth')
    edge_delays = nx.get_edge_attributes(G, 'delay')

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_edges(G, pos, width=3, edge_color='gray')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_delays, font_size=10, label_pos=0.5, font_color='red')

    # Set plot attributes and display the image
    plt.title('Virtual Network')
    plt.axis('off')
    plt.show()
