from Player import Player
from Board import Board
import numpy as np
from random import randint


class MyBotRandom(Player):
    '''Bot, der nur random Züge spielen kann'''
    def __init__(self, number):
        self.number = number 
        self.name = "RandomBot"       

    def make_move(self, board = Board):  
        '''Ermöglicht dem Bot das Setzen seiner Markierung auf dem Spielfeld-Array.
        2 Pseudo-Zufallszahlen werden erstellt, die für die Indexierung eines Feldes
        verwendet werden. Ist Feld frei, setzt Bot an dieser Stelle. Andernfalls werden
        neue Zufallszahlen generiert, bis der Bot ein leeres Feld trifft
        '''                        
        x_coordinate = randint(0,4)                                         
        y_coordinate = randint(0,4)                                         
        while board.array[y_coordinate][x_coordinate] != 0:                 #wenn Feld belegt
            x_coordinate = randint(0,4)                                    
            y_coordinate = randint(0,4)                                     

        board.set_field_value(y_coordinate, x_coordinate, self.number)      #methode def. in Board-Klasse, markiert Spielzug auf dem Spielbrett
        return board.array                                                  



class MyBot2(Player):         
    '''Bot etwas besser als random'''    

    def __init__(self, number):
        self.number = number
        self.name = "MyBot2"
        self.winning_moves_bot2 = []

    def bot2_make_random_move(self, board):          
        '''Prüft auf sonnvolle, random Züge
        
        Bot prüft, ob zentrales Feld frei ist, aufgrund dessen strategischer Stärke.
        Sollte es belegt sein, werden alle freien Felder in einer Liste gespeichert.
        Bot prüft Liste auf Felder, die nicht am Spielfeldrand liegen.
        Wenn auch die alle belet: Bot setzt auf zufälliges freies Feld
        '''                         
        if board.array[2][2] == 0:
            y_coordinate = 2
            x_coordinate = 2   
        else:                     
            all_possible_moves = list(np.argwhere(board.array == 0))         #gibt eine Liste von Tupeln zurück, die alle freien Felder (0) besitzen
            for tupel in all_possible_moves:  
                if 0 not in tupel and 4 not in tupel:
                    y_coordinate = tupel[0]
                    x_coordinate = tupel[1]
                    break
                else:
                    y_coordinate = tupel[0]
                    x_coordinate = tupel[1]
                                                                                             #andere zufällige y-Koordinate wird generiert
        print(f"Bot setzt random hier: {x_coordinate + 1, 5 - y_coordinate}")
        board.set_field_value(y_coordinate, x_coordinate, self.number)                       #methode def. in Board-Klasse, markiert Spielzug auf dem Spielbrett
        return board.array         

    def make_move(self, board):
        '''Bot prüft horizontal und vertikal auf eigene Gewinnmöglichkeit und setzt entsprechend
        
        Bot prüft, ob er selbst gewinnen kann. Wenn ja, wird an einer zufällig gewählten Stelle gesetzt,
        an der er gewinnen kann. Wenn nicht, wird random gesetzt.
        '''
        self.check_horizontally(board)
        self.check_vertically(board)
        if self.winning_moves_bot2 == []:
            self.bot2_make_random_move(board)
            return board.array
        else:
            random_number = randint(0, len(self.winning_moves_bot2) - 1)
            print(f"mögliche Züge in Array-Index-Form in possible_moves: {self.winning_moves_bot2}")
            print(f"Bot setzt hier: ({self.winning_moves_bot2[random_number][0], self.winning_moves_bot2[random_number][1]})")
            board.set_field_value(self.winning_moves_bot2[random_number][0], self.winning_moves_bot2[random_number][1], self.number)
            self.winning_moves_bot2 = []
            return board.array

    def check_horizontally(self, board):     
        '''Überprüft, ob horizontal auf dem Spielfeld 3 eigene Steine in einer Reihe sind
        
        Verfahren: Spielfeld wird zeilenweise durchgegangen. Wenn 3 eigene Steine in einer Reihe sind,
        wird geprüft, ob das Feld rechts oder links von der Reihe frei ist. Wenn ja, wird dieses Feld
        in eine Liste gespeichert, die alle möglichen Gewinnzüge enthält.
        '''                
        for row_index in range(len(board.array)):       
            row = board.array[row_index]               
            for element in range(len(row)):             
                #2 Prüfungsmethoden, da sonst Indexfehler
                if element == 0 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element+3] == 0:
                        self.winning_moves_bot2.append((row_index, element+3))

                if element == 2 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element-1] == 0:
                        self.winning_moves_bot2.append((row_index, element-1))    


    def check_vertically(self, board):     
        '''Überprüft, ob vertikal auf dem Spielfeld 3 eigene Steine in einer Reihe sind
        
        Spielfeld wird um 90° gedreht, um die vertikalen Reihen zu überprüfen.
        Verfahren ansonsten identisch zu check_horizontally()
        '''  
        transposed_board = np.rot90(board.array)                     
        for row_index in range(len(transposed_board)):       
            row = transposed_board[row_index]                
            for element in range(len(row)):              
                if element == 0 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element+3] == 0:
                        self.winning_moves_bot2.append((element+3, 4-row_index))

                if element == 2 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element-1] == 0:
                        self.winning_moves_bot2.append((element-1, 4-row_index))                                                             
