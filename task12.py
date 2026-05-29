# Используя подзадачи и оптимальную стратегию на каждом шаге, найти решение для
# N = 12
# n = 3
from scales import Scales

from visualization import Node


def build_tree_12():

    root = Node("START")

    w1 = Node(
        "[1 2 3 4] vs [5 6 7 8]"
    )

    root.add("WEIGH", w1)

    equal = Node(
        "9 10 11 12 suspects"
    )

    left = Node(
        "1-4 heavy\n5-8 light"
    )

    right = Node(
        "1-4 light\n5-8 heavy"
    )

    w1.add("=", equal)
    w1.add(">", left)
    w1.add("<", right)

    w2 = Node(
        "[9 10 11] vs [1 2 3]"
    )

    equal.add("WEIGH", w2)

    found12 = Node(
        "FOUND 12"
    )

    heavy_group = Node(
        "9 10 11 heavy"
    )

    light_group = Node(
        "9 10 11 light"
    )

    w2.add("=", found12)
    w2.add(">", heavy_group)
    w2.add("<", light_group)

    return root