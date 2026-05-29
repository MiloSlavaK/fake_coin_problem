from graphviz import Digraph


def node_color(label):

    if "FOUND" in label:
        return "#77DD77"

    if "vs" in label:
        return "#F8BBD0"

    if "states" in label:
        return "#C8E6C9"

    return "#FFFFFF"


class Node:

    def __init__(self, label):

        self.label = label
        self.children = {}

    def add(self, edge, node):

        self.children[edge] = node


def build_graph(graph, node):

    graph.node(
        str(id(node)),
        node.label,
        style="filled",
        fillcolor=node_color(node.label),
        shape="ellipse"
    )

    for edge, child in node.children.items():

        graph.edge(
            str(id(node)),
            str(id(child)),
            label=edge
        )

        build_graph(graph, child)


def save_tree(root, filename):

    graph = Digraph(
        format="png"
    )

    graph.attr(rankdir="TB")

    build_graph(graph, root)

    graph.render(
        filename,
        cleanup=True
    )