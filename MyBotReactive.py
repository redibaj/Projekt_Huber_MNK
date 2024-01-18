from Player import Player
from Board import Board
import numpy as np
from random import randint


class MyBotReactive(Player):                                            
    def __init__(self, number):  
        '''Konstruktur des High-Level-Bots
        
        Eigenschaften umfassen Spielernummer sowie Listen für mögliche Züge, wichtige Züge und gewinnbringende Züge
        '''                                       
        self.number = number                                                
        self.possible_moves = []
        self.gefilterte_liste = []
        self.important_moves = []
        self.winning_moves = []
        self.moves_to_get_2_in_a_row = []
                                                                    
    
    def make_random_move_or_get_two_in_row(self, board):  
        '''Methode, die einen zufälligen Zug macht, wenn es keine wichtigen oder gewinnbringenden Züge gibt.
        
        Überprüft, ob Bot eine Zweierkette bilden kann. 
        Falls ja, wird ein zufälliger Zug aus dieser Liste gemacht, 
        der möglichst nicht am Rand des Spielfelds liegt.
        Falls nicht, prüft er, ob das Feld in der Mitte frei ist. 
        Wenn ja, wird dort ein Stein gesetzt, wenn nicht wird eine Liste aller freien Felder erstellt.
        Bot versucht nach Möglichkeit, nicht am Rand zu setzen.
        '''
        if self.moves_to_get_2_in_a_row == []:  
            #wenn keine Zweierkette möglich:                                  
            if board.array[2][2] == 0:
                y_coordinate = 2
                x_coordinate = 2   
            else:                     
                all_possible_moves = list(np.argwhere(board.array == 0))         
                for tupel in all_possible_moves:  
                    if 0 not in tupel and 4 not in tupel:
                        y_coordinate = tupel[0]
                        x_coordinate = tupel[1]
                        break
                    else:
                        y_coordinate = tupel[0]
                        x_coordinate = tupel[1]
        else:
            #wenn Bildung einer Zweierkette möglich:
            random_number = randint(0, len(self.moves_to_get_2_in_a_row) - 1)
            y_coordinate = self.moves_to_get_2_in_a_row[random_number][0]
            x_coordinate = self.moves_to_get_2_in_a_row[random_number][1]
                                                                                             
        print(f"Bot setzt random hier: {x_coordinate + 1, 5 - y_coordinate}")
        board.set_field_value(y_coordinate, x_coordinate, self.number)                       
        return board.array                                                                          
    
    def make_move(self, board):
        '''Methode, die den Bot einen Zug machen lässt.

        Prüft zunächst in der Horizontalen, Vertikalen und Diagonalen nach sinnvollen Zügen, wo 
        sie nach Priorität in verschiednene Listen sortiert werden. 
        Anschließend wird einer der am höchsten priorisierten Züge gespielt.
        Wenn keine wichtigen Züge möglich sind, wird ein überlegt-zufälliger Zug gespielt.
        Nach jedem Zug werden Listen geleert, damit keine veralteten Züge gespielt werden.
        '''
        self.check_horizontally(board)
        self.check_vertically(board)
        self.check_diagonally(board)
        self.gefilterte_liste = [tupel for tupel in self.possible_moves if 0 not in tupel and 4 not in tupel]
        if self.possible_moves == [] and self.important_moves == [] and self.winning_moves == []:
            #wenn keine strategisch sinnvollen Züge möglich sind:
            self.make_random_move_or_get_two_in_row(board)
            self.possible_moves = []
            self.gefilterte_liste = []
            self.important_moves = []
            return board.array
        elif self.gefilterte_liste == [] and self.important_moves == [] and self.winning_moves == []: 
            #wenn lediglich strategische unwichtigere Züge möglich sind:
            random_number = randint(0, len(self.possible_moves) - 1)
            print(f"mögliche Züge in Array-Index-Form in possible_moves: {self.possible_moves}")
            print(f"Bot setzt hier: ({self.possible_moves[random_number][0], self.possible_moves[random_number][1]})")
            board.set_field_value(self.possible_moves[random_number][0], self.possible_moves[random_number][1], self.number)
            print()
            self.possible_moves = []
            self.gefilterte_liste = []
            self.important_moves = []
            self.winning_moves = []
            return board.array
        elif self.important_moves == [] and self.winning_moves == []:
            #wenn strategisch sinnvollere, aber keine wichtigen Züge möglich sind:
            random_number = randint(0, len(self.gefilterte_liste) - 1)
            print(f"mögliche Züge in Array-Index-Form in gefilterte_liste: {self.gefilterte_liste}")
            print(f"Bot setzt hier: ({self.gefilterte_liste[random_number][0], self.gefilterte_liste[random_number][1]})")
            board.set_field_value(self.gefilterte_liste[random_number][0], self.gefilterte_liste[random_number][1], self.number)
            print()
            self.possible_moves = []
            self.gefilterte_liste = []
            self.important_moves = []
            self.winning_moves = []
            return board.array
        elif self.winning_moves == []:
            #wenn wichtige Züge möglich sind:
            random_number = randint(0, len(self.important_moves) - 1)
            print(f"mögliche Züge in Array-Index-Form in important_moves: {self.important_moves}")
            print(f"Bot setzt hier: ({self.important_moves[random_number][0], self.important_moves[random_number][1]})")
            board.set_field_value(self.important_moves[random_number][0], self.important_moves[random_number][1], self.number)
            print()
            self.possible_moves = []
            self.gefilterte_liste = []
            self.important_moves = []
            self.winning_moves = []
            return board.array
        else:
            #wenn gewinnbringende/verhindernde Züge möglich/nötig sind:
            random_number = randint(0, len(self.winning_moves) - 1)
            print(f"mögliche Züge in Array-Index-Form in important_moves: {self.winning_moves}")
            print(f"Bot setzt hier: ({self.winning_moves[random_number][0], self.winning_moves[random_number][1]})")
            board.set_field_value(self.winning_moves[random_number][0], self.winning_moves[random_number][1], self.number)  
            print()
            self.possible_moves = []
            self.gefilterte_liste = []
            self.important_moves = []
            self.winning_moves = []
            return board.array
        
    def check_for_empty_fields_around_own_number(self, board):
        '''Methode, die prüft, ob Felder um die eigene Zahl herum leer sind.
        
        Zunächst werden alle Felder mit der eigenen Zahl in einer Liste gespeichert.
        Anschließend wird für jedes Feld in der Liste überprüft, ob Felder um die eigene Zahl herum leer sind.
        Alle leeren Felder werden dann in einer Liste gespeichert.
        '''
        own_number_counter = []
        self.moves_to_get_2_in_a_row = []

        #Alle Felder mit eigener Zahl in Liste speichern
        for row_index in range(len(board.array)):       
            row = board.array[row_index]                
            for element in range(len(row)):
                if row[element] == self.number:
                    own_number_counter.append((row_index, element))
       
        #Indizes aus Positions-Tupel in Variablen speichern
        for position in own_number_counter:
            row_index, col_index = position
        
        #Checken, ob Felder um die eigene Zahl herum leer sind
        for i in range(row_index - 1, row_index + 2):
            for j in range(col_index - 1, col_index + 2):
                # Überprüfe, ob die Position im Array liegt
                if 0 <= i < 5 and 0 <= j < 5:
                    # Überprüfe, ob der Wert der umliegenden Position 0 ist
                    if board.array[i, j] == 0:
                        self.moves_to_get_2_in_a_row.append((i, j))
            

    def check_horizontally(self, board):
        '''Methode, die in Horizontalen nach sinnvollen Zügen sucht.
        
        Prüft auf verschiedene Situationen in den Reihen des Spielfelds:
        -Dreierkette mit leerem Feld links oder rechts (gewinnbringend)
        -potentielle Dreierkette mit leerem Feld in der Mitte des Spielbretts (gewinnbringend)
        -Zweierkette mit leerem Feld links oder rechts
        '''                     
        for row_index in range(len(board.array)):       
            row = board.array[row_index]                
            for element in range(len(row)):             
                #Wenn eigene Dreierkette und links oder rechts leer:
                if element == 0 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element+3] == 0:
                        self.winning_moves.append((row_index, element+3, "h"))

                if element == 2 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element-1] == 0:
                        self.winning_moves.append((row_index, element-1, "h"))

                #Wenn in Mitte der Reihe leeres Feld, links und rechts von der selben Zahl belegt und Felder am Rand leer:
                if row[2] == 0 and row[1] == row [3] and row[1] != 0 and row[0] == row[4] == 0:
                    self.important_moves.append((row_index, 2, "h"))

                #Wenn Feld belegt (links bis mitte):
                if row[element] != 0 and element < 3:
                    #wenn Dreierkette (spielerunabhängig):   
                    if row[element] == row[element + 1] == row[element + 2]:
                        if element == 2 and row[element-1] == 0:
                            self.important_moves.append((row_index, element - 1,"h"))
                        elif element == 1 and row[element+3] == 0:
                            self.important_moves.append((row_index, element + 3,"h"))
                        elif element == 1 and row[element-1] == 0:
                            self.important_moves.append((row_index, element - 1,"h"))
                        elif element == 0 and row[element+3] == 0:
                            self.important_moves.append((row_index, element + 3,"h")) 

                    #andernfalls: Prüfen auf Zweierketten und Lücken die zu Dreierkette führen: 
                    elif row[element] == row[element + 1] and row[element + 2] == 0:     
                        self.possible_moves.append((row_index, element + 2,"h"))
                    elif row[element] == row[element + 1] and row[element - 1] == 0 and element > 0:    
                        self.possible_moves.append((row_index, element - 1,"h"))
                    elif row[element] == row[element + 2] and row[element + 1] == 0:  
                        self.possible_moves.append((row_index, element+1,"h"))
                    else:
                        pass
                
                #wenn Feld belegt (rechts):
                elif row[element] != 0 and element <= 4: 
                    if row[element] == row[element-1] and row[element-2] == 0: 
                            self.possible_moves.append((row_index, element-2,"h"))
                    else:
                        pass
                else:
                    pass
                

    def check_vertically(self, board):     
        '''Methode, die in Vertikalen nach sinnvollen Zügen sucht.

        Dreht das Spielfeld um 90° und überprüft es die dadurch entstandenen Reihen.
        Entspricht bis auf Indexierung der Methode check_horizontally.
        '''  
        transposed_board = np.rot90(board.array)                    
        for row_index in range(len(transposed_board)):       
            row = transposed_board[row_index]                
            for element in range(len(row)):              
                if element == 0 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element+3] == 0:
                        self.winning_moves.append((element+3, 4-row_index, "v"))

                if element == 2 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element-1] == 0:
                        self.winning_moves.append((element-1, 4-row_index, "v"))
                
                if row[2] == 0 and row[1] == row[3] and row[1] != 0 and row[0] == row[4] == 0:
                    self.important_moves.append((2, 4-row_index, "v"))

                if row[element] != 0 and element < 3:   
                    if row[element] == row[element + 1] == row[element + 2]:            
                        if element == 2 and row[element-1] == 0:
                            self.important_moves.append((element-1, 4-row_index,"v"))
                        elif element == 1 and row[element+3] == 0:
                            self.important_moves.append((element + 3, 4-row_index,"v"))
                        elif element == 1 and row[element-1] == 0:
                            self.important_moves.append((element - 1, 4-row_index,"v"))

                    elif row[element] == row[element + 1] and row[element + 2] == 0:     
                        self.possible_moves.append((element + 2, 4-row_index,"v"))
                    elif row[element] == row[element + 1] and row[element - 1] == 0 and element > 0:    
                        self.possible_moves.append((element - 1, 4-row_index,"v"))
                    elif row[element] == row[element + 2] and row[element + 1] == 0:
                        self.possible_moves.append((element+1, 4-row_index,"v"))
                    else:
                        pass

                elif row[element] != 0 and element <= 4:
                    if row[element] == row[element - 1] and row[element - 2] == 0: 
                        self.possible_moves.append((element - 2, 4-row_index,"v"))
                    else:
                        pass
                else:
                    pass
                
    def check_diagonally(self, board):
        '''Methode, die in den Diagonalen nach sinnvollen Zügen sucht.
        
        Prüft auf verschiedene Situationen in den 6 möglichen Gewinn-Diagonalen des Spielfelds:
        -Dreierkette mit leerem Feld links oder rechts (gewinnbringend)
        -potentielle Dreierkette mit leerem Feld in der Mitte des Spielbretts (gewinnbringend)
        -Zweierkette mit leerem Feld links oder rechts
        '''
        diag_1_main = list(board.array.diagonal())                                               
        diag_2_above_main = list(board.array.diagonal(offset=1) )                                         
        diag_3_under_main = list(board.array.diagonal(offset=-1))                                         

        flipped_board = np.fliplr(board.array)                                                    

        diag_flipped_main = list(flipped_board.diagonal())                                              
        diag_flipped_above_main = list(flipped_board.diagonal(offset=1))                                 
        diag_flipped_under_main = list(flipped_board.diagonal(offset=-1))                                

        main_diagonals = [diag_1_main, diag_flipped_main]                                                           
        side_diagonals = [diag_2_above_main, diag_3_under_main, diag_flipped_above_main, diag_flipped_under_main]  

        #Überprüfung der Hauptdiagonalen auf...
        for element in range(len(main_diagonals[0])): 
            #...eigene Dreierketten     
            if element == 0 or element == 1:
                if diag_1_main[element] == diag_1_main[element+1] == diag_1_main[element+2] == self.number and diag_1_main[element+3] == 0:
                    self.winning_moves.append((element+3, element+3, "md"))
            if element == 2 or element == 1:
                if diag_1_main[element] == diag_1_main[element+1] == diag_1_main[element+2] == self.number and diag_1_main[element-1] == 0:
                    self.winning_moves.append((element-1, element-1, "md"))
            
            #...potentielle Dreierketten die Sieg bringen
            if diag_1_main[2] == 0 == diag_1_main[0] == diag_1_main[4] and diag_1_main[1] == diag_1_main[3] and diag_1_main[2] != 0:
                self.important_moves.append((2,2, "md"))

            if diag_1_main[element] != 0 and element < 3:
                if diag_1_main[element] == diag_1_main[element + 1] == diag_1_main[element + 2]:
                    #...generelle Dreierketten (spielerunabhängig) mit link/rechts leer
                    if element == 2 and diag_1_main[element-1] == 0:
                        self.important_moves.append((element-1, element-1,"md"))
                    elif element == 1 and diag_1_main[element+3] == 0:
                        self.important_moves.append((element + 3, element + 3,"md"))
                    elif element == 1 and diag_1_main[element-1] == 0:
                        self.important_moves.append((element - 1, element - 1,"md"))
                    elif element == 0 or element == 1:
                        if diag_1_main[element+3] == 0:
                            self.important_moves.append((element + 3, element + 3,"md"))
                
                #...Zweierketten mit links/rechts leer
                elif diag_1_main[element] == diag_1_main[(element+1)] and diag_1_main[(element+2)] == 0:
                    self.possible_moves.append((element+2, element+2,"md"))
                elif diag_1_main[element] == diag_1_main[element + 1] and diag_1_main[element - 1] == 0 and element > 0: 
                    self.possible_moves.append((element-1, element-1,"md"))
                
                #...Mitte leer, links/rechts von selbem Spieler belegt
                elif diag_1_main[element] == diag_1_main[element + 2] and diag_1_main[element+1] == 0:
                    self.possible_moves.append((element+1, element+1,"md"))
                else:
                    pass

            elif diag_1_main[element] != 0 and element <= 4:
                #...Zweierketten mit links leer
                if diag_1_main[element] == diag_1_main[element - 1] and diag_1_main[element - 2] == 0:
                    self.possible_moves.append((element-2, element-2,"md"))
                else:
                    pass
            else:
                pass

        for element in range(len(main_diagonals[1])):        

            if element == 0 or element == 1:
                #...eigene Dreierketten
                if diag_flipped_main[element] == diag_flipped_under_main[element+1] == diag_flipped_main[element+2] == self.number and diag_flipped_main[element+3] == 0:
                    self.winning_moves.append((element+3, 4-(element+3), "fmd"))

            if element == 2 or element == 1:
                if diag_flipped_main[element] == diag_flipped_under_main[element+1] == diag_flipped_main[element+2] == self.number and diag_flipped_main[element-1] == 0:
                    self.winning_moves.append((element-1, 4-(element-1), "fmd"))
            
            #...potentielle Dreierketten die Sieg bringen
            if diag_flipped_main[2] == 0 == diag_flipped_main[0] == diag_flipped_main[4] and diag_flipped_main[1] == diag_flipped_main[3] and diag_flipped_main[2] != 0:
                self.important_moves.append((2,2))

            if diag_flipped_main[element] != 0 and element < 3:
                if diag_flipped_main[element] == diag_flipped_main[element + 1] == diag_flipped_main[element + 2]:
                    #...generelle Dreierketten (spielerunabhängig) mit link/rechts leer
                    if element == 2 and diag_flipped_main[element-1] == 0:
                        self.important_moves.append((element-1, 4-(element-1),"fmd"))
                    elif element == 1 and diag_flipped_main[element+3] == 0:
                        self.important_moves.append((element+3, 4-(element+3), "fmd"))
                    elif element == 1 and diag_flipped_main[element-1] == 0:
                        self.important_moves.append((element-1, 4-(element-1), "fmd"))
                    elif element == 0 or element == 1:
                        if diag_flipped_main[element+3] == 0:
                            self.important_moves.append((element+3, 4-(element+3), "fmd"))
                
                #...Zweierketten mit links/rechts leer
                elif diag_flipped_main[element] == diag_flipped_main[(element+1)] and diag_flipped_main[(element+2)] == 0:
                    self.possible_moves.append((element+2, 4-(element+2), "fmd"))
                elif diag_flipped_main[element] == diag_flipped_main[element + 1] and diag_flipped_main[element - 1] == 0 and element > 0: 
                    self.possible_moves.append((element-1, 4-(element-1), "fmd"))

                #...Mitte leer, links/rechts von selbem Spieler belegt
                elif diag_flipped_main[element] == diag_flipped_main[element+2] and diag_flipped_main[element+1] == 0:
                    self.possible_moves.append((element+1, 4-(element+1), "fmd"))
                else:
                    pass

            #...Zweierketten mit links leer
            elif diag_flipped_main[element] != 0 and element <= 4:
                if diag_flipped_main[element] == diag_flipped_main[element - 1] and diag_flipped_main[element - 2] == 0:
                    self.possible_moves.append((element-2, 4-(element-2), "fmd"))
                else:
                    pass
            else:
                pass

        
        #Überprüfung der Nebendiagonalen auf...
        for element in range(len(side_diagonals[0])):
            #...eigene Dreierketten
            if element == 0:
                if diag_2_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] == self.number and diag_2_above_main[element+3] == 0:
                    self.winning_moves.append((element+3, 1+element+3, "amd"))
            elif element == 1:
                if diag_2_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] == self.number and diag_2_above_main[element-1] == 0:
                    self.winning_moves.append((element-1, 1+(element-1), "amd"))


            if diag_2_above_main[element] != 0:
                if element < 2:
                    #...generelle Dreierketten (spielerunabhängig) mit link/rechts leer
                    if diag_2_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element ==0 and diag_2_above_main[element+3] == 0:
                        self.important_moves.append((element+3, 1+element+3, "amd"))
                    elif diag_2_above_main[element] == diag_2_above_main[element+1] == diag_2_above_main[element+2] and element==1 and diag_2_above_main[element-1] == 0:
                        self.important_moves.append((element-1, 1+element-1, "amd"))

                    #Zweierkette des Gegners mit rechts leer
                    elif self.number not in diag_3_under_main:
                        if diag_2_above_main[element] == diag_2_above_main[element+1] and diag_2_above_main[element+2] == 0:
                            self.possible_moves.append((element+2, 1+element+2, "amd"))

                elif element == 2: 
                    #Zweierkette des Gegners mit links leer
                    if self.number not in diag_3_under_main:
                        if diag_2_above_main[element] == diag_2_above_main[element+1] and diag_2_above_main[element-1] == 0:
                            self.possible_moves.append((element-1, (1+element-1), "amd"))
            else:
                pass
        
        for element in range(len(side_diagonals[1])):
            if diag_3_under_main[element] != 0:
                #...eigene Dreierketten
                if element == 0:
                    if diag_3_under_main[element] == diag_3_under_main[element+1] == diag_3_under_main[element+2] == self.number and diag_3_under_main[element+3] == 0:
                        self.important_moves.append((1+element+3, element+3, "umd"))

                elif element == 1:
                    if diag_3_under_main[element] == diag_3_under_main[element+1] == diag_3_under_main[element+2] == self.number and diag_3_under_main[element-1] == 0:
                       self.important_moves.append((1+(element-1), element-1, "umd")) 

                if element < 2:
                    #...generelle Dreierketten (spielerunabhängig) mit link/rechts leer
                    if diag_3_under_main[element] == diag_3_under_main[element+1] == diag_3_under_main[element+2] and element ==0 and diag_3_under_main[element+3] == 0:
                        self.important_moves.append((1+element+3, element+3, "umd"))
                    elif diag_3_under_main[element] == diag_3_under_main[element+1] == diag_3_under_main[element+2] and element==1 and diag_3_under_main[element-1] == 0:
                        self.important_moves.append((1+element-1, element-1, "umd"))
                    
                    #Zweierkette des Gegners mit rechts leer
                    elif self.number not in diag_3_under_main:
                        if diag_3_under_main[element] == diag_3_under_main[element+1] and diag_3_under_main[element+2] == 0:
                            self.possible_moves.append((1+element+2, element+2, "umd"))
                elif element == 2: 
                    if self.number not in diag_3_under_main:
                        #Zweierkette des Gegners mit links leer
                        if diag_3_under_main[element] == diag_3_under_main[element+1] and diag_3_under_main[element-1] == 0:
                            self.possible_moves.append((1+element-1, element-1, "umd"))
                    
            else:
                pass
        
        for element in range(len(side_diagonals[2])):
            if diag_flipped_above_main[element] != 0:
                if element == 0:
                    #...eigene Dreierketten
                    if diag_flipped_above_main[element] == diag_flipped_above_main[element+1] == diag_flipped_above_main[element+2] == self.number and diag_flipped_above_main[element+3] == 0:
                        self.winning_moves.append((element+3, 3-(element+3), "afmd"))

                elif element == 1:
                    if diag_flipped_above_main[element] == diag_flipped_above_main[element+1] == diag_flipped_above_main[element+2] == self.number and diag_flipped_above_main[element-1] == 0:
                        self.winning_moves.append((element-1, 3-(element-1), "afmd"))

                if element < 2:
                    #...generelle Dreierketten (spielerunabhängig) mit link/rechts leer
                    if diag_flipped_above_main[element] == diag_flipped_above_main[element+1] == diag_flipped_above_main[element+2] and element ==0 and diag_flipped_above_main[element+3] == 0:
                        self.important_moves.append((element+3, 3 - (element+3),"afmd"))
                    elif diag_flipped_above_main[element] == diag_flipped_above_main[element+1] == diag_flipped_above_main[element+2] and element==1 and diag_flipped_above_main[element-1] == 0:
                        self.important_moves.append((element-1, 3 - (element-1),"afmd"))   

                    #Zweierkette des Gegners mit rechts leer                                                                                                                     
                    elif self.number not in diag_flipped_above_main:
                        if diag_flipped_above_main[element] == diag_flipped_above_main[element+1] and diag_flipped_above_main[element+2] == 0:
                            self.possible_moves.append((element+2, 3 - (element+2), "afmd"))

                elif element == 2: 
                    if self.number not in diag_flipped_above_main:
                        #Zweierkette des Gegners mit links leer
                        if diag_flipped_above_main[element] == diag_flipped_above_main[element+1] and diag_flipped_above_main[element-1] == 0:
                            self.possible_moves.append((element-1, 2, "afmd"))
            else:
                pass
        
        
        for element in range(len(side_diagonals[3])):
            if diag_flipped_under_main[element] != 0:
                if element == 0:
                    #...eigene Dreierketten
                    if diag_flipped_under_main[element] == diag_flipped_under_main[element+1] == diag_flipped_under_main[element+2] == self.number and diag_flipped_under_main[element+3] == 0:
                        self.winning_moves.append((1+element+3, 4 - (element+3),"ufmd"))

                elif element == 1:
                    if diag_flipped_under_main[element] == diag_flipped_under_main[element+1] == diag_flipped_under_main[element+2] == self.number and diag_flipped_under_main[element-1] == 0:
                        self.winning_moves.append((1+element-1, 4 - (element-1),"ufmd"))

                if element < 2:
                    #...generelle Dreierketten (spielerunabhängig) mit link/rechts leer
                    if diag_flipped_under_main[element] == diag_flipped_under_main[element+1] == diag_flipped_under_main[element+2] and element ==0 and diag_flipped_under_main[element+3] == 0:
                        self.important_moves.append((1+element+3, 4 - (element+3),"ufmd"))
                    elif diag_flipped_under_main[element] == diag_flipped_under_main[element+1] == diag_flipped_under_main[element+2] and element==1 and diag_flipped_under_main[element-1] == 0:
                        self.important_moves.append((1, 4,"ufmd"))  
                    elif self.number not in diag_flipped_under_main:
                        #Zweierkette des Gegners mit rechts leer    
                        if diag_flipped_under_main[element] == diag_flipped_under_main[element+1] and diag_flipped_under_main[element+2] == 0:
                            self.possible_moves.append((1+element+2, 4-(element+2), "ufmd"))
                
                elif element == 2:   
                    if self.number not in diag_flipped_under_main: 
                        #Zweierkette des Gegners mit rechts leer 
                        if diag_flipped_under_main[element] == diag_flipped_under_main[element+1] and diag_flipped_under_main[element-1] == 0:
                            self.possible_moves.append((element,element+1,"ufmd"))
            else:
                pass
