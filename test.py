#uebung_strings2

#Eingabe
eingabe = input("Bitte einen zu konvertierenden String eingeben: ")
#für jeden Buchstaben in eingabe sollen folgende Anweisungen durchgeführt werden:
anzahl = len(eingabe)
#definieren eines leeren strings, in dem die Konvertierung gespeichert werden kann
swap = ""


# für jede Stelle i im string eingabe soll vorne bis hinten eine Anweisung durchgeführt werden (for-Schleife).
# Dabei soll immer überprüft werden, welches die richtige Anweisung ist (if-Schleife)
for i in range(anzahl):
    #folgende Überprüfungen führen zur richtigen Anweisung
    if eingabe[i].islower() == True:
        #
        swap += eingabe[i].upper()
    else:
        swap += eingabe[i].lower()
print("Erfolgreiche Konvertierung: ",swap)

print("done")