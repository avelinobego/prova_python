"""
Board game
"""

from player import Player
from house import EmptyState, House, VoidState


class Board(object):

    def __init__(self):
        self.houses = dict()
        self.size = 0
        self.__players = set()
        self.__players_original = set()
        self.stop = False

    def build(self, size=20, step=1):
        self.size = size

        from collections import defaultdict

        empty = House(0, self, VoidState)

        self.houses = defaultdict(
            lambda: empty, {k: House(1000, self, EmptyState) for k in range(1, size + 1, step)})

    def move_player(self, player, die_value):
        """
        Move um jogador de posicao
        """

        if self.stop:
            return

        if player in self.__players:
            player.position += die_value
            while player.position > self.size:
                # Completou uma volta
                player.amount += 100.0
                player.position -= self.size

            self.houses[player.position].add_player(player)

    def add_player(self, player):
        self.__players.add(player)
        self.__players_original.add(player)

    def remove_player(self, player):
        self.__players.discard(player)
        self.stop = len(self.__players) == 1

    def has_player(self, player):
        return player in self.__players

    def winner(self):
        if len(self.__players) == 1:
            return list(self.__players)[0]
        else:
            return None

    def reset(self):
        self.stop = False
        self.__players = set(self.__players_original)
        for player in self.__players:
            player.reset()

        for _, house in self.houses.items():
            house.state = EmptyState
            house.owner = None

    def __repr__(self):
        return "Board()"
