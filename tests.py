from information_theory import entropy, max_coins


def test_entropy():

    h = entropy(12)

    assert h > 0

    print("Entropy test passed")


def test_max_coins():

    assert max_coins(3) == 12

    print("Max coins test passed")


if __name__ == "__main__":

    test_entropy()
    test_max_coins()