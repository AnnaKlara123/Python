# Passwort nach Python cracken
 # zuerst alle möglichen Buchstarben/Zahlen/Zeichen angeben
 # dann Passwort als Imput (soll aus 4 zeichen bestehen)

from typing import Counter


possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?_"
password = input("Gib ein Passwort (4 Zeichen)an: ")

for letter1 in possible:    
    for letter2 in possible:
        for letter3 in possible:
            for letter4 in possible: # Buchstaben auf richtigkeit kontrollieren 
                password2 = letter1+letter2+letter3+letter4
                if password == password2: 
                    print("Das Passwort lautet: ", password2)
                    break # break aus der Schleife 
                if password == password2:   
                    break # break aus der Schleife 
            if password == password2:   
                    break # break aus der Schleife 
        if password == password2:   
                    break # break aus der Schleife 

print("done")

# Kombinationen: 
laenge = len(possible)
anzahl = laenge**4
print(anzahl)