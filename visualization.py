import matplotlib.pyplot as plt
import networkx as nx


def add_nodes(graph, node, parent=None):

    graph.add_node(node.label)

    if parent:
        graph.add_edge(parent.label, node.label)

    for child in node.children.values():
        add_nodes(graph, child, node)


def visualize_tree(root):

    graph = nx.DiGraph()

    add_nodes(graph, root)

    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(graph, seed=42)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="lightblue",
        font_size=8
    )

    plt.title("Дерево решений")
    plt.show()