# Volumen eines Wuerfels
import math

# Funktion def. 
def qurd(s):
    vw = s**3 # Volumen Würfel Formel
    return vw

def kugel(r):
    pi = math.pi
    vk = (4/3)*pi*r**3 # Volumen Kugel Formel
    return vk

def dif(vw,vk):
    differ = abs(vw-vk) # Differenz der Volumen berechnen
    return differ

#Main - Usereingabe
s=r = int(input("Geben Sie die Seitenlänge, bzw. den Radius an: "))

for i in range(1,11): #start=1, Ende bei 10, 1= Steps
    if i == 1: # Berechnung der 1.Runde, ohne "count"
        print(i,"te Iteration")
        vw = qurd(s) # Berechnung des WürfelVolumens durch Aufrufen der Funktion quad als erste Iteration und Speicherung des Werts als Variable
        print("Das Volumen des" , 1 ,"ten Würfels beträgt", vw, "m^3")
        vk = kugel(r) #s.o. nur für Kugel
        # print(volk)
        print("Das Volumen der" , 1 ,"ten Kugel beträgt", vk, "m^3")
        absolutdiff = dif(vw, vk) # Berechnung der Differenz der beiden Volumen 
        print("Die Differenz beträgt: ", absolutdiff)
        
    elif i<11 and i>1: # Berechnung des Volumens für die anderen 9 Iterationen
            print(i,"te Iteration")
            vw=qurd(s+i)        # +i um jeweils plus 1 zu rechnen 
            vk=kugel(r+i)
            # vw = vol2
            # vk = volk2
            absolutdiff = dif(vw, vk)
            print("Das Volumen des" , i ,"ten Würfels beträgt", vw, "m^3")
            print("Das Volumen des" , i ,"ten Würfels beträgt", vk, "m^3")
            print("Die Differenz beträgt: ", absolutdiff)
print("done")

