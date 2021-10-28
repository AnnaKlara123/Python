# Dreieck berrechnen

# moduls

# Funktionen
import math

def dist(x1, x2, y1, y2): # Funktion erwartet 4 Argumente
    dx = x2 - x1
    dy = y2 -y1
    d = math.sqrt(dx**2 + dy**2)
    return d

# Main
i = list(map(int, input("Numbers: ").split())) 
print(i) 

x1 = i[0]
x2 = i[1]
y1 = i[2]
y2 = i[3]

print (x1)
print (x2)
print (y1)
print (y2)


# x1 = 1
# x2 = 2
# y1 = 3
# y2 = 4

var2 = dist(x1,x2, y1, y2)
print(var2)

# Call function
 # Direkte Berechnung mit vorgegebennen Zahlen 
    # var1 = dist(1,2,3,4) # hier werden Argumente direkt der Funktion übergeben / Hier wird Funktuon aufgerufen
    # print(var1)

