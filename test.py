# Volumen eines Wuerfels
import math

# Funktion def. 
def kugel(r):
    pi = math.pi
    vk = (4/3)*pi*r**3
    return vk

def dif(vw,vk):
    differ = abs(vw-vk)
    return differ
#Main
r = int(input("Geben Sie den Radius an: "))

for i in range(1,11,1):
    if i == 1:
        print(i)
        volk = kugel(r)
        print(volk)
        print("Das Volumen der" , 1 ,"ten Kugel beträgt", volk)

    else:
        volk2=kugel(r+i)
        print(i)
        print("Das Volumen des" , i ,"ten Würfels beträgt", volk2)




print("done")

