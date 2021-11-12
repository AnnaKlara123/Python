import random
import time

timebefore = time.time()

# Erstellt Liste von zufälligen Zahlen von 0 bis 1000. Schleife wird 1000 mal durchgeführt.
# Zufallzahl von 0 bis 1000 wird erstellt. An die Liste zufall wird die immer wieder neue variable a drangehängt
zufall = []
for i in range (1000):
    a = (int(random.random()*1000))
    zufall.append(a)

mylist = []
mydict = {}
# Für jeden Eintrag in Liste "zufall" wird geprüft und einer von 2 Aufträgen ausgeführt. Dabei wird das dictionary (mydict) gefüllt.
# 1. Fall (if): wenn i schon im dict vorhanden ist, dann wird i gelöscht. Nicht nur der key i wird gelöscht, sonder auch der damit zusammenhängende Eintrag. Anschließend wird ein neuer Eintrag erstellt.
# i ist der key, die Anzahl an Einträgen im dict ist der Wert.
# 2. Fall bzw. alle anderen Fälle (else): es gibt noch keinen Eintrag mit key i und es wird ein neuer erstellt mit key i und als Wert die Zahl, die angibt wie häufig der key in der Liste vorkam.
for i in zufall:
    if i in mydict:
        del mydict[i]
        mydict[i] = zufall.count(i)
    else:
        mydict[i] = zufall.count(i)

# Inhalt des dictionary sortiert ausgeben
# for key in sorted(mydict.keys()):
#     print(key, mydict[key])
#alternativ:
# for key in sorted(mydict.keys()):
#     print("%s: %s" % (key, mydict[key]))


###dict ist nur cache (Zwischenspeicher), nun soll der Inhalt des dict wieder in einer Liste gespeichert und ausgegeben werden.
# mydict=sorted(mydict.keys())


# mylist wird zu einer Variablen, die eine Kopie des dict ist
mylist = mydict.items()
# mylist ist nun eine neue eigene Liste
mylist = list(mylist)
# mylist wird sortiert nach den Werten von Index 0 (also dem key)
mylist.sort(key = lambda x: x[0])
print(mylist)
# mylist.sort()
# print(mylist)



timeafter = time.time()
duration = timeafter - timebefore
print(duration)

print("done")

# Tipps von:
# https://www.delftstack.com/de/howto/python/python-convert-dictionary-to-list/
# https://www.delftstack.com/de/howto/python/python-sort-list-of-tuples/