# Input soll umgewandelt werden FOR Loop hierfür verwenden

#1 : Hier wird die Eingabe pro Buchstabe  nach Upper/Lower getestet und dann jeweills gegeneteilig zurückgegeben
eingabe = input("Enter something:")
for x in eingabe:
    if x >= 'A' and x <= 'Z':
            print(x.lower())
    elif x >= 'a' and x <= 'z':
            print(x.upper())

print("done")

# eingabe = input("Enter something:")
# for x in eingabe:
#     if x >= 'A' and x <= 'Z':
#             print(x.islower())
#     else:
#             print("TRUE")

# print("done")

# eingabe = input("Enter something:")
# for x in eingabe: # zählt jeden Buchstaben einzeln
#     if x.isupper(): # checkt, ob Buchstabe GROSS oder klein ist
#             print(x.lower()) # gibt Buchstabe jeweils gegenteilig zurück
#     elif x.islower():
#             print(x.upper())

# print("done")

