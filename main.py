from visualization import save_tree

from task12 import build_tree_12
from task39 import build_tree_39
from task27 import build_tree_27


def main():

    tree12 = build_tree_12()

    save_tree(
        tree12,
        "trees/tree_12"
    )

    print(
        "tree_12.png created"
    )

    tree39 = build_tree_39()

    save_tree(
        tree39,
        "trees/tree_39"
    )

    print(
        "tree_39.png created"
    )

    tree27 = build_tree_27()

    save_tree(
        tree27,
        "trees/tree_27"
    )

    print(
        "tree_27.png created"
    )


if __name__ == "__main__":
    main()