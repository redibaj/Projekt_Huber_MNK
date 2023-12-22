from Board import Board                                            #alle notwendigen Klassen-Importe 
from Player import Player
from MyBotRandoms import MyBotRandom
from MyBotReactive import MyBotReactive
from MyBotRandoms import MyBot2

class Game:
    def __init__(self, m=5, n=5, k=4, player1=None, player2=None):                                                              #setz m,n und k default-mäßig auf 5,5 und 4 (Spiel funktioniert auch nur so)
        self.m = m                                                                                  #definiert m-Wert
        self.n = n                                                                                  #definiert n-Wert
        self.k = k                                                                                  #definiert k-Wert
        self.board = Board()                                                                        #Spielfeld ein Objekt der Klasse Board
        self.player1 = player1                             #Spieler1 = Objekt der Klasse Spieler mit dem Namen, den der Spieler selbst eingibt
        self.player2 = player2                             #Spieler2 = Objekt der Klasse Spieler mit dem Namen, den der Spieler selbst eingibt
    
    def start(self):                                                                                #Methode, die vor eigenltichem Spielstart die gewünschten Parameter abfragt
        print("Wilkommen! Wie möchtest du spielen?\nPlayer vs. Player [1] / Player vs. Bot [2]")    #Begrüßung und Wahl der Spielart
        choice = input(">>> ")                                                                      #Spieler wählt Spielart
        if choice == "1":    
            self.player1 = Player(name=input("Name Spieler 1: "), number=1)                             #Spieler1 = Objekt der Klasse Spieler mit dem Namen, den der Spieler selbst eingibt
            self.player2 = Player(name=input("Name Spieler 2: "), number=2)                                                                        #wenn Spieler vs. Spieler gewählt:
            self.game_loop()                                                                        #game-loop wird gestartet
        elif choice == "2":                                                                         #wenn Spieler vs. Bot gewählt: 
            print("Welches Level soll der Bot haben? [1] / [2]")                                    #Frage nach gwünschtem Bot-Levels / der Schwierigkeitsstufe des Bots
            bot_level = input(">>> ")                                                               #Eingabe des Spielers
            if bot_level == "1": 
                self.player1 = Player(name=input("Name Spieler 1: "), number=1)                                                                   #wenn einfacher Bot (Level 1)
                self.player2 = MyBotRandom(number=2)                                                #zweiter Spieler wird durch Bot Level 1 ersetzt, dieser bekommt Spielernummer/-markierung 2
                print()
                self.game_loop()                                                                    #game-loop wird gestartet
            elif bot_level == "2":      
                self.player1 = Player(name=input("Name Spieler 1: "), number=1)                                                                   #wenn schwierigerer Bot (Level 2)
                self.player2 = MyBotReactive(number=2)                                              #Spieler 2 wird durch Bot Level 2 mit Spielernummer/-markierung 2 ersetzt
                print()
                print("Einleitung\nDas Spielfeld besteht aus 5x5 Feldern.\nEin leeres Feld wird durch eine 0 gekennzeichnet, ein belegtes Feld durch eine 1 oder 2.\nSpielt ihr zu zweit, so belegt Spieler 1 das Feld mit einer 1 und Spieler 2 mit einer 2.\nSpielst du alleine, so legst du automatisch die 1 und der Computer die 2.\nDu kannst Werte zwischen 1 und 5 angeben.\nDer erste Wert beschreibt die Horizontale, der zweite die Vertikale\nDie Eingabe ähnelt der bei 'Schiffe versenken'\nDie Werte dürfen nicht in einer Klammer stehen!\n")
                self.game_loop()                                                                    #game-loop wird gestartet
        

    def game_loop(self):                                      #Methode für den eigentlichen Vorgang des Spiels
        print("Lasset die Spiele beginnen!")                  #Eingangsstatement, dass nun begonnen werden kann
        winner = False                                        #es wird festgelegt, dass es zu Beginn keinen Gewinner gibt
        full_board = False                                    #es wird gespeichert, dass das Board zu Beginn noch nicht voll ist
        while winner == False and full_board == False:        #solange es keinen Gewinner gibt und das Spielfeld nicht voll ist soll gespielt werden
            self.board.display()                              #Spielfeld wird für Spieler sichtbar
            print()
            self.player1.make_move(board=self.board)          #Spieler 1 macht einen Zug
            winner = self.board.has_won()                     #es wird mit Methode aus Board-Klasse überprüft, ob es einen Gewinner gibt (falls ja, würde hier True zurückgegeben werden)
            full_board = self.board.board_full()
            if winner == True:                                #sollte es einen Gewinner geben:
                print()
                self.board.display()
                break                                         #Spiel wird beendet
            if full_board == True:                            #prüft, ob das es noch freie Stellen auf dem Spielfeld gibt (falls nicht, wird False zurückgegeben). Falls Feld voll sein sollte: 
                print()
                self.board.display()                          #zeigt ein letztes Mal das Spielfeld (es werden alle Felder belegt sein) 
                print("Unentschieden!")                       #signalisiert das dadurch entstandene Unentschieden
                break                                         #Spiel wird beendet
            self.board.display()                              #falls keine der beiden zuvorigen Bedingungen erfüllt ist, wird hier weitergemacht und das aktualisiert Spielfeld angezeigt, damit der nächste Spiele eine faire Chance auf einen guten Zug hat
            print()
            full_board = self.board.board_full()              #schaut, ob das Spielfeld voll ist und speichert aktualisierten Boolean-Return-Wert in Variable full_board
            self.player2.make_move(board=self.board)          #zweiter Spieler setzt
            winner = self.board.has_won()                     #es wird mit Methode aus Board-Klasse überprüft, ob es einen Gewinner gibt (falls ja, würde hier True zurückgegeben und gespeichert werden)
            full_board = self.board.board_full()
            if winner == True:                                #sollte es einen Gewinner geben (bzw. die vorher definierten, dafür notwendigen Bedigungen erfüllt sein)
                print()
                self.board.display()                          #zeigt ein letztes Mal das Spielfeld an
                break                                         #beendet Spiel an dieser Stelle
            if full_board == True:                            #sollte das Spielfeld keine freien Stellen mehr haben und dadurch kein Zug mehr möglich sein: 
                print("Unentschieden!")                       #signalisiert das dadurch entstandene Unentschieden
                print()
                self.board.display()
                break                                         #beendet das Spiel
        print("\nSpiel vorbei")                                 #sobald Bedingungen der While-Schleife nicht mehr erfüllt sind, geht es hier weiter. Letzte Aktion ist diese Print-Ausgabe

#game1=Game()
#game1.start()


def game_sim(number):
    winner = []
    count_bot_1 = 0
    count_bot_2 = 0
    count_draw = 0
    for i in range(number):
        game=Game(player1=MyBot2(number=1), player2=MyBotReactive(number=2))
        game.game_loop()
        if game.board.has_won_diagonally() or game.board.has_won_horizontally() or game.board.has_won_vertically():
            winner.append(game.board.winner)
        elif game.board.board_full():
            winner.append(None)    
    
    for i in winner:
        if i == 1:
            count_bot_1 += 1
        elif i == 2:
            count_bot_2 += 1
        elif i == {1}:
            count_bot_1 += 1
        elif i == {2}:
            count_bot_2 += 1
        elif i == None:
            count_draw += 1

    print("\nSieger:")
    print(f"Bot 1: {count_bot_1}\nBot 2: {count_bot_2}\nDraw: {count_draw}\n")


game_sim(100)
