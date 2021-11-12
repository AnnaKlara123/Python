# Passworttest
password = "GeHeiM" 

# for Loop starten mit 3 Durchläufen (jeder falsche Versuch -1)
for x in range (3, 0, -1): # ":" bedeutet Start des Loops 

#Abfrage starten a = Feld für PW eingabe

    a = input("Enter password: ")
#Kontrolle ob PW stimmt
    if a == password:
        print("password correct. Welcome!")
        break # Loop beenden
    else: 
        print("Incorrect password")

# Abfrage der Versuchsanzahlen
    if x == 1: 
        print("access denied")
    elif x == 3:
        print("you have 2 more trials")
    elif x == 2:
        print("you have 1 more trials")
    else:
        print("password not accepted")


