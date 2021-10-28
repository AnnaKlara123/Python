# Dreieck berrechnen

# moduls

# Funktionen
import math

def area(h, k): # Funktion deniniert: sie erwartet 2 Argumente und inkludiert 1 Rechnung
     O = (k/2)*h
     return O # ist die Fläche 

# Main --> Parameter definieren durch input 

h = int(input("Geben  Sie die Höhe ein des Dreiecks:"))
k = int(input("Geben Sie Kantenlänge  der Grundseite ein:"))


# Call function
area = area(h, k)
print(area)


