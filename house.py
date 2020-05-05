"""
House
"""


class VoidState(object):

    @staticmethod
    def add_player(house, player):
        pass


class EmptyState(object):

    @staticmethod
    def add_player(house, player):
        player.buy_house(house)


class SoldedState(object):

    @staticmethod
    def add_player(house, player):
        player.rent_house(house)


class House(object):

    def __init__(self, value, board, state):
        self.board = board
        self.__state = state
        self.value = value
        self.owner = None

    def solded(self):
        self.state = SoldedState

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @state.deleter
    def state(self):
        self.__state = EmptyState

    def add_player(self, player):
        self.state.add_player(self, player)

    def __repr__(self):
        return f"House({self.board}, {self.__state})"
