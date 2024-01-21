import numpy as np
class Board():
    '''Erstellt ein Spielfeld mit den Dimensionen m x n und einer Gewinnbedingung von k in Folge'''
    def __init__(self, m=5, n=5, k=4):
        self.m = m
        self.n = n
        self.k = k
        self.array = np.zeros((self.m, self.n))
        self.winner = None
    

    def display(self): 
        '''Zeigt das Spielfeld an'''               
        print(self.array)
    
    def return_field_value(self, x, y):           
        '''Gibt den Wert eines Feldes zurück.
         
        Findet statt, um zu prüfen, ob an der Stelle 
        gelegt werden darf (Darf, wenn Wert = 0)
        '''
        return self.array[x][y]                   
    
    def set_field_value(self, x, y, value):
        '''Ermöglicht Änderung eines Werts/setzen einer Markierung auf dem Spielfeld'''
        self.array[int(x)][int(y)] = value

    def board_full(self):
        '''Prüft, ob das Spielfeld voll ist
        
        Überblickt alle Elemente des Spielfeldes und zählt, wie viele Felder 
        belegt sind. Wenn alle Felder belegt sind, ist das Spielfeld voll.
        Beginnt bei 25 und zählt für jedes Element, das nicht 0 ist, 1 runter.
        '''
        zero_counter = 25
        for row in self.array:
            for element in row:
                if element != 0:
                    zero_counter -= 1
        if zero_counter == 0:
            return True
        else: 
            return False

    def has_won(self):                            
        '''Prüft, ob ein Spieler gewonnen hat'''
        if self.has_won_horizontally() or self.has_won_vertically() or self.has_won_diagonally():
            return True                           
        else:
            return False                          

    def has_won_horizontally(self):
        '''Prüft alle Reihen auf horizontalen Sieg
        
        Indiziert durch die Reihen und schaut, ob 4 Elemente (ungleich 0) in Folge gleich sind.
        Falls ja, wird das Spielfeld angezeigt und Gewinner gespeichert.
        '''
        for row in self.array:                                                       
            for i in range(len(row) -3):         #um innerhalb Spielfeld zu bleiben                                  
                if row[i] != 0:                                                                                              
                    if (row[i] == row[i + 1] == row[i + 2] == row[i + 3]):          
                        return True                                                             
                    else:     
                        pass  
                                                               
                        
    def has_won_vertically(self):   
        '''Prüft alle Spalten auf vertikalen Sieg           

        Dreht das Board um 90° und prüft dann die Reihen auf horizontalen Sieg.
        Gleiche Methodik wie in has_won_horizontally()
        '''             
        transposed_board = np.transpose(self.array)                     #flippt das board um 90° -> die Spalten werden zu Zeilen                             
        for row in transposed_board:                                    #für jede Reihe in transposed_board     
            for i in range(len(row) - 3):                               #ab hier gleich
                if row[i] != 0:                                             #schaut, ob Element nicht 0 ist
                    if row[i] == row[i + 1] == row[i + 2] == row[i + 3]:    #schuat, ob 4 Elemente in Folge gleich sind
                        return True                                                                          
                    else:                                                   
                        pass                                      
                      
    
    def has_won_diagonally(self):
        '''Prüft auf Sieg in den Diagonalen (Haupt- und Nebendiagonalen)

        Definiert zunächst alle Haupt- und Nebendiagonalen.
        Prüft dann, ob in einer Diagonalen 4 Elemente gleich sind.
        Sind in einer Diagonalen 4 Elemente gleich, wird das Spielfeld angezeigt und Gewinner gespeichert.
        '''
        diag_1_main = list(self.array.diagonal())                                                
        diag_2_above_main = set(self.array.diagonal(offset=1) )                                         
        diag_3_under_main = set(self.array.diagonal(offset=-1))                                         

        flipped_board = np.fliplr(self.array)        #Board drehen, um andere Diagonalen zu bekommen

        diag_flipped_main = list(flipped_board.diagonal())                                              
        diag_flipped_above_main = set(flipped_board.diagonal(offset=1))                                 
        diag_flipped_under_main = set(flipped_board.diagonal(offset=-1))                                

        main_diagonals = [diag_1_main, diag_flipped_main]                                                       
        side_diagonals = [diag_2_above_main, diag_3_under_main, diag_flipped_above_main, diag_flipped_under_main]   


        for x in main_diagonals:
            #sind 4 Elemente gleich und nicht 0, dann ist Gewinner
            if x[0] == x[1] == x[2] == x[3] and x[0] != 0:                    
                return True                                   
                
            elif x[4] == x[3] == x[2] == x[1] and x[4] != 0:                            
                return True                                                         
            

        for element in side_diagonals:
            #erstellt Set aus allen Elementen der Nebendiagonalen
            #wenn Set nur ein Element und Element ungleich 0: Gewinner                                 
            if len(set(element)) == 1 and element != {0}:                    
                return True

        return False        #wenn kein Gewinner in Diagonalen
