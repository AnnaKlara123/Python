# Dreieck berrechnen

# moduls

# Funktionen
import math

def scope(a, b ,c ): # Funktion deniniert: sie erwartet 4 Argumente und inkludiert 3 Rechnungen 
    q = a + b + c 
    return q # q ist der Umfang!

# Main
i = list(map(int, input("Enter the three side lengths of the triangle. Be sure to separate the numbers with a space: ").split())) # Eingabe als Liste einlesen 
print(i) 

a = i[0]
b = i[1]
c = i[2]

# Call function
scope = scope(a, b, c)
print(scope)


