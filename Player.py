from Board import Board
class Player():
    def __init__(self, name, number):
        self.name = name            #speichert Name des Spielers
        self.number = number        #1 oder 2, wird bei make_move() als Setzstein übergeben, Spieler markiert mit seiner Nummer auf dem Feld

        
    def make_move(self, board):
        coordinates_input = (input(f"{self.name}, gib deine Koordinaten ein (Form: x,y): "))
        coordinates_list = coordinates_input.split(",")                      #1. Wert = gewünschtes x, 2. Wert = gewünschtes y

        x_coordinate = (int(coordinates_list[0]) - 1)                        #Eingabe Indexierung anders als Rechner -> erstes Feld unten links für User Feld (1,1) statt (0,0)
        y_coordinate = 5 - int(coordinates_list[1])                          #auch wegen anderer Indexierung des Users. Damit unterste Reihe im Array für Usereingabe die erste Reihe ist
           

        if x_coordinate >= 5 or y_coordinate >= 5:                           #wenn Koordinaten außerhalb des Spielfelds (rechts oder oben) liegen:
            print("Ungültige Eingabe! *Keine Werte größer 5*")                                       #signalisiert eine ungültige Eingabe
            return self.make_move(board=board)                               #ruft Funktion nochmals auf, um erneute Eingabe zu ermöglichen. Return hat David hingepackt um alte Funktion zu schließen
            
        elif x_coordinate < 0 or y_coordinate < 0:                           #wenn Koordinaten unter oder links vom Feld liegen
            print("Ungültige Eingabe! *Keine Werte kleiner Null*")                                       #signalisiert eine ungültige Eingabe
            return self.make_move(board=board)                               #ruft Funktion nochmals auf, um erneute Eingabe zu ermöglichen. Return hat David hingepackt um alte Funktion zu schließen
            
        elif board.return_field_value(y_coordinate, x_coordinate) != 0:      #wenn ausgewähltes Feld schon belegt:
            print("Feld ist bereits belegt. Lege woanders")                  #kommuniziert dem User, dass das Feld bereits belegt ist 
            return self.make_move(board=board)                               #ruft Funktion nochmals auf, um erneute Eingabe zu ermöglichen. Return hat David hingepackt um alte Funktion zu schließen
                                     
        else:                                                                #wenn Feld frei ist:
            print()
            return board.set_field_value(y_coordinate, x_coordinate, self.number)   #definiert in Board Klasse, lässt Spieler an gewünschter Stelle mit seinem Zeichen (Zahl) setzen
        
        #return board.array                                                   #gibt Spielfeld zurück, damit es in Game Klasse verwendet werden kann
