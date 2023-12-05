from Board import Board
from Player import Player
class Game:
    def __init__(self, m=5, n=5, k=4):
        self.m = m
        self.n = n
        self.k = k
        self.board = Board()
        self.player1 = Player(name=input("Name Spieler 1: "), number=1)
        self.player2 = Player(name=input("Name Spieler 2: "), number=2)
    
    def start(self):
        pass

    def game_loop(self):
        print("Lasset die Spiele beginnen!")
        winner = False
        while winner == False:
            self.board.display()
            self.player1.make_move(board=self.board)
            winner = self.board.has_won()
            if winner == True:
                break
            self.board.display()
            self.player2.make_move(board=self.board)
            winner = self.board.has_won()
            if winner == True:
                break
        print("Spiel vorbei")