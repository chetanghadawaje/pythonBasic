"""
Template method design pattern is to define an algorithm as a skeleton of operations and leave the details to be implemented by the child
classes. The overall structure and sequence of the algorithm are preserved by the parent class.

Hear run() method this template method.
"""

from abc import ABC


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players

    def run(self):
        self.start()
        print(f"{self.winning_player} Wins!")

    def start(self): pass

    @property
    def winning_player(self): pass


class Cricket(Game):
    def __init__(self):
        super().__init__(11)

    def start(self):
        print("Cricket game start")

    @property
    def winning_player(self):
        return "Chetan"


game = Cricket()
game.run()

"""
O/P:
Cricket game start
Chetan Wins!
"""