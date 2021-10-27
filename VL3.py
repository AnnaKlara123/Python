#myfunction 

# MODULES --> Struktur angewöhnen

# FUNCTIONS
def fakultaet(zahl): # hier die Variable "Zahl" durch in die Klammern schreiben defiieren
    ergebnis = 1
    
    for i in range(2, zahl+1): # i muss man in dem Fall nicht definieren, da es jeweils i-te Stelle darstellt
        ergebnis = ergebnis * i
    # print("Ergebins: ", ergebnis)
    # bis hierher bekomme ich nur ein Ergebnis. WEnn ich mit dem Ergebnis weiterrechnen will brauche ich eine weitere Funktion:
    return ergebnis

# MAIN
while True:
    zahl = int(input("Eingabe: "))
    # fakultaet(zahl) # DAS ist der AUFRUF bzw. DURCHFÜHRUNG der Funktion!!! 
    var = fakultaet(zahl) # gibt dem Ergebnis der Funktion eine Variable. Mit dieser kann dann im "Hauptprogramm" weitergerechnet werden
    print(var)

print("done")