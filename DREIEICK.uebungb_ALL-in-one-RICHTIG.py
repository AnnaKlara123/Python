# Dreieck berrechnen

# moduls

import math

# Funktionen definieren

def scope(a, b ,c ): # 
    q = a + b + c 
    return q # q ist der Umfang!
# Alternative Rechnenweise mit Höhe berrechnen:
# def hight(a,c):
#     h = (1/2)*math.sqrt(4*a**2-c**2)
#     return h

# def area(h, c): 
#         O = (c/2)*h
#         return O # ist die Fläche
def flaeche(a, b, c): # Funktion der Fläche
    s = (a+b+c)/2
    area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    round
    return area


# Main --> Parameter definieren durch input 
a = b = int(input("Geben  Sie die beiden gleichlangen Seitenlängen des Dreiecks ein: "))
c = int(input("Geben  Sie die dritte Seitenlänge ein: "))
iterat= int(input("Geben sie die Wiederholungen ein "))
weit = int(input("Geben Sie die Schrittweite an: "))

for i in range(0, iterat,1): # Schrittzahl eventuell später noch definieren
# Call function
    if i == 0:
        # h = hight(a,c)+weit
        # b = b 
        area1 = flaeche(a,b,c) # funktionsaufruf
        print(i+1, "-te Runde")
        print("Die gleichlangen Seiten betragen", a)
        print("Die dritte Seitenlänge bertägt",c )
        print("die Fläche beträgt: ", area1)
        scope1 = scope(a, b, c)
        print("Der Umfang beträgt: ", scope1)

    else:
        a = a+weit
        c = c+weit
        area2 = flaeche(a,b,c)
        scope2  = scope(a, b, c)
        
        print(i+1, "-te Runde")
        print("Die gleichlangen Seiten betragen", a)
        print("Die dritte Seitenlänge bertägt",c)
        print("die Fläche beträgt: ", area2)
        print("Der Umfang beträgt: ", scope2)
