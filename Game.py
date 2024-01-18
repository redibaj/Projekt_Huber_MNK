from Board import Board                                            
from Player import Player
from MyBotRandoms import MyBotRandom
from MyBotReactive import MyBotReactive
from MyBotRandoms import MyBot2

class Game:
    def __init__(self, m=5, n=5, k=4, player1=None, player2=None):                                                              
        self.m = m                                                                                  
        self.n = n                                                                                  
        self.k = k                                                                                  
        self.board = Board()                                                                        
        self.player1 = player1                             
        self.player2 = player2                           
    
    def start(self): 
        '''Fragt nach Spielmodus und Spielernamen, startet anschl. das Spiel'''                                                                              
        print("Willkommen! Wie möchtest du spielen?\nPlayer vs. Player [1] / Player vs. Bot [2]")    
        choice = input(">>> ")                                                                     
        if choice == "1":    
            self.player1 = Player(name=input("Name Spieler 1: "), number=1)                             
            self.player2 = Player(name=input("Name Spieler 2: "), number=2)                                                                        
            self.game_loop()                                                                        
        elif choice == "2":                                                                       
            print("Welches Level soll der Bot haben? Random [1] / Low-Level [2] / High-Level [3]")                            
            bot_level = input(">>> ")                                                              
            if bot_level == "1": 
                self.player1 = Player(name=input("Name Spieler 1: "), number=1)                                                                  
                self.player2 = MyBotRandom(number=2)                                               
                print()
                print(
                    "Einleitung\nDas Spielfeld besteht aus 5x5 Feldern.\n",
                    "Ein leeres Feld wird durch eine 0 gekennzeichnet, ein belegtes Feld durch eine 1 oder 2.\n",
                    "Spielt ihr zu zweit, so belegt Spieler 1 das Feld mit einer 1 und Spieler 2 mit einer 2.\n", 
                    "Spielst du alleine, so legst du automatisch die 1 und der Computer die 2.\n",
                    "Du kannst Werte zwischen 1 und 5 angeben.\nDer erste Wert beschreibt die Horizontale, der zweite die Vertikale\n",
                    "Die Eingabe ähnelt der bei 'Schiffe versenken'\n",
                    "Die Werte dürfen nicht in einer Klammer stehen!\n"
                    )
                self.game_loop()                                                                   
            elif bot_level == "2":      
                self.player1 = Player(name=input("Name Spieler 1: "), number=1)                                                                 
                self.player2 = MyBot2(number=2)                                             
                print()
                print(
                    "Einleitung\nDas Spielfeld besteht aus 5x5 Feldern.\n",
                    "Ein leeres Feld wird durch eine 0 gekennzeichnet, ein belegtes Feld durch eine 1 oder 2.\n",
                    "Spielt ihr zu zweit, so belegt Spieler 1 das Feld mit einer 1 und Spieler 2 mit einer 2.\n", 
                    "Spielst du alleine, so legst du automatisch die 1 und der Computer die 2.\n",
                    "Du kannst Werte zwischen 1 und 5 angeben.\nDer erste Wert beschreibt die Horizontale, der zweite die Vertikale\n",
                    "Die Eingabe ähnelt der bei 'Schiffe versenken'\n",
                    "Die Werte dürfen nicht in einer Klammer stehen!\n"
                    )
                self.game_loop()                                                                    
            elif bot_level == "3":
                self.player1 = Player(name=input("Name Spieler 1: "), number=1)               
                self.player2 = MyBotReactive(number=2)                                                     
                print()
                print(
                    "Einleitung\nDas Spielfeld besteht aus 5x5 Feldern.\n",
                    "Ein leeres Feld wird durch eine 0 gekennzeichnet, ein belegtes Feld durch eine 1 oder 2.\n",
                    "Spielt ihr zu zweit, so belegt Spieler 1 das Feld mit einer 1 und Spieler 2 mit einer 2.\n", 
                    "Spielst du alleine, so legst du automatisch die 1 und der Computer die 2.\n",
                    "Du kannst Werte zwischen 1 und 5 angeben.\nDer erste Wert beschreibt die Horizontale, der zweite die Vertikale\n",
                    "Die Eingabe ähnelt der bei 'Schiffe versenken'\n",
                    "Die Werte dürfen nicht in einer Klammer stehen!\n"
                    )
                self.game_loop()                                                                    
        

    def game_loop(self):        
        '''Startet die Partie
        
        Solange kein Gewinner feststeht und Spielfeld nicht voll ist, wird das Spiel fortgesetzt.
        Board wird angezeigt, Spieler setzt Stein, Board prüft auf Gewinner und volles Spielfeld.
        Wenn Gewinner feststeht oder Spielfeld voll ist, wird das Board angezeigt und das Spiel beendet.
        Andernfalls zieht der nächste Spieler.
        '''                              
        print("Lasset die Spiele beginnen!")                 
        winner = False                                       
        full_board = False                                    
        while winner == False and full_board == False:       
            self.board.display()                             
            print()
            self.player1.make_move(board=self.board)          
            winner = self.board.has_won()                   
            full_board = self.board.board_full()
            if winner == True:                               
                print()
                self.board.display()
                break                                         
            if full_board == True:                            
                print()
                self.board.display()                          
                print("Unentschieden!")                       
                break                                         
            self.board.display()                              
            print()
            full_board = self.board.board_full()             
            self.player2.make_move(board=self.board)          
            winner = self.board.has_won()                    
            full_board = self.board.board_full()
            if winner == True:                               
                print()
                self.board.display()                        
                break                                        
            if full_board == True:                           
                print("Unentschieden!")                       
                print()
                self.board.display()
                break                                         
        print("\nSpiel vorbei")                               

game1=Game()
game1.start()


def game_sim(number):
    '''Simuliert Spiele zwischen Bots
    
    Simuliert eine bestimmte Anzahl an Spielen zwischen zwei Bots.
    Die Anzahl der Spiele wird als Parameter übergeben.
    Die Ergebnisse werden in eine CSV-Datei geschrieben.
    '''
    with open("game_sim.csv", "w") as doc_file:
        doc_file.write("MyBotRandom vs. MyBotReactive\nStarter: MyBotRandom\n\n")
    
    winner = []
    count_bot_1 = 0
    count_bot_2 = 0
    count_draw = 0
    for i in range(number):
        game=Game(player1=MyBotRandom(number=1), player2=MyBotReactive(number=2))
        game.game_loop()
        if game.board.has_won_diagonally() or game.board.has_won_horizontally() or game.board.has_won_vertically():
            winner.append(game.board.winner)
        elif game.board.board_full():
            winner.append(None)    
    
    for i in winner:
        if i == 1:
            count_bot_1 += 1
            doc_file.write("Bot 1\n")
        elif i == 2:
            count_bot_2 += 1
            doc_file.write("Bot 2\n")
        elif i == {1}:
            count_bot_1 += 1
            doc_file.write("Bot 1\n")
        elif i == {2}:
            count_bot_2 += 1
            doc_file.write("Bot 2\n")
        elif i == None:
            count_draw += 1
            doc_file.write("Draw\n")

    print("\nSieger:")
    print(f"Bot 1: {count_bot_1}\nBot 2: {count_bot_2}\nDraw: {count_draw}")


#game_sim(100)
