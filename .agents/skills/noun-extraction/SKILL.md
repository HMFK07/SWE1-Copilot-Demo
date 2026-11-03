---
name: noun-extraction
description: "Extrahiert nach Freigabe Substantive aus funktionalen Anforderungen, User Stories und Use Cases als belegte Begriffsliste für den Einstieg in UML-Objekt- und Klassenmodelle. Studierende beurteilen selbst Klassen-, Attribut- und Komponentenkandidaten; der Skill erstellt kein fertiges Modell."
---
# Noun Extraction – von Prosa zu Modellkandidaten

**Lernziel (4–5):** Studierende unterscheiden sprachliche Begriffe von Modellelementen und begründen anhand von Anforderungen, welche Begriffe sie weiter modellieren oder verwerfen.

## Eingang und Grenze
Aktuelles Übungsblatt, ausdrückliche Freigabe **für diese Extraktion als Modellierungsvorbereitung** und benannte Listen funktionaler Anforderungen, User Stories und/oder Use Cases. Eine einzelne dieser Quellen genügt; ein UML-Erstentwurf ist hier noch nicht nötig. Eine Requirements-Review-Freigabe allein erlaubt diese Vorbereitung nicht automatisch. Ohne passende Freigabe keine konkrete Extraktion; nur abstrakte Methodenerklärung. Regeln aus `docs/SEMESTERREGELN.md` bleiben verbindlich.

## Extrahieren, noch nicht einordnen
1. Lies nur die benannten Quellen. Übernimm vorhandene Anforderungs-/Story-/Use-Case-IDs; ergänze für fehlende IDs nachvollziehbare Fundstellen (Datei und Zeile bzw. Abschnitt). Berücksichtige im freigegebenen Umfang auch Vorbedingungen, Nachbedingungen und Alternativabläufe. Fehlende oder unlesbare Quellen benennen, nichts ergänzen.
2. Sammle Substantive, substantivierte Ausdrücke und Eigennamen mit ihrem Kontext. Erhalte fachliche Mehrwortbegriffe und Komposita; zerlege sie nicht in erfundene Teilbegriffe. Verben nicht nur durch Großschreibung zu Substantiven machen. Bei sprachlicher Unsicherheit kennzeichne die Stelle.
3. Führe Flexionsformen desselben Begriffs in derselben Bedeutung unter einer Grundform zusammen; erhalte Originalformen und alle Fundstellen. Lass unterschiedliche Bedeutungen getrennt. Mögliche Synonyme, Abkürzungen und Rollenvarianten nur als Klärungsbedarf markieren, nicht still gleichsetzen. Streiche weder generische Wörter wie „System“ noch technische Begriffe oder Akteure vorab wegen vermuteter Modellrelevanz.
4. Gib eine **unbewertete Arbeitsliste** aus: `ID | Originalform(en) | Grundform/Begriff | Fundstelle(n) mit kurzem Originalbeleg | sprachliche Unklarheit | studentische Einordnung | studentische Begründung`. Die letzten beiden Spalten bleiben „offen“. Vergib weder Kategorien noch Rangfolgen vorab. Bei langen Quellen arbeite in kenntlich gemachten Abschnitten, nenne bearbeiteten und verbleibenden Umfang; behaupte keine Vollständigkeit bei Teilausgaben.

## Studierende untersuchen
Bitte das Team, zunächst einige Begriffe selbst einzuordnen und mit einem Quellenbeleg zu begründen. Mögliche Ergebnisse sind **Klassenkandidat, Attributkandidat, Komponentenkandidat, konkretes Objekt/Instanz, nicht modellrelevant oder unklar**; mehrere begründete Möglichkeiten bleiben zulässig. Stelle höchstens drei offene Fragen und warte auf Antworten. Keine ausgefüllte Musterklassifikation in der ersten Ausgabe.

Bei Lehrendenaufträgen dient die Liste als Arbeitsblatt; richte die Untersuchungsfragen an die Studierenden, ohne Antworten oder Entscheidungen vorwegzunehmen.

Nutze bei der anschließenden Besprechung diese Prüfkriterien, ohne daraus automatisch Zuordnungen abzuleiten:
- Klasse oder Objekt: Ist ein Typ mit gemeinsamen Eigenschaften gemeint oder eine konkrete Instanz? Ein Objektmodell zeigt konkrete Instanzen, Werte und Links in einer Situation; ein Klassenmodell beschreibt Typen und deren Struktur. Erfinde keine Instanzen oder Werte.
- Attribut: Wessen Eigenschaft wäre der Begriff, und warum benötigt er im gewählten Modell keine eigene Identität? Eine Klasse muss nicht allein wegen eines Substantivs entstehen.
- Komponente: Welche zusammenhängende Verantwortung und welche Schnittstelle begründen eine Systemzerlegung? Komponenten sind eine andere Sicht als fachliche Klassen; ein Substantiv allein belegt keine Komponente. Externe Rollen und Systeme können außerhalb der Modellgrenze liegen.

## Abschluss und Übergang
Halte höchstens fünf belegte Lernpunkte oder offene Entscheidungen fest. Übernimm studentische Zuordnungen als solche; Feedback und Alternativen getrennt kennzeichnen. Keine Kategorien im Namen der Studierenden entscheiden. Das Team erstellt anschließend eigenständig seinen ersten Objekt-/Klassenentwurf; Beziehungen, Multiplizitäten, Vererbung und Operationen folgen nicht automatisch aus der Wortliste. Kein UML-/PlantUML-Diagramm oder Code in diesem Skill. Keine anderen Skills automatisch starten. Ergebnisse nur auf ausdrücklichen Auftrag speichern; Anforderungen und vorhandene Modelle unverändert lassen.

**Learning Check:** Welcher Begriff wurde erst durch seinen Kontext zum Modellkandidaten, und welche andere Einordnung wäre mit einer anderen Systemgrenze plausibel?
