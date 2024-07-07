nachricht = "Es steht nur wenig freier Speicher zur Verfügung!"
titel = "Wichtiger Hinweis"
durchschnittlicheRamAuslastung = 0
summeWerte = 0
auslastungRam = [18,1001,18,18,19,21,34,35,45,62,79,45,68,56,57,45,44,35,20,19,15,13,19,15]
grenzwert = int(input("Geben Sie einen Grenzwert ein: "))
for x in auslastungRam:
    summeWerte += x
durchschnittlicheRamAuslastung = summeWerte / 24
if durchschnittlicheRamAuslastung > grenzwert:
    print(titel)
    print(nachricht)
    print("Die durchschnittliche RAM-Auslastung lag bei " + str(int(durchschnittlicheRamAuslastung)))