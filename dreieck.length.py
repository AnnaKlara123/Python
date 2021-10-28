# Dreieck berrechnen

# moduls

# Funktionen
import math

def dist(x1, x2, y1, y2): # Funktion deniniert: sie erwartet 4 Argumente und inkludiert 3 Rechnungen 
    dx = x2 - x1
    dy = y2 -y1
    d = math.sqrt(dx**2 + dy**2)
    return d # d ist die Länge!

# Main
i = list(map(int, input("Numbers: ").split())) # Eingabe als Liste einlesen 
print(i) 

x1 = i[0]
x2 = i[1]
y1 = i[2]
y2 = i[3]

# print (x1)
# print (x2)
# print (y1)
# print (y2)

# Call function
var2 = dist(x1,x2, y1, y2)
print(var2)


 # Direkte Berechnung mit vorgegebennen Zahlen 
    # var1 = dist(1,2,3,4) # hier werden Argumente direkt der Funktion übergeben / Hier wird Funktuon aufgerufen
    # print(var1)

