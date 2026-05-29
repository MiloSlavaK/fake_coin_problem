import math


def entropy(n):
    """
    Энтропия задачи:
    H = log2(2n)
    """

    return math.log2(2 * n)


def max_coins(k):
    """
    Максимальное число монет
    для k взвешиваний:
    n <= (3^k - 3) / 2
    """

    return (3 ** k - 3) // 2


if __name__ == "__main__":

    for k in range(1, 5):
        print(
            f"{k} взвешивания -> "
            f"{max_coins(k)} монет"
        )