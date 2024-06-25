from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create nodes for the expression ((2 + 5) / 3) - (3 + 8)
root = Node('-')

# Left subtree ((2 + 5) / 3)
root.left = Node('/')
root.left.left = Node('+')
root.left.left.left = Node('2')
root.left.left.right = Node('5')
root.left.right = Node('3')

# Right subtree (3 + 8)
root.right = Node('+')
root.right.left = Node('3')
root.right.right = Node('8')

# Initialize graphviz Digraph
dot = Digraph()
dot.attr('node', shape='circle')

# Function to add nodes and edges to the graph
def add_nodes_edges(node, graph):
    if node:
        graph.node(node.value)
        if node.left:
            graph.edge(node.value, node.left.value)
            add_nodes_edges(node.left, graph)
        if node.right:
            graph.edge(node.value, node.right.value)
            add_nodes_edges(node.right, graph)

# Add nodes and edges to the graph
add_nodes_edges(root, dot)

# Save the graph to a file and render it
dot.render('binary_expression_tree_simple', format='png', view=True)
