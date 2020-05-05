from random import randint


class ImpulsiveBehavior:

    @staticmethod
    def name():
        return "Impulsive"

    @staticmethod
    def buy_house(player, house):
        player.amount -= house.value
        if player.board.has_player(player):
            house.owner = player
            house.solded()

    @staticmethod
    def rent_house(player, house):
        if player.board.has_player(player) and house.owner != player:
            dif = player.amount - house.value
            house.owner.value = dif
            player.amount -= dif


class DemandingBehavior:

    @staticmethod
    def name():
        return "Demanding"

    @staticmethod
    def buy_house(player, house):
        if house.value > 50.0:
            ImpulsiveBehavior.buy_house(player, house)

    @staticmethod
    def rent_house(player, house):
        if house.value > 50.0:
            ImpulsiveBehavior.rent_house(player, house)


class CautiousBehavior:

    @staticmethod
    def name():
        return "Cautious"

    @staticmethod
    def buy_house(player, house):
        if player.amount > 80.0:
            ImpulsiveBehavior.buy_house(player, house)

    @staticmethod
    def rent_house(player, house):
        if player.amount > 80.0:
            ImpulsiveBehavior.rent_house(player, house)


class RandomBehavior:

    @staticmethod
    def name():
        return "Random"

    @staticmethod
    def buy_house(player, house):
        prob = randint(1, 2)
        if prob == 1:
            ImpulsiveBehavior.buy_house(player, house)

    @staticmethod
    def rent_house(player, house):
        prob = randint(1, 2)
        if prob == 1:
            ImpulsiveBehavior.rent_house(player, house)


class Player(object):
    def __init__(self, name, board, state):
        self.name = name
        self.__behavior = state
        board.add_player(self)
        self.board = board
        self.reset()

    def buy_house(self, house):
        self.__behavior.buy_house(self, house)

    def rent_house(self, house):
        self.__behavior.rent_house(self, house)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value
        if value <= 0.0:
            del self.amount

    @amount.deleter
    def amount(self):
        self.board.remove_player(self)

    def reset(self):
        self.position = 0
        self.__amount = 500.0

    def __repr__(self):
        return f"Name: {self.name}, Type: {self.__behavior.name()}"

    def __hash__(self):
        return hash(self.name)
