# Multiplikationen mit import file

# # FUNCTION importieren 

import mytools
# Alternativ:  from mytools import *

# #MAIN Parameter der Funktion definieren 
a = 4
b = 2
c = 6
d = 6

# Funktion aufrufen (Funktionsname steht im externen file. Je nach import Art kann direkt daruf zugegriffen werden oder mit VerweisAufFile.Funktion) 
ergebnis = mytools.calcfacult(a,b,c,d)
# alternativ: ergebnis = calcfacult(a,b,c,d)

print(ergebnis)
print("done")
