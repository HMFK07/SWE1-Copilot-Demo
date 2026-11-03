# Pilot: Begriffe für ein Repair-Café

Künstliche Eingaben für `noun-extraction`, keine studentische Musterlösung und keine Freigabe realer Arbeiten. Die Lehrperson muss die Extraktion als Modellierungsvorbereitung für diesen Pilot ausdrücklich freigeben. Modellzuordnungen sind absichtlich nicht vorgegeben.

## Funktionale Anforderungen

- FA-01: Das System speichert für jedes Gerät eine Bezeichnung und eine Fehlerbeschreibung.
- FA-02: Eine Werkstatt hat eine Bezeichnung und bestätigt Reparaturaufträge für Geräte.

## User Story

- US-01: Als Kundin möchte ich eine Buchung für mein Gerät sehen, damit ich meinen Termin planen kann.

## Use Case UC-01: Reparaturauftrag anlegen

- Akteur: Kundin
- Vorbedingung: Ein Termin ist verfügbar.
- Hauptablauf:
  1. Die Kundin Anna nennt die Bezeichnung ihres Geräts und eine Fehlerbeschreibung.
  2. Das System erfasst einen Reparaturauftrag und eine Reservierung für den Termin.
  3. Die Werkstatt bestätigt den Reparaturauftrag.
- Alternativablauf: Ist kein Termin verfügbar, nimmt die Kundin ihren Wunsch in eine Warteliste auf.
- Nachbedingung des Erfolgsfalls: Der Reparaturauftrag ist bestätigt.

## Bewusst ungeklärt

Ob „Buchung“ und „Reservierung“ dasselbe bedeuten, ist nicht entschieden. Diese Notiz ist Kontext für Rückfragen und keine zusätzliche Anforderung.
