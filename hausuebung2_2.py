# Input soll umgewandelt werden FOR Loop hierfür verwenden

#1 : Hier wird die Eingabe pro Buchstabe  nach Upper/Lower getestet und dann jeweills gegeneteilig zurückgegeben
eingabe = input("Enter something:")
for x in eingabe:
    if x >= 'A' and x <= 'Z':
            print(eingabe.lower())
    elif x >= 'a' and x <= 'z':
            print(eingabe.upper())

print("done")
