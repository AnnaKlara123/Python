# Multiplikationen mit import file

# # FUNCTION importieren 

import mytools
# Alternativ:  from mytools import *

# #MAIN Var. der Funktion definieren 
a = 4
b = 2
c = 6
d = 6

# Funktion aufrufen (Funktionsname steht im externen file. Da dieses importiert wird kann direkt daruf zugegriffen werden) 
ergebnis = mytools.calcfacult(a,b,c,d)

print(ergebnis)
print("done")
