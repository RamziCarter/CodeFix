import networkx as nx
import matplotlib.pyplot as plt

# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores edges with weights
        self.visual = []

    # addEdge function inputs the vertices of an edge and its weight
    def addEdge(self, a, b, weight):
        temp = (a, b, weight)
        self.visual.append(temp)

    # Visualize the full graph
    def visualize_full_graph(self):
        G = nx.Graph()
        for edge in self.visual:
            G.add_edge(edge[0], edge[1], weight=edge[2])

        pos = nx.circular_layout(G)  # Layout for nodes
        nx.draw_networkx(G, pos, node_color='lightblue', node_size=2000, font_size=10)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
        plt.title("Full Graph")
        plt.show()
        return G, pos  # Return the graph and its layout for reuse

    def visualize_greedy_path_fixed(self, G, pos, start_node):
        visited = set()  # Use a set for faster lookup of visited nodes
        greedy_path_edges = []
        current_node = start_node

        while len(visited) < len(G.nodes):
            visited.add(current_node)  # Mark the current node as visited

            # Find all unvisited neighbors with their weights
            neighbors = [
                (neighbor, G[current_node][neighbor]['weight'])
                for neighbor in G.neighbors(current_node)
                if neighbor not in visited
            ]

            if not neighbors:
                break  # Stop if no neighbors are left to visit

            # Pick the neighbor with the smallest weight
            next_node, weight = min(neighbors, key=lambda x: x[1])
            greedy_path_edges.append((current_node, next_node))  # Add the edge to the path
            current_node = next_node  # Move to the next node

        # Draw the full graph
        nx.draw_networkx(G, pos, node_color='lightblue', node_size=2000, font_size=10)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

        # Highlight the greedy path
        nx.draw_networkx_edges(G, pos, edgelist=greedy_path_edges, edge_color='red', width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color='orange', node_size=2000)

        plt.title("Greedy Path by Smallest Weight (Step-by-Step)")
        plt.show()


# Define vertices as strings
l1 = "Location 1"
l2 = "Location 2"
l3 = "Location 3"
l4 = "Location 4"
l5 = "Location 5"
l6 = "Location 6"

# Driver code
G = GraphVisualization()
G.addEdge(l1, l2, 2)    # l1 to l2 is 2 miles
G.addEdge(l1, l3, 50)   # l1 to l3 is 50 miles
G.addEdge(l1, l4, 17)   # l1 to l4 is 17 miles
G.addEdge(l1, l5, 0.6)  # l1 to l5 is 0.6 miles
G.addEdge(l1, l6, 41)   # l1 to l6 is 41 miles
G.addEdge(l2, l3, 48)   # l2 to l3 is 48 miles
G.addEdge(l2, l4, 15)   # l2 to l4 is 15 miles
G.addEdge(l2, l5, 1.4)  # l2 to l5 is 1.4 miles
G.addEdge(l3, l4, 33)   # l3 to l4 is 33 miles
G.addEdge(l3, l6, 9)    # l3 to l6 is 9 miles
G.addEdge(l4, l5, 16.4) # l4 to l5 is 16.4 miles
G.addEdge(l4, l6, 24)   # l4 to l6 is 24 miles
G.addEdge(l5, l6, 40.4) # l5 to l6 is 40.4 miles

# Visualize the full graph
plt.figure(1)
graph, positions = G.visualize_full_graph()

# Visualize the corrected greedy path
plt.figure(2)
G.visualize_greedy_path_fixed(graph, positions, l1)
