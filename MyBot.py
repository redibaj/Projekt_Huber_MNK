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
        self.possible_moves = []
        self.gefilterte_liste = []
        self.important_moves = []
                                       #Liste, die alle sinnvollen Spielzüge (also Markierungen auf Borad) speichert und aus der später ein Zug ausgeführt werden soll
    
    def make_random_move(self, board):                                      #Methode aus MyBotRandom, ermöglicht zufälligen Spielzug des Bots
        x_coordinate = randint(0,4)
        y_coordinate = randint(0,4)
        while board.array[y_coordinate][x_coordinate] != 0:
            x_coordinate = randint(0,4)
            y_coordinate = randint(0,4)
        print(f"Bot setzt random hier: {x_coordinate + 1, 5 - y_coordinate}")
        board.set_field_value(y_coordinate, x_coordinate, self.number)
        print()
        return board.array
        

    def make_move(self, board):
        self.check_horizontally(board)
        self.check_vertically(board)
        self.check_diagonally(board)
        self.gefilterte_liste = [tupel for tupel in self.possible_moves if 0 not in tupel and 4 not in tupel]
        if self.possible_moves == [] and self.important_moves == []:
            self.make_random_move(board)
            return board.array
        elif self.gefilterte_liste == [] and self.important_moves == []: 
            random_number = randint(0, len(self.possible_moves) - 1)
            print(f"mögliche Züge in Array-Index-Form in possible_moves: {self.possible_moves}")
            print("Bot setzt hier: ")
            board.set_field_value(self.possible_moves[random_number][0], self.possible_moves[random_number][1], self.number)
            print()
            self.possible_moves = []
            return board.array
        elif self.important_moves==[]:
            random_number = randint(0, len(self.gefilterte_liste) - 1)
            print(f"mögliche Züge in Array-Index-Form in gefilterte_liste: {self.gefilterte_liste}")
            print("Bot setzt hier: ")
            board.set_field_value(self.gefilterte_liste[random_number][0], self.gefilterte_liste[random_number][1], self.number)
            print()
            self.possible_moves = []
            self.gefilterte_liste = []
            return board.array
        else:
            random_number = randint(0, len(self.important_moves) - 1)
            print(f"mögliche Züge in Array-Index-Form in important_moves: {self.important_moves}")
            print("Bot setzt hier: ")
            board.set_field_value(self.important_moves[random_number][0], self.important_moves[random_number][1], self.number)
            print()
            self.possible_moves = []
            self.gefilterte_liste = []
            self.important_moves = []
            return board.array
        

    def check_horizontally(self, board):                     
        for row_index in range(len(board.array)):       #für spätere Indexierung des Arrays für speichern des möglichen Zuges
            row = board.array[row_index]                #zur Verbesserung der übersichtlichkeit
            for element in range(len(row)):           #nur elemente in der Reihe
                if row[element] != 0 and '''row[element] != self.number''' and element < 3:   #Feld von Gegner belegt und nicht am Rand
                    if row[element] == row[element + 1] == row[element + 2]:
                        if element == 2 and row[element-1] == 0:
                            self.important_moves.append((row_index, element - 1))
                        elif element == 1 and row[element+3] == 0:
                            self.important_moves.append((row_index, element + 3))
                        elif element == 1 and row[element-1] == 0:
                            self.important_moves.append((row_index, element - 1))
                        elif element == 0 and row[element+3] == 0:
                            self.important_moves.append((row_index, element + 3)) 
                    elif row[element] == row[element + 1] and row[element + 2] == 0:     #2 Felder in Folge vom Gegner belegt und 3. Feld frei
                        self.possible_moves.append((row_index, element + 2))
                    elif row[element] == row[element + 1] and row[element - 1] == 0:    #2 Felder in Folge vom Gegner belegt und Feld davor frei
                        self.possible_moves.append((row_index, element - 1))
                    elif row[element] == row[element + 2] and row[element + 1] == 0:
                        self.possible_moves.append((row_index, element+1))
                    else:
                        pass
                elif row[element] != 0 and '''row[element] != self.number''' and element <= 4: #Feld von Gegner belegt und am Rand
                    if row[element] == row[element - 1] and row[element - 2] == 0: 
                            self.possible_moves.append((row_index, element - 2))
                    else:
                        pass
                else:
                    pass
                

    def check_vertically(self, board):       
        transposed_board = np.rot90(board.array)         #flippt das board um 90° -> die Spalten werden zu Zeilen              
        for row_index in range(len(transposed_board)):       #für spätere Indexierung des Arrays für speichern des möglichen Zuges
            row = transposed_board[row_index]                #zur Verbesserung der übersichtlichkeit
            for element in range(len(row)):              #nur elemente in der Reihe
                if row[element] != 0 and '''row[element] != self.number''' and element < 3:   #Feld von Gegner belegt und nicht am Rand
                    if row[element] == row[element + 1] == row[element + 2]:            # 3 Felder in Folge belegt
                        if element == 2 and row[element-1] == 0:
                            self.important_moves.append((element-1, 4-row_index))
                        elif element == 1 and row[element+3] == 0:
                            self.important_moves.append((element + 3, 4-row_index))
                        elif element == 1 and row[element-1] == 0:
                            self.important_moves.append((element - 1, 4-row_index))
                        elif row[element+3] == 0:
                            self.important_moves.append((element + 3, 4-row_index)) 
                    elif row[element] == row[element + 1] and row[element + 2] == 0:     #2 Felder in Folge vom Gegner belegt und 3. Feld frei
                        self.possible_moves.append((element + 2, 4-row_index))
                    elif row[element] == row[element + 1] and row[element - 1] == 0:    #2 Felder in Folge vom Gegner belegt und Feld davor frei
                        self.possible_moves.append((element - 1, 4-row_index))
                    elif row[element] == row[element + 2] and row[element + 1] == 0:
                        self.possible_moves.append((element+1, 4-row_index))
                    else:
                        pass
                elif row[element] != 0 and '''row[element] != self.number''' and element <= 4: #Feld von Gegner belegt und am Rand
                    if row[element] == row[element - 1] and row[element - 2] == 0: 
                        self.possible_moves.append((element - 2, 4-row_index))
                    else:
                        pass
                else:
                    pass
                
    def check_diagonally(self, board):
        diag_1_main = list(board.array.diagonal())                                                #gibt Diagonale von links oben nach rechts unten aus
        diag_2_above_main = list(board.array.diagonal(offset=1) )                                         #gibt Diagonale da drüber aus
        diag_3_under_main = list(board.array.diagonal(offset=-1))                                         #gibt Diagonale da drunter aus

        flipped_board = np.fliplr(board.array)                                                    #spiegelt das board vertikal

        diag_flipped_main = list(flipped_board.diagonal())                                              #gibt Diagonale von rechts oben nach links unten aus
        diag_flipped_above_main = list(flipped_board.diagonal(offset=1))                                 #gibt Diagonale da drüber aus
        diag_flipped_under_main = list(flipped_board.diagonal(offset=-1))                                #gibt Diagonale da drunter aus


        main_diagonals = [diag_1_main, diag_flipped_main]                                                           #liste mit allen Hauptdiagonalen
        side_diagonals = [diag_2_above_main, diag_3_under_main, diag_flipped_above_main, diag_flipped_under_main]  

        #Überprüfung der Hauptdiagonalen nach 2 Steinen in Folge:

        for element in range(len(main_diagonals[0])):        #damit nur die Indizes und nicht die tatsächlichen Werte durchgegangen werden
            if diag_1_main[element] != 0 and''' diag_1_main[element] != self.number''' and element < 3:
                if diag_1_main[element] == diag_1_main[element + 1] == diag_1_main[element + 2]:
                    if element == 2 and diag_1_main[element-1] == 0:
                        self.important_moves.append((element-1, element-1))
                    elif element == 1 and diag_1_main[element+3] == 0:
                        self.important_moves.append((element + 3, element + 3))
                    elif element == 1 and diag_1_main[element-1] == 0:
                        self.important_moves.append((element - 1, element - 1))
                    elif diag_1_main[element+3] == 0:
                        self.important_moves.append((element + 3, element + 3))
                elif diag_1_main[element] == diag_1_main[(element+1)] and diag_1_main[(element+2)] == 0:
                    self.possible_moves.append((element+2, element+2))
                elif diag_1_main[element] == diag_1_main[element + 1] and diag_1_main[element - 1] == 0: 
                    self.possible_moves.append((element-1, element-1))
                else:
                    pass
            elif diag_1_main[element] != 0 and '''diag_1_main[element] != self.number''' and element <= 4:
                if diag_1_main[element] == diag_1_main[element - 1] and diag_1_main[element - 2] == 0:
                    self.possible_moves.append((element-2, element-2))
                else:
                    pass
            else:
                pass

        for element in range(len(main_diagonals[1])):        #weil Board geflipt wurde muss anders gespeichert werden, deshalb 2. 
            if diag_flipped_main[element] != 0 and""" diag_flipped_main[element] != self.number""" and element < 3:
                if diag_1_main[element] == diag_1_main[element + 1] == diag_1_main[element + 2]:
                    if element == 2 and diag_1_main[element-1] == 0:
                        self.important_moves.append((element-1, 4-(element-1)))
                    elif element == 1 and diag_1_main[element+3] == 0:
                        self.important_moves.append((element + 3, (4-element+3)%4))
                    elif element == 1 and diag_1_main[element-1] == 0:
                        self.important_moves.append((element - 1, 4-(element-1)))
                    elif diag_1_main[element+3] == 0:
                        self.important_moves.append((element + 3, (4-element+3)%4))
                elif diag_flipped_main[element] == diag_flipped_main[(element+1)] and diag_flipped_main[(element+2)] == 0:
                    self.possible_moves.append((element+2, (4-element+2)%4))
                elif diag_flipped_main[element] == diag_flipped_main[element + 1] and diag_flipped_main[element - 1] == 0: 
                    self.possible_moves.append((element-1, 4-(element-1)))
                else:
                    pass
            elif diag_flipped_main[element] != 0 and ''' diag_flipped_main[element] != self.number''' and element <= 4:
                if diag_flipped_main[element] == diag_flipped_main[element - 1] and diag_flipped_main[element - 2] == 0:
                    self.possible_moves.append((element-2, ((4-element-2)%4)))
                else:
                    pass
            else:
                pass

        #Überprüfung der Nebendiagonalen nach 2 Steinen in Folge:    
        #für jede einzeln, wegen Unterschieden in Indexierung. Darum keine for-Schleife, die über Liste mit Nebendiagonalen iteriert   
        # fertig
        for element in range(len(diag_2_above_main)):
            if diag_2_above_main[element] != 0 and''' diag_2_above_main[element] != self.number''':
                if element < 2:
                    if diag_2_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element ==0 and diag_2_above_main[element+3] == 0:
                        self.important_moves.append((element+3, 1+element+3))
                    elif diag_2_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element==1 and diag_2_above_main[element-1] == 0:
                        self.important_moves.append((element-1, 1+element-1))

                    elif self.number not in diag_3_under_main:
                        if diag_2_above_main[element] == diag_2_above_main[element+1] and diag_2_above_main[element+2] == 0:
                            self.possible_moves.append((element+2, 1+element+2))
                elif element == 2: 
                    if self.number not in diag_3_under_main:
                        if diag_2_above_main[element] == diag_2_above_main[element+1] and diag_2_above_main[element-1] == 0:
                            self.possible_moves.append((element-1, (1+element-1)))
            else:
                pass
        #fertig
        for element in range(len(diag_3_under_main)):
            if diag_3_under_main[element] != 0 and'''diag_3_under_main[element] != self.number''':
                if element < 2:
                    if diag_3_under_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element ==0 and diag_3_under_main[element+3] == 0:
                        self.important_moves.append((1+element+3, element+3))
                    elif diag_3_under_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element==1 and diag_3_under_main[element-1] == 0:
                        self.important_moves.append((1+element-1, element-1))
                    elif self.number not in diag_3_under_main:
                        if diag_3_under_main[element] == diag_3_under_main[element+1] and diag_3_under_main[element+2] == 0:
                            self.possible_moves.append((1+element+2, element+2))
                elif element == 2: 
                    if self.number not in diag_3_under_main:
                        if diag_3_under_main[element] == diag_3_under_main[element+1] and diag_3_under_main[element-1] == 0:
                            self.possible_moves.append((1+element-1, element-1))
                    
            else:
                pass
        
        for element in range(len(diag_flipped_above_main)):
            if diag_flipped_above_main[element] != 0 and'''diag_flipped_above_main[element] != self.number''':
                if element < 2:
                    if diag_flipped_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element ==0 and diag_3_under_main[element+3] == 0:
                        self.important_moves.append((element+3, 3 - (element+3)))
                    elif diag_flipped_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element==1 and diag_3_under_main[element-1] == 0:
                        self.important_moves.append((element-1, 1))                                                                                                                    # NICHT SICHER, OB 1 RICHTIG IST
                    elif self.number not in diag_flipped_above_main:
                        if diag_flipped_above_main[element] == diag_flipped_above_main[element+1] and diag_flipped_above_main[element+2] == 0:
                            self.possible_moves.append((element+2, 3 - (element+2)))
                elif element == 2: 
                    if self.number not in diag_flipped_above_main:
                        if diag_flipped_above_main[element] == diag_flipped_above_main[element+1] and diag_flipped_above_main[element-1] == 0:
                            self.possible_moves.append((element-1, 2))
            else:
                pass
        
        #indexierung fehlt
        for element in range(len(diag_flipped_under_main)):
            if diag_flipped_under_main[element] != 0 and ''' diag_flipped_under_main[element] != self.number''':
                if element < 2:
                    if diag_flipped_under_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element ==0 and diag_3_under_main[element+3] == 0:
                        self.important_moves.append((1+element+3, 4 - (element+3)))
                    elif diag_flipped_under_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element==1 and diag_3_under_main[element-1] == 0:
                        self.important_moves.append((1, 4))  
                    elif self.number not in diag_flipped_under_main:
                        if diag_flipped_under_main[element] == diag_flipped_under_main[element+1] and diag_flipped_under_main[element+2] == 0:
                            self.possible_moves.append((1+element+2, 4-(element+2)))
                elif element == 2:
                    if self.number not in diag_flipped_under_main: 
                        if diag_flipped_under_main[element] == diag_flipped_under_main[element+1] and diag_flipped_under_main[element-1] == 0:
                            self.possible_moves.append((2,3))
            else:
                pass
        
