# Projekte durchführen

![Kapitelbild](bilder/kapitelbild_projektmanagement.png)

In diesem Kapitel funden Sie folgende Inhalte:

- Anforderungsanalyse
- Präferenzmatrix und Nutzwertanalyse
- Netzplantechnik und Gantt-Diagramme
- Projektphasen

---

## Anforderungen analysieren

!!! info ""

   Sie lernen, wie sie die Bedürfnisse und Anforderungen von Kunden systematisch erfassen und analysieren. Sie entwickeln Fähigkeiten, um technische Lösungen passgenau zu planen und erfolgreich zu implementieren. 

### Exkurs Anforderungsanalyse

[Download der Vortragsfolien als PDF](material/Exkurs_Anforderungen_ermitteln.pdf)

### Arbeitsauftrag - Checkliste für die Anforderungen an eine neue Hardware erstellen

Erstellen Sie eine Checkliste für die Ermittlung von Anforderungen an eine neue Hardware. Gehen Sie dabei von einem gesamten Arbeitsplatz aus, der für neue Kolleg:innen bestellt werden soll. Welche Fragen sind hier zu berücksichtigen? Wie kann die Checkliste vorstrukturiert werden?

### Arbeitsauftrag - Checkliste für die Anforderungen an eine neue Software erstellen

Erstellen Sie eine Checkliste für die Ermittlung von Anforderungen an eine neue Software. Gehen Sie dabei von einem gesamten Arbeitsplatz aus, der für neue Kolleg:innen bestellt werden soll. Welche Fragen sind hier zu berücksichtigen? Wie kann die Checkliste vorstrukturiert werden?

## Präferenzmatrix und Nutzwertanalyse durchführen

!!! info ""

   Die Präferenzmatrix und Nutzwertanalyse sind Werkzeuge, die eingesetzt werden, um Entscheidungen systematisch und objektiv zu treffen. Mit der Präferenzmatrix werden verschiedene Optionen anhand festgelegter Kriterien bewertet, während die Nutzwertanalyse diese Bewertungen quantifiziert und eine klare Entscheidungshilfe bietet.

### Exkurs - Relative und absolute Adressierung in MS Excel

[Download der Vorlage in Excel](material/Exkurs_Excel_relativ_absolut.xlsx)

### Arbeitsauftrag -  Erstellung einer Präferenzmatrix

Ein neues Teammitglied soll einen neuen Computer erhalten. Zur Auswahl der besten Hardware sollen fünf Anforderungen gegenübergestellt und gewichtet werden. Die fünf Anforderungen sind:

- Prozessorleistung
- Arbeitsspeicher (RAM)
- Speicherplatz (SSD)
- Grafikkarte
- Preis

Erstellen Sie eine Präferenzmatrix, um die relative Wichtigkeit der einzelnen Anforderungen zu ermitteln. Vergleichen Sie jede Anforderung mit jeder anderen und bewerten Sie die Wichtigkeit auf einer Skala von 1 bis 5, wobei 1 bedeutet, dass die erste Anforderung weniger wichtig ist als die zweite, und 5 bedeutet, dass die erste Anforderung viel wichtiger ist als die zweite.

### Arbeitsauftrag - Erstellung einer Nutzwertanalyse

Nachdem die Präferenzmatrix erstellt und die Gewichtungen der Anforderungen ermittelt wurden, sollen nun drei mögliche Hardware-Optionen anhand dieser Gewichtungen bewertet werden. Die Optionen sind:

1. Option B
2. Option A
3. Option C

Jede Hardware-Option wird auf einer Skala von 1 bis 5 für jede Anforderung bewertet, wobei 1 für die schlechteste und 5 für die beste Erfüllung der Anforderung steht.

#### Gewichtungen der Anforderungen (aus der Präferenzmatrix)

1. Grafikkarte: 0.316
2. Prozessorleistung: 0.281
3. Arbeitsspeicher (RAM): 0.175
4. Speicherplatz (SSD): 0.140
5. Preis: 0.088

#### Bewertung der Optionen

| Anforderung | Option A | Option B | Option C |
| :--- | :---: | :---: | :---: |
| Prozessorleistung | 4 | 5 | 3 |
| Arbeitsspeicher (RAM) | 5 | 4 | 3 |
| Speicherplatz (RAM) | 3 | 5 | 4 |
| Grafikkarte | 4 | 3 | 5 |
| Preis | 3 | 2 | 5 |

## Netzplantechnik und Gantt-Diagramme erstellen

!!! info ""

   Sie lernen die Netzplantechnik und das Gantt-Diagramm als zentrale Werkzeuge des Projektmanagements kennen. Die Netzplantechnik ermöglicht die grafische Darstellung und Analyse von Abläufen und Abhängigkeiten in Projekten, während das Gantt-Diagramm zeitliche Abläufe und Meilensteine visualisiert.

### Exkurs - Netzplantechnik und Gantt-Diagramme

[Download der Vortragsfolien als PDF](material/Exkurs_Netzplantechnik_und_Gantt-Diagramme.pdf)

### Arbeitsauftrag - Projektzeit mit der Netzplantechnik visualisieren

Erstellen Sie einen Projektzeitplan für ein Softwareentwicklungsprojekt, bei dem die folgenden Aufgaben erledigt werden müssen. Bestimmen Sie die früheste und späteste Start- und Endzeit für jede Aufgabe und zeichnen Sie den Netzplan.

#### Aufgaben und Dauer

- **A:** Anforderungsspezifikation (5 Tage)
- **B:** Systemdesign (3 Tage) - kann erst beginnen, wenn **A** abgeschlossen ist.
- **C:** Implementierung (10 Tage) - kann erst beginnen, wenn **B** abgeschlossen ist.
- **D:** Testen (4 Tage) - kann erst beginnen, wenn **C** zu 50% abgeschlossen ist.
- **E:** Deployment (2 Tage) - kann erst beginnen, wenn **C** und **D** abgeschlossen sind.
- **F:** Projektabschluss (1 Tag) - kann erst beginnen, wenn **E** abgeschlossen ist.

#### Abhängigkeiten

- **B** beginnt nach **A**
- **C** beginnt nach **B**
- **D** beginnt, wenn **C** zu 50% abgeschlossen ist
- **E** beginnt nach **C** und **D**
- **F** beginnt nach **E**

### Tool-Tipp

[draw.io](https://draw.io)

### Vorlage eines Netzplans für draw.io

[Download der Vorlage](material/Vorlage%20NTP.drawio)

### Arbeitsauftrag - Projektzeit mit dem Gantt-Diagramm visualisieren

Erstellen Sie einen Projektzeitplan für ein Softwareentwicklungsprojekt, bei dem die folgenden Aufgaben erledigt werden müssen. Erstellen Sie hierfür in MS Excel ein einfaches Gantt-Diagramm.

#### Aufgaben und Dauer

- **A:** Anforderungsspezifikation (5 Tage)
- **B:** Systemdesign (3 Tage) - kann erst beginnen, wenn **A** abgeschlossen ist.
- **C:** Implementierung (10 Tage) - kann erst beginnen, wenn **B** abgeschlossen ist.
- **D:** Testen (4 Tage) - kann erst beginnen, wenn **C** zu 50% abgeschlossen ist.
- **E:** Deployment (2 Tage) - kann erst beginnen, wenn **C** und **D** abgeschlossen sind.
- **F:** Projektabschluss (1 Tag) - kann erst beginnen, wenn **E** abgeschlossen ist.

#### Abhängigkeiten

- **B** beginnt nach **A**
- **C** beginnt nach **B**
- **D** beginnt, wenn **C** zu 50% abgeschlossen ist
- **E** beginnt nach **C** und **D**
- **F** beginnt nach **E**

## Projektphasen unterscheiden

### Arbeitsauftrag - Projektphasen unterscheiden

Erstellen Sie sich eine Übersicht in Form einer Mind-Map zum Thema "Projektphasen".

- Tooltipp: [TeamMapper](https://map.kits.blog/)
- Informationsmaterial - Projektphasen

### Informationsmaterial - Projektphasen

Ein Projekt wird in der Regel in fünf klar definierte Phasen unterteilt, um eine strukturierte und effiziente Durchführung zu gewährleisten. Diese Phasen sind Initiierung, Planung, Durchführung, Überwachung und Abschluss.

1. **Initiierung:** Die Initiierungsphase markiert den Beginn eines Projekts. In dieser Phase wird die Projekt1. idee definiert und bewertet, um ihre Machbarkeit und den Nutzen zu bestimmen. Wichtige Aktivitäten umfassen die Erstellung eines Projektauftrags, die Bestimmung der Projektziele und die Ernennung eines Projektmanagers. Die Stakeholder werden identifiziert und ein erster grober Zeit- und Kostenrahmen wird festgelegt.
2. **Planung:** Die Planungsphase ist entscheidend für den Erfolg des Projekts. Hier werden detaillierte Pläne estellt, die als Fahrplan für die Projektumsetzung Dienen. Dazu gehören die Entwicklung eines Projektstrukturplans, die Festlegung von Meilensteinen und die Erstellung eines Zeitplans. Ressourcen werden zugewiesen, Budgets festgelegt und Risikomanagementpläne entwickelt. Die Kommunikation und das Änderungsmanagement werden ebenfalls in dieser Phase geplant, um sicherzustellen, dass alle Beteiligten informiert und an Bord sind.
3. **Durchführung:** In der Durchführungsphase werden die Pläne in die Tat umgesetzt. Das Projektteam führt d1. e Aufgaben aus, die im Projektplan definiert wurden, und arbeitet daran, die Projektziele zu erreichen. Diese Phase erfordert effektives Teammanagement, klare Kommunikation und die kontinuierliche Überwachung des Fortschritts. Bei Bedarf müssen Anpassungen vorgenommen werden, um den Plan einzuhalten. Hierbei ist es wichtig, dass der Projektleiter motiviert bleibt und Konflikte löst, die den Fortschritt behindern könnten.
4. **Überwachung und Kontrolle:** Die Überwachungs- und Kontrollphase läuft parallel zur Durchführung und stellt sicher, dass das Projekt auf Kurs bleibt. In dieser Phase werden die Fortschritte regelmäßig überprüft und mit den geplanten Zielen und Meilensteinen abgeglichen. Abweichungen werden identifiziert und korrigierende Maßnahmen ergriffen. Wichtige Aktivitäten umfassen das Performance-Reporting, das Management von Änderungen und das Risikomanagement. Durch kontinuierliche Überwachung können Probleme frühzeitig erkannt und behoben werden.
5. **Abschluss:** Die Abschlussphase markiert das Ende des Projekts. Hier wird sichergestellt, dass alle Projektziele erreicht wurden und das Projekt ordnungsgemäß abgeschlossen wird. Dies umfasst die Abnahme durch den Kunden, die Dokumentation aller Ergebnisse und die Übergabe an den Betrieb oder den Kunden. Eine Nachbesprechung oder ein Projektabschlussbericht wird erstellt, um Erkenntnisse und Verbesserungspotentiale für zukünftige Projekte zu dokumentieren. Die Teammitglieder werden entlastet und das Projekt wird offiziell geschlossen.

### Arbeitsauftrag - Kreuzworträtsel zu den Projektphasen

*Interaktives Inhaltselement im Moodle-Kurs*

{%
   include-markdown "inhalte/lizenzhinweis.md"
   start="<!--include-start-->"
   end="<!--include-end-->"
%}