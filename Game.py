from Board import Board
from Player import Player
from MyBot import MyBotRandom
from MyBot import MyBotReactive
class Game:
    def __init__(self, m=5, n=5, k=4):
        self.m = m
        self.n = n
        self.k = k
        self.board = Board()
        self.player1 = Player(name=input("Name Spieler 1: "), number=1)
        self.player2 = Player(name=input("Name Spieler 2: "), number=2)
    
    def start(self):
        print("Wilkommen! Wie möchtest du spielen?\nPlayer vs. Player [1] / Player vs. Bot [2]")
        choice = input(">>> ")
        if choice == "1":
            self.game_loop()
        elif choice == "2":
            print("Welches Level soll der Bot haben? [1] / [2]")
            bot_level = input(">>> ")
            if bot_level == "1":
                self.player2 = MyBotRandom(number=2)
                self.game_loop()
            elif bot_level == "2":
                self.player2 = MyBotReactive(number=2)
                self.game_loop()
        

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

game1=Game()
game1.start()