# Input soll umgewandelt werden FOR Loop hierfür verwenden

#1 : Hier wird die Eingabe pro Buchstabe  nach Upper/Lower getestet und dann jeweills gegeneteilig zurückgegeben

eingabe = input("Enter something:")
for x in eingabe: # zählt jeden Buchstaben einzeln
    if x.isupper(): # checkt, ob Buchstabe GROSS oder klein ist
            print(x.lower()) # gibt Buchstabe jeweils gegenteilig zurück
    elif x.islower():
            print(x.upper())    

print("done")

