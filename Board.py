import numpy as np
class Board():
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
        '''
        Gibt den Wert eines Feldes zurück.
         
        Findet statt, um zu prüfen, ob an der Stelle 
        gelegt werden darf (Darf, wenn Wert = 0)
        '''
        return self.array[x][y]                   
    
    def set_field_value(self, x, y, value):
        '''Ermöglicht Änderung eines Werts/setzen einer Markierung auf dem Spielfeld'''
        self.array[int(x)][int(y)] = value

    def board_full(self):
        '''
        Prüft, ob das Spielfeld voll ist
        
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
        '''
        Prüft alle Reihen auf horizontalen Sieg
        
        Indiziert durch die Reihen und schaut, ob 4 Elemente (ungleich 0) in Folge gleich sind.
        Falls ja, wird das Spielfeld angezeigt und Gewinner gespeichert.
        '''
        for row in self.array:                                                       
            for i in range(len(row) -3):         #um innerhalb Spielfeld zu bleiben                                  
                if row[i] != 0:                                                                                              
                    if (row[i] == row[i + 1] == row[i + 2] == row[i + 3]):          
                        print("Wir haben einen horizontalen Sieger!") 
                        print("Winning ELement: ", int(row[i]))
                        self.winner = int(row[i])
                        self.display()
                        return True                                                             
                    else:     
                        pass  
                                                               
                        
    def has_won_vertically(self):                           
        transposed_board = np.transpose(self.array)                     #flippt das board um 90° -> die Spalten werden zu Zeilen                             
        for row in transposed_board:                                    #für jede Reihe in transposed_board     
            for i in range(len(row) - 3):                               #ab hier gleich
                if row[i] != 0:                                             #schaut, ob Element nicht 0 ist
                    if row[i] == row[i + 1] == row[i + 2] == row[i + 3]:    #schuat, ob 4 Elemente in Folge gleich sind
                        print("Wir haben einen vertikalen Sieger!")
                        # if row[i] == 1:
                        #     print(f"Sieger: {Game.player1}")
                        # elif row[i] == 2:
                        #     print(f"Sieger: {Game.player2}")
                        print("Winning ELement: ", int(row[i]))
                        self.display() 
                        self.winner = int(row[i])
                        return True                                                                          
                    else:                                                   
                        pass                                      
                      
    
    def has_won_diagonally(self):
        diag_1_main = list(self.array.diagonal())                                                #gibt Diagonale von links oben nach rechts unten aus
        diag_2_above_main = set(self.array.diagonal(offset=1) )                                         #gibt Diagonale da drüber aus
        diag_3_under_main = set(self.array.diagonal(offset=-1))                                         #gibt Diagonale da drunter aus

        flipped_board = np.fliplr(self.array)                                                    #spiegelt das board vertikal

        diag_flipped_main = list(flipped_board.diagonal())                                              #gibt Diagonale von rechts oben nach links unten aus
        diag_flipped_above_main = set(flipped_board.diagonal(offset=1))                                 #gibt Diagonale da drüber aus
        diag_flipped_under_main = set(flipped_board.diagonal(offset=-1))                                #gibt Diagonale da drunter aus


        main_diagonals = [diag_1_main, diag_flipped_main]                                                           #liste mit allen Hauptdiagonalen
        side_diagonals = [diag_2_above_main, diag_3_under_main, diag_flipped_above_main, diag_flipped_under_main]   #liste mit allen Nebendigonalen (über/unter Hauptdiagonalen)

      
        #Überprüfung der Hauptdiagonalen nach Gewinner:
        #Idee: wenn ersten oder letzten 4 Elemente einer Hauptdiagonalen gleich sind, dann ist in dieser Diagonalen k=4
        
        #für Hauptdiagonalen:
        for x in main_diagonals:
            if x[0] == x[1] == x[2] == x[3] and x[0] != 0:                    #prüft ersten 4 Elemente beider Hauptdiagonalen und schaut, ob sie gleich sind
                print("Wir haben einen diagonalen Sieger!")
                # if x[0] == 1:
                #     print(f"Sieger: {Game.player1}")
                # elif x[0] == 2:
                #     print(f"Sieger: {Game.player2}")
                print("Winning ELement: ", int(x[0]))
                self.display()
                self.winner = int(x[0])
                return True                                   
                
            elif x[4] == x[3] == x[2] == x[1] and x[4] != 0:                  #prüft, ob die letzten 4 Elemente gleich sind und ob sie nicht 0 sind            
                print("Wir haben einen diagonalen Sieger!")
                # if x[4] == 1:
                #     print(f"Sieger: {Game.player1}")
                # elif x[4] == 2:
                #     print(f"Sieger: {Game.player2}")
                print("Winning ELement: ", int(x[4]))    
                self.display()
                self.winner = int(x[4])
                return True                                                         

        #für zweite Hauptdiagonale:
        
        #Überprüfung der Nebendiagonalen nach Gewinner:
        #Idee: Nebendiagonalen haben aufgrund der Anordnung des Spielfeldes immer 4 Elemente
        #wenn ein Set mit Werten einer unserer Nebendiagonalen nur einen Wert hat, dann ist in dieser Diagonalen k=4
        #      -> nur ein Wert: Gewinner, da er 4 in einer Reihe hat

        for element in side_diagonals:                                  #für jedes Element in der Liste der Nebendiagonalen 
            if len(set(element)) == 1 and element != {0}:                    #Gefahr: Menge mit Wert 0: es wurde kein Wert von Spieler eingegeben, trotzdem ist 4 mal 0 in einer Reihe
                print("Wir haben einen Nebendiagonalen Sieger!")
                # if element == {1}:
                #     print(f"Sieger: {Game.player1}")
                # elif element == {2}:
                #     print(f"Sieger: {Game.player2}")
                print("Winning Element: ", set(element))
                self.display()
                self.winner = set(element)
                return True

        return False               #erst hier, damit ganze Funktion durchlaufen wird und nicht bei erstem False abgebrochen wird      
