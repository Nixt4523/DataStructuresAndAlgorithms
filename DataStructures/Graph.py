# Graphs
"""
Graphs is not a Linear Data Structure
It consists of Nodes(Vertex) and Edges
Each node have connections the other node these connections are called Edges
Types of Graphs
Directed Graphs: In this graph you can only traverse in one direction
Undirected Graphs: In this graph you can traverse both back and forth nodes
Weighted Graphs : In this graph you can also have information in the Edges
Unweighted Graphs : In this graph Edges does not contain any information
Cyclic Graphs : In this graph you have some Nodes that are connected in a Cyclical way
Acyclic Graphs : In this graph Nodes are not connected in a Cyclical way
"""

# Ways to build Graphs
'''
Edge List : graph = [[0, 2], [2, 3], [2, 1], [1, 3]]
            In Edge list we store the connection between 2 nodes
Adjacent List : {0 : [2], 1: [2, 3], 2 : [0, 1, 3], 3 : [1, 2]}
              In Adjacent list we store each node in Hashmap as a key,
              and all the connections in an array as its value
'''

# Implementing Graphs in Python
class Graph:

    def __init__(self):
        self.num_of_nodes = 0
        self.adjacent_list = {}

    def add_node(self, node):

        self.adjacent_list[node] = []
        self.num_of_nodes += 1

    def add_edge(self, node1, node2):

        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def print_graph(self):
        print(self.adjacent_list)


'''
We can initialize the Graph i.e Graph()
We can use methods in Graph class to manipulate the Graph
'''