# Volumen eines Wuerfels
import math

# Funktion def. 
def qurd(s):
    vw = s**3
    return vw

def kugel(r):
    pi = math.pi
    vk = (4/3)*pi*r**3
    return vk

def dif(vw,vk):
    differ = abs(vw-vk)
    return differ

#Main
s = int(input("Geben Sie die Seitenlänge an: "))
r = int(input("Geben Sie den Radius an: "))

for i in range(1,11,1):
    if i == 1:
        print(i)
        vol = qurd(s) # Berechnung des WürfelVolumens erste Iteration
        # print(vol)
        print("Das Volumen des" , 1 ,"ten Würfels beträgt", vol)
        volk = kugel(r) #Berechnung des Kugelvolumens erste Iteration
        # print(volk)
        print("Das Volumen der" , 1 ,"ten Kugel beträgt", volk)
        vw = vol
        vk = volk
        absolutdiff = dif(vw, vk) # Berechnung der Differenz der beiden Volumen 
        print("Die Differenz beträgt: ", absolutdiff)
        
    else:
        vol2=qurd(s+i)
        print(i)
        
        volk2=kugel(r+i)
        print(i)

        absolutdiff = dif(vw, vk)
    print("Das Volumen des" , i ,"ten Würfels beträgt", vol2)
    print("Das Volumen des" , i ,"ten Würfels beträgt", volk2)
    print("Die Differenz beträgt: ", absolutdiff)


print("done")

