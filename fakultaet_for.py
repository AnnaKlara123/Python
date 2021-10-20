# Rahembedingungen überprüfen mit
while True: # ist eine Endlossschleife
    zahl = int(input("gebe Zahl ein: "))
    
    if zahl < 0:
        print("negativ Zahl nicht erlaubt")
        continue # While Schleife läuft weiter

    elif zahl == 0:
        print("Programm beenden.")
        break

    else: 
        print(zahl, "Die Eingabe ist korrekt")

    # Berechnung der Fakultät

    ergebnis = 1
    while zahl > 0:
        print(ergebnis,zahl)
        ergebnis = ergebnis *zahl
        zahl = zahl - 1
    print ("Ergebnis: ", ergebnis)
    
    
print("done")