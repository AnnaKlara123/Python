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
    
    for i in range(2, zahl+1): # i muss man in deim Fall nicht definieren!
        ergebnis = ergebnis * i
    print("Ergebins: ", ergebnis)

    
print("done")