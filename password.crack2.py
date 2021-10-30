# alternative 2 zum Password crack

# Passwort nach Python cracken
 # zuerst alle möglichen Buchstarben/Zahlen/Zeichen angeben
 # dann Passwort als Imput (soll aus 4 zeichen bestehen)

possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?_" # das sind die möglichen Eingegebenen Zeichen
password = input("Gib ein Passwort (4 Zeichen)an: ") # das ist das selbst bestimmte Passwort 

for letter1 in possible:    # hier teste ich das erste eingegebene Zeichen´
    if letter1 == password[0]:
        print(letter1)
        break
    for letter2 in possible:  
        if letter2 == password[:1]:
            print(letter1)
            break
        for letter2 in possible:  
        if letter2 == password[:1]:
            print(letter1)
            break


    # if a == password[0]:
    #     break
    #     print(i)
    # for i in possible:
    #     if i== password[1]:
    #         print(i)
    #         break
    #     if i== password[1]:
    #         break
    #     for i in possible:
    #         if i == password[2]:
    #             print(i)
    #             break
    #         if i == password[2]:
    #             break
            # for letter4 in possible: # Buchstaben auf richtigkeit kontrollieren 
            #     if letter4== password[3]:
            #         print(letter4)
            #         break
            #     if letter4 == password[3]:
            #         break

print("done")

# möglich Anzahl an Kombinationen: 
laenge = len(possible)
anzahl = laenge**4
print(anzahl)