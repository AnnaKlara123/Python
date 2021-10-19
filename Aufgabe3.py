#start
import math

#Variablen definieren
racetime_min = 43.5 
racetime_h= racetime_min/60
print(racetime_h)

racelength_km = 10.0
racelength_mi= racelength_km/1.61
print(racelength_mi)

#Rechnung

averagetime = racelength_mi/racetime_h
print(averagetime)
# Durschnittliche Zeit pro Mile = 8.57mi/h

averagespeed = racetime_h/racelength_mi*6
print(averagespeed)
# Durschnittliche Geschwindigkeit pro Mile = 7min/mi