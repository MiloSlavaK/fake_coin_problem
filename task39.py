# Используя подзадачи и оптимальную стратегию на каждом шаге, найти решение для
# N = 39
# n = 4

from visualization import Node


def build_tree_39():

    root = Node("START")

    w1 = Node(
        "[1..13] vs [14..26]"
    )

    root.add("WEIGH", w1)

    equal = Node(
        "27..39 suspects"
    )

    left = Node(
        "1..13 heavy\n14..26 light"
    )

    right = Node(
        "1..13 light\n14..26 heavy"
    )

    w1.add("=", equal)
    w1.add(">", left)
    w1.add("<", right)

    next_step = Node(
        "Divide into thirds"
    )

    equal.add("NEXT", next_step)
    left.add("NEXT", next_step)
    right.add("NEXT", next_step)

    return root