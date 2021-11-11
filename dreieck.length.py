# Dreieck berrechnen

# moduls

# Funktionen
import math

def dist(x1, x2, y1, y2): # Funktion deniniert: sie erwartet 4 Argumente und inkludiert 3 Rechnungen 
    dx = x2 - x1
    dy = y2 -y1
    d = math.sqrt(dx**2 + dy**2)
    return d # d ist die Seitenlänge!

# Main
i = list(map(int, input("Please enter 4 numbers. The first one counts as x1, second as x2, thrird as y1, forth as y2.  Be sure to separate the numbers with a tab:  ").split())) # Eingabe als Liste einlesen 
print(i) # Eingabe der Parameter werden als Liste gespeichert

x1 = i[0] # Parameter werden aus der Liste abgerufen 
x2 = i[1]
y1 = i[2]
y2 = i[3]

# Call function
var2 = dist(x1,x2, y1, y2)
print("The calculated sidelength is:", var2)


 # Direkte Berechnung mit vorgegebennen Zahlen 
    # var1 = dist(1,2,3,4) # hier werden Argumente direkt der Funktion übergeben / Hier wird Funktuon aufgerufen
    # print(var1)

