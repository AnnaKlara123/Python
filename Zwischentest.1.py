# einen Satz als Imput wählen 
satz = input('Gib einen Sazt ein: ')

wordcount = len(satz.split())
print("Der Satz hat", wordcount, "Wörter")

upper = 0 # eine Count Variable anlegen, die sich erhöt, sobald ein Großbuchstabe erkannt wird
for i in satz:
    #zählt Großbuchstaben
    if(i.isupper()):
        upper = upper + 1
		

# Ausgabe der gezählten Buchstaben 
print('Der Satz hat',upper, 'Großbuchstaben')

#Alternativ:
# Satz eingeben 
satz = input("gib einen Satz ein: ")
# Großbuchstaben zählen
upper_count = sum(1 for i in satz if i.isupper())
# print 
print("der Sazt hat", upper_count, "Großbuchstaben")

#Alternative 2

wordcount = len(satz.split())
list = satz.split()
print(list)
count = 0
for i in list:
    if i[0].isupper():
        count = count + 1
		
print(count , "Großbuchstaben")

print("done")
