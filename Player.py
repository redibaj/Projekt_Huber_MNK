from Board import Board
class Player():
    def __init__(self, name, number):
        self.name = name
        self.number = number        #1 oder 2, wird bei make_move() als Setzstein übergeben, Spieler markiert mit seiner Nummer auf dem Feld

        
    def make_move(self, board):
        coordinates_input = (input(f"{self.name}, gib deine Koordinaten ein (Form: x,y): "))
        coordinates_list = coordinates_input.split(",")                      #1. Wert = gewünschtes x, 2. Wert = gewünschtes y

        x_coordinate = (int(coordinates_list[0]) - 1)                        #Wegen Indexierung bei np-Arrays (1. Wert quasi y, 2. Wert quasi x)
        y_coordinate = 5 - int(coordinates_list[1])                  
           
        if x_coordinate >= 5 or y_coordinate >= 5:                           #wenn Koordinaten außerhalb des Spielfelds liegen:
            print("Ungültige Eingabe")
            return self.make_move(board=board)
            
        elif x_coordinate < 0 or y_coordinate < 0:
            print("Ungültige Eingabe")
            return self.make_move(board=board)
            
        elif board.return_field_value(y_coordinate, x_coordinate) != 0:      #wenn Feld schon belegt:
            print("Feld ist bereits belegt. Lege woanders")
            return self.make_move(board=board)
            
        else:                                                                #wenn Feld frei:
            board.set_field_value(y_coordinate, x_coordinate, self.number)   #definiert in Board Klasse, lässt Spieler an gewünschter Stelle setzen
        
        return board.array                                                   #gibt Spielfeld zurück, damit es in Game Klasse verwendet werden kann
                                                                             # -> Runde wird nicht zuende gespielt, wenn erster Spieler gewonnen hat