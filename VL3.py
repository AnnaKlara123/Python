#myfunction 

# MODULES --> Struktur angewöhnen

# FUNCTIONS
def fakultaet(zahl): # hier die Variable "Zahl" durch in die Klammern schreiben defiieren
    ergebnis = 1
    
    for i in range(2, zahl+1): # i muss man in dem Fall nicht definieren, da es jeweils i-te Stelle darstellt
        ergebnis = ergebnis * i
    print("Ergebins: ", ergebnis)
# MAIN
while True:
    zahl = int(input("Eingabe: "))
    fakultaet(zahl) # DAS ist der AUFRUF bzw. DURCHFÜHRUNG der Funktion!!! 

print("done")