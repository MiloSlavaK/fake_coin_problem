from scales import Scales


class TreeNode:
    def __init__(self, label):
        self.label = label
        self.children = {}


class FakeCoinSolver:

    def __init__(self, n):
        self.n = n

        # пример:
        self.fake_coin = 5
        self.fake_type = "heavy"

        self.scales = Scales(
            self.fake_coin,
            self.fake_type
        )

        self.tree = TreeNode("START")

    def solve(self):

        coins = list(range(1, self.n + 1))

        return self._solve_recursive(
            coins,
            self.tree
        )

    def _solve_recursive(self, coins, node):

        # Базовый случай
        if len(coins) == 1:
            result = f"Монета {coins[0]} фальшивая"

            child = TreeNode(result)
            node.children["FOUND"] = child

            return result

        third = len(coins) // 3

        left = coins[:third]
        right = coins[third:2 * third]
        rest = coins[2 * third:]

        outcome = self.scales.weigh(left, right)

        weigh_label = f"{left} vs {right}"

        weigh_node = TreeNode(weigh_label)

        node.children[str(outcome)] = weigh_node

        if outcome == 0:
            next_coins = rest

        elif outcome == 1:
            next_coins = left + right

        else:
            next_coins = left + right

        return self._solve_recursive(
            next_coins,
            weigh_node
        )