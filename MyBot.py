from Player import Player
from Board import Board
import numpy as np
from random import randint

class MyBotRandom(Player):          #erster Bot, der zufälligen Spielzug spielt
    def __init__(self, number):
        self.number = number        #1 oder 2, wird bei make_move() als Setzstein übergeben, Spieler markiert mit seiner Nummer auf dem Feld

    def make_move(self, board = Board):                                     #lässt Bot spielen, benötigt allerdings eigene make_move Methode, da Verfahren anders
        x_coordinate = randint(0,4)                                         #generiert eine beliebige x-Koordinate, die auf dem Spielfeld liegen kann
        y_coordinate = randint(0,4)                                         #generiert eine beliebige y-Koordinate, die auf dem SPielfeld liegen kann
        while board.array[y_coordinate][x_coordinate] != 0:                 #sollte das Feld auf dem Spielfeld schon belegt (!= 0) sein:
            x_coordinate = randint(0,4)                                     #andere zufällige x-Koordinate wird generiert
            y_coordinate = randint(0,4)                                     #andere zufällige y-Koordinate wird generiert

        board.set_field_value(y_coordinate, x_coordinate, self.number)      #methode def. in Board-Klasse, markiert Spielzug auf dem Spielbrett
        return board.array                                                  #gibt das aktualisierte Spielbrett zurück

class MyBotReactive(Player):                                                #zweiter Bot, der reaktiv spielt
    def __init__(self, number):                                         
        self.number = number                                                #Spielstein, mit dem der Bot seine Markierungen auf Spielfeld Board setzt
        self.possible_moves = []                                            #Liste, die alle sinnvollen Spielzüge (also Markierungen auf Borad) speichert und aus der später ein Zug ausgeführt werden soll
    
    def make_random_move(self, board):                                      #Methode aus MyBotRandom, ermöglicht zufälligen Spielzug des Bots
        x_coordinate = randint(0,4)
        y_coordinate = randint(0,4)
        while board.array[y_coordinate][x_coordinate] != 0:
            x_coordinate = randint(0,4)
            y_coordinate = randint(0,4)

        board.set_field_value(y_coordinate, x_coordinate, self.number)
        return board.array
        
    #def make_move(self, board=Board):                                       #erneut eigene Methode, da Verfahren auch hier wieder anders zu vorherigen
                                                                             #kein diagonaler Check auf mögliche Spielzüge (es muss ja noch Luft nach oben sein :))
         #self.check_horizontally(board)                                     #prüft auf spezielle Markierungsmuster auf horizontaler Ebene auf Spielfeld
      #  #self.check_vertically(board)                                       #prüft auf spezielle Markierungsmuster auf vertikaler Ebene auf Spielfeld
       # print("Bot setzt hier: ")
        #if self.possible_moves == []:                                       #sollten keine besorgniserregenden Spielzüge des Gegners, die Eingreifen des Bots bedarfen, vorhanden sein:
         #   self.make_random_move(board)                                    #dann soll ein zufälliger Zug gespielt werden
        #else:                                                               #falls es doch eine der in check-Methoden definierten Situationen geben: 
         #   random_num = randint(0, len(self.possible_moves))               #generiert eine zufällige Zahl zwischen 0 und der Länge der Liste mit sinnvollen Spielzügen
          #  print(self.possible_moves)
           # board.set_field_value(self.possible_moves[random_num - 1])     #sucht aus der Liste mit sinnvollen Spielzügen durch zuvorige "Zufalls"-Zahl einen Spielzug aus und führt diesen durch
           


#    def check_horizontally(self, board=Board):
#        self.possible_moves = []                                                      #um alte Spieloptionen zu löschen
#        for row in board.array:                                                       #für jede Reihe in board.array
#            for i in range(len(row) -3):                                              #für jedes Element in der Reihe
#                if row[i] != 0:                                                       #wenn das Element nicht 0 ist                                         
#                    if (row[i] == row[i + 1]):                                        #wenn 2 Elemente in Folge gleich sind
#                        if i + 2 > 4:
#                            if row[i-1] == 0:
#                                self.possible_moves.append((row, i-1))
#                            else:
#                                pass
#                        else:
#                            if row[i + 2] == 0:
#                                self.possible_moves.append((row, i+2))
#                            else:
#                                pass
#                    else: 
#                        pass
#                else: 
#                    pass


#WORKING
    def make_move(self, board):
        self.check_horizontally(board)
        self.check_vertically
        if self.possible_moves == []:
            print("Bot setzt hier: ")
            self.make_random_move(board)
            return board.array
        else: 
            random_number = randint(0, len(self.possible_moves) - 1)
            print(f"mögliche Züge in Array-Index-Form: {self.possible_moves}")
            print("Bot setzt hier: ")
            board.set_field_value(self.possible_moves[random_number][0], self.possible_moves[random_number][1], self.number)
            self.possible_moves = []
            return board.array
        
    def check_horizontally(self, board):                     
        for row_index in range(len(board.array)):       #für spätere Indexierung des Arrays für speichern des möglichen Zuges
            row = board.array[row_index]                #zur Verbesserung der übersichtlichkeit
            for element in range(len(row) - 1):           #nur elemente in der Reihe
                if row[element] != 0 and row[element] != self.number and element < 4:   #Feld von Gegner belegt und nicht am Rand
                    if row[element] == row[element + 1] and row[element + 2] == 0:     #2 Felder in Folge vom Gegner belegt und 3. Feld frei
                        self.possible_moves.append((row_index, element + 2))
                    elif row[element] == row[element + 1] and row[element - 1] == 0:    #2 Felder in Folge vom Gegner belegt und Feld davor frei
                        self.possible_moves.append((row_index, element - 1))
                    else:
                        pass
                elif row[element] != 0 and row[element] != self.number and element == 4: #Feld von Gegner belegt und am Rand
                    if row[element] == row[element - 1] and row[element - 2] == 0: 
                        self.possible_moves.append((row_index, element - 2))
                    else:
                        pass
                else:
                    pass
                

    def check_vertically(self, board):       
        transposed_board = np.transpose(board.array)         #flippt das board um 90° -> die Spalten werden zu Zeilen              
        for row_index in range(len(transposed_board)):       #für spätere Indexierung des Arrays für speichern des möglichen Zuges
            row = transposed_board[row_index]                #zur Verbesserung der übersichtlichkeit
            for element in range(len(row) - 1):              #nur elemente in der Reihe
                if row[element] != 0 and row[element] != self.number and element < 4:   #Feld von Gegner belegt und nicht am Rand
                    if row[element] == row[element + 1] and row[element + 2] == 0:      #2 Felder in Folge vom Gegner belegt und 3. Feld frei
                        self.possible_moves.append((element + 2, row_index, ))
                    elif row[element] == row[element + 1] and row[element - 1] == 0:    #2 Felder in Folge vom Gegner belegt und Feld davor frei
                        self.possible_moves.append((element - 1, row_index, ))
                    else:
                        pass
                elif row[element] != 0 and row[element] != self.number and element == 4: #Feld von Gegner belegt und am Rand
                    if row[element] == row[element - 1] and row[element - 2] == 0: 
                        self.possible_moves.append((element - 2, row_index))
                    else:
                        pass
                else:
                    pass



#    def check_vertically(self, board=Board):
#        self.possible_moves = []                                                      #um alte Spieloptionen zu löschen
#        transposed_board = np.transpose(board.array)                                  #flippt das board um 90° -> die Spalten werden zu Zeilen                             
#        for row in transposed_board:                                                  #für jede Reihe in board.array
#            for i in range(len(row) -2):                                              #für jedes Element in der Reihe
#                if row[i] != 0:                                                       #wenn das Element nicht 0 ist                                         
#                    if (row[i] == row[i + 1]):                                        #wenn 2 Elemente in Folge gleich sind
#                        if i+2 > 4:
#                            if row[i-1] == 0:
#                                self.possible_moves.append((row, i-1))
#                            else:
#                                pass
#                        else:
#                            if row[i + 2] == 0:
#                                self.possible_moves.append((row, i+2))
#                            else:
#                                pass
#                    else: 
#                        pass
#                else: 
#                    pass                                          
        


