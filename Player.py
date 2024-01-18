from Board import Board
class Player():
    def __init__(self, name, number):
        self.name = name            
        self.number = number        
        
    def make_move(self, board):
        '''Lässt Spieler einen Zug machen.
        
        Nimmt von User Indexierung des Feldes, auf welches er setzen möchte, entgegen.
        Überprüft, ob Eingabe gültig ist.
        Wenn ja, wird der Zug ausgeführt, andefalls muss erneute Eingabe erfolgen.
        Eingabe im Stil (Spalte, Zeile) -> (x,y)
        '''
        coordinates_input = input(f"{self.name}, gib deine Koordinaten ein (Form: x,y): ")
        coordinates_list = coordinates_input.split(",")                      

        #prüft Gültigkeit d. Eingabe
        if len(coordinates_input)<3:
            print(f"{self.name}, gib 2 Werte ein!")
            return self.make_move(board=board)
        elif len(coordinates_input)<3:
            print(f"{self.name}, gib 2 Werte zwischen 1 und 5 an!")
            return self.make_move(board=board)
        elif "," not in coordinates_input:
            print(f"{self.name}, gib 2 Werte ein!")
            return self.make_move(board=board)
        
        #Umwandlung in Array-Indexierung
        x_coordinate = (int(coordinates_list[0]) - 1)                        
        y_coordinate = 5 - int(coordinates_list[1])                          

        if x_coordinate >= 5 or y_coordinate >= 5:                          
            print("Ungültige Eingabe! *Keine Werte größer 5*")                                       
            return self.make_move(board=board)                               
        elif x_coordinate < 0 or y_coordinate < 0:                           
            print("Ungültige Eingabe! *Keine Werte kleiner Null*")                                      
            return self.make_move(board=board)                                  
        elif board.return_field_value(y_coordinate, x_coordinate) != 0:      
            print("Feld ist bereits belegt. Lege woanders")                   
            return self.make_move(board=board)                                                          
        else:                                                                
            print()
            return board.set_field_value(y_coordinate, x_coordinate, self.number)   
