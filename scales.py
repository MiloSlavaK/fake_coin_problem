class Scales:
    """
    Модель рычажных весов.
    """

    def __init__(self, fake_coin, fake_type):
        """
        fake_coin - номер фальшивой монеты
        fake_type - "heavy" или "light"
        """

        self.fake_coin = fake_coin
        self.fake_type = fake_type

    def weigh(self, left, right):
        """
        Возвращает:
        -1 -> левая легче
         0 -> равновесие
         1 -> левая тяжелее
        """

        left_weight = len(left)
        right_weight = len(right)

        if self.fake_coin in left:
            if self.fake_type == "heavy":
                left_weight += 1
            else:
                left_weight -= 1

        if self.fake_coin in right:
            if self.fake_type == "heavy":
                right_weight += 1
            else:
                right_weight -= 1

        if left_weight > right_weight:
            return 1

        if left_weight < right_weight:
            return -1

        return 0