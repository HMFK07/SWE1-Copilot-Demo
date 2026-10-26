# Offene Entscheidungen und Demoannahmen

**Status:** Engineering-Dokumentation für künstliches Demomaterial.
Diese Übersicht präzisiert den Demo-Umfang; sie ändert weder die
[Quellen](../lehrpfad.md#quellen-status-und-freigaben) noch Semesterregeln.
Es hat noch keine Challenge-/Compare-Vorführung mit anschließender menschlicher
fachlicher Revision stattgefunden.

## Menschlich entschiedener Demo-Umfang

Die folgenden Festlegungen stammen ausdrücklich aus dem Auftrag „SWE1-Demo – AP2“.
Sie sind keine aus dem Szenario abgeleiteten verbindlichen Produktanforderungen.

| ID | Im Auftrag entschiedene Demoannahme | Begründung und Grenze |
|---|---|---|
| DA-01 / I1 | Bekannte Start-/Zielstrecke für eine neue Suche übernehmen; einen neuen Suchzeitpunkt verwenden. Keine automatische Persistenz. | Kleiner, beobachtbarer Schritt zum Bedürfnis nach weniger Wiederholung. Woher die bekannte Strecke kommt und wie der Zeitpunkt übergeben wird, bleibt vor dem Codeauftrag zu präzisieren. |
| DA-02 / I2 | Künstliche Fahrtoptionen nach einem ausdrücklich beschlossenen Zeitfenster filtern; Normal-, Grenz- und Leerfälle testen. | Ermöglicht nachvollziehbare Beispiele ohne realen Fahrplandienst. Die genaue Zeitfenstersemantik ist noch nicht beschlossen. |
| DA-03 / Aufbau | Ein gemeinsamer wachsender Mobilitäts-Fachkern; I1 und I2 jetzt nur planen. | Keine Anwendungskopien pro Stufe, kein Code und keine Stackentscheidung in AP2. |

## Offene fachliche und technische Entscheidungen

| ID | Frage und mögliche Alternativen | Aktueller Stand / vor Umsetzung zu klären |
|---|---|---|
| OF-D1 | Wie steht eine bekannte Strecke bereit: explizit übergebene Daten, laufende Sitzung oder bewusst gespeicherte Auswahl? | Produktentscheidung offen. Für I1 keine automatische Persistenz; vor Implementierung einen begrenzten Eingabevertrag beschließen. RE-D1 begründet keine Speichertechnik. |
| OF-D2 | Was bedeutet „aktuelle Abfahrtsdaten“: neue Abfrage, sichtbarer Datenstand oder zusätzlich eine erlaubte Altersgrenze? | Offen. Ein neuer Suchzeitpunkt allein beweist keine frischen Fahrplandaten. I1 prüft nur den neuen Suchauftrag; I2 arbeitet mit künstlichen Optionen. Eine echte Aktualitätszusage benötigt später Datenvertrag und Kriterien. |
| OF-D3 | Ist ein Benutzerkonto nötig, optional oder für die betrachtete Nutzung entbehrlich? | Offen gemäß PV-01/P01. Kein Konto als Voraussetzung von I1/I2 einführen. Das entscheidet nicht über das Gesamtprodukt. |
| OF-D4 | Was ist „rechtzeitig“, und wie wird das Zeitfenster geprüft? | Offen: Abfahrtsuntergrenze, Ankunftsobergrenze, Gleichheit an Grenzen, Datum/Zeitzone, ungültige Eingaben. Vor I2 explizit beschließen. |
| OF-D5 | Wie werden frühere Suchergebnisse von Ergebnissen einer neuen Suche unterscheidbar? | Offen: Kennzeichnung, Austausch oder andere Interaktion. Später sichtbare Kriterien festlegen; keine Cache- oder UI-Architektur daraus ableiten. |
| OF-D6 | Was bedeutet „schnell erkennen“? | Noch kein messbares Qualitätskriterium. Ein menschlich begründetes Bedienbeispiel beziehungsweise Messverfahren fehlt. |

Ticketkauf, Zahlungsabwicklung, reale Datenanbindung und technische Architektur
werden für I1/I2 nicht entschieden. Störungen, fehlendes Internet und komplexe
Tarife bleiben gemäß S01 außerhalb dieses Kontext-Slices.

## Vorläufiger Vorschlag für ein späteres I2-Gespräch

**Vorschlag, nicht beschlossen:** Nur gültige künstliche Optionen derselben Strecke
an einem gemeinsamen Tag betrachten. Abfahrt mindestens 08:00 und Ankunft spätestens
08:45, jeweils einschließlich der Grenze. Alle passenden Optionen ausgeben;
keine „beste Verbindung“ automatisch auswählen. Datumswechsel, ungültige Eingaben
und Ergebnisreihenfolge vor einer Implementierung ausdrücklich abgrenzen.

| Beispiel | Abfahrt → Ankunft | Erwartung nur unter diesem Vorschlag |
|---|---|---|
| Normalfall | 08:05 → 08:40 | enthalten |
| Zu frühe Abfahrt | 07:55 → 08:25 | nicht enthalten |
| Zu späte Ankunft | 08:20 → 08:55 | nicht enthalten |
| Gleichheit an beiden Grenzen | 08:00 → 08:45 | enthalten |
| Leerfall | Dieselben Optionen, Fenster 09:00–09:15 | keine enthalten |

Dies sind illustrative Akzeptanzbeispiele, keine ausgeführten Tests. Sie ergänzen
die Erstfassung nicht automatisch. Die Demoentscheidung über OF-D4 ist weiterhin offen.

## Vorlage für spätere menschliche Entscheidungen

Nach der Vorführung pro Punkt festhalten, ohne eine Zustimmung vorwegzunehmen:

- **Bezug:** RE-D… / OF-D… und Quellenaussage oder ausdrücklich neue Demoannahme.
- **Beobachtung:** Was war unklar? Was hat die Challenge tatsächlich gezeigt?
- **Compare-Vorschlag:** Wortlaut oder Referenz, ausdrücklich als KI-Vorschlag.
- **Menschliche Entscheidung:** annehmen / ablehnen / zurückstellen, mit Begründung.
- **Folge:** betroffene Anforderung, Akzeptanzbeispiel und verbleibende offene Frage.
- **Nachweis:** entscheidende Person, Datum und Transfercheck ohne KI.

Bis eine Person dies tatsächlich entscheidet, bleibt der Eintrag Vorschlag oder
offene Frage. Für den [Demoablauf](../demo/requirements.md) ist die Erstfassung der
Ausgangspunkt; diese Übersicht ist kein vorab erzeugtes Challenge-Ergebnis.
