# Для найти решение, если известно, что фальшивая монета легче остальных
# N = 27
# n = 3

from visualization import Node


def build_tree_27():

    root = Node("START")

    w1 = Node(
        "[1..9] vs [10..18]"
    )

    root.add("WEIGH", w1)

    g1 = Node("1..9")
    g2 = Node("10..18")
    g3 = Node("19..27")

    w1.add("<", g1)
    w1.add(">", g2)
    w1.add("=", g3)

    w2 = Node(
        "[1 2 3] vs [4 5 6]"
    )

    g1.add("NEXT", w2)

    final = Node(
        "1 vs 2"
    )

    w2.add("NEXT", final)

    found = Node(
        "FOUND"
    )

    final.add("DONE", found)

    return root