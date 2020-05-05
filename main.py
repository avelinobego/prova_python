
from random import randint, seed
from player import Player
from player import CautiousBehavior, ImpulsiveBehavior, RandomBehavior, DemandingBehavior
from board import Board
from time import sleep


def die():
    result = randint(1, 6)
    return result


if __name__ == "__main__":
    board = Board()
    board.build(size=100, step=5)

    player1 = Player("player1", board, ImpulsiveBehavior)
    player2 = Player("player2", board, DemandingBehavior)
    player3 = Player("player3", board, CautiousBehavior)
    player4 = Player("player4", board, RandomBehavior)

    summarize = {player1: 0, player2: 0, player3: 0, player4: 0}

    winners = []
    timeout_count = 0

    for rounds in range(1000):

        timeout = True

        for game in range(300):

            board.move_player(player1, die())
            board.move_player(player2, die())
            board.move_player(player3, die())
            board.move_player(player4, die())

            if board.stop:
                timeout = False
                break

        if timeout:
            timeout_count += 1

        winners.append(board.winner())

        board.reset()

    print(f"Timouts: {timeout_count}")

    for p in winners:
        summarize[p] += 1

    podium = sorted(summarize.items(), key = lambda e: e[1], reverse = True)
    
    print("Podium")
    for e in podium:
        print(e)
    
