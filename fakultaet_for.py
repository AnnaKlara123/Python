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
    
print("done")