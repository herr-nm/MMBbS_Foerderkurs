nachricht = "Es steht nur wenig freier Speicher zur Verfügung"
titel = "Wichtiger Hinweis"
durchschnittlicheRamAuslastung = 0
summeWerte = 0
auslastungRam[24] = (18,19,20,18,19,21,34,35,45,62,79,45,68,56,57,45,44,35,20,19,15,13,19,15)
for für i = 0; i < 24; i++:
    summeWerte = summeWerte + auslastungRAM[i]
durchschnittlicheRamAuslastung = summeWerte / 24
if wenn durchschnittlicheRamAuslastung > 75:
    print(titel)
    print(nachricht)
