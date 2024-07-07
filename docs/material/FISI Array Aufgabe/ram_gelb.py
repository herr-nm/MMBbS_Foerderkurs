nachricht = "Es steht nur wenig freier Speicher zur Verfügung!"
titel = "Wichtiger Hinweis"
durchschnittlicheRamAuslastung = 0
summeWerte = 0
grenzwert = int(input("Bitte geben Sie den Grenzwert ein: "))
auslastungRam = [18,1000,150,18,19,21,34,35,45,62,79,45,68,56,57,45,44,35,20,19,15,13,19,15]
for i in range(len(auslastungRam)):
    summeWerte = summeWerte + auslastungRam[i]
durchschnittlicheRamAuslastung = summeWerte / len(auslastungRam)
print(durchschnittlicheRamAuslastung)
durchschnittlicheRamAuslastung = int(durchschnittlicheRamAuslastung)
if durchschnittlicheRamAuslastung > grenzwert:
    print(titel)
    print(nachricht)
    print("Die Auslastung lag bei " + str(durchschnittlicheRamAuslastung))