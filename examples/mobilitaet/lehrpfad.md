# Mobilitäts-Demonstrator – inkrementeller Lehrpfad

**Status:** Didaktischer Vorschlag für das Kollegendemonstrationsrepository,
AP2. Keine verbindliche Semesteraufgabe und keine studentische KI-Freigabe.
Die sechs Stufen beschreiben einen gemeinsamen, schrittweise wachsenden Fachkern;
es entstehen keine vollständigen Anwendungskopien pro Stufe.

## Quellen, Status und Freigaben

- [PV-01 – Produktvision](../../docs/product/vision.md),
  [P01 – Nora Fischer](../../docs/personas/P01-junge-pendlerin.md) und
  [S01 – tägliche Fahrt](../../docs/scenarios/S01-taegliche-fahrt.md)
  sind unveränderte fachliche Quellen, keine fertige Spezifikation.
- Die [Requirements-Erstfassung](artefakte/requirements-erstfassung.md) ist
  künstliches Demomaterial. [Entscheidungen](artefakte/entscheidungen.md)
  unterscheiden offene Fragen, Vorschläge und ausdrücklich beauftragte Demoannahmen.
- Für WS 2026/27 gilt gemäß dem bestätigten Engineering-Auftrag: zunächst eigene
  Anforderungserhebung und Modellierung ohne KI; auch Anforderungen,
  Akzeptanzkriterien und priorisierte Feature-Roadmap entstehen eigenständig.
  Studentische Requirements Challenge benötigt eine spätere ausdrückliche Freigabe,
  Compare zusätzlich eine gesonderte Freigabe nach eigener Erstfassung.
  Die [Semesterdatei](../../docs/SEMESTERREGELN.md) ist weiterhin eine unbefüllte
  Vorlage und erteilt keine aktuelle Freigabe.
- Der vorliegende Auftrag erlaubt künstliche Demonstrationsartefakte. Die
  [Promptvorlagen](demo/requirements.md) sind Material für eine spätere Vorführung;
  sie wurden hier nicht als Copilot-Sitzungen ausgeführt. Die konkrete Freigabe
  wird dort für Challenge und Compare getrennt erklärt. Sie gilt nie für echte
  studentische Arbeiten. Engineering- und Copilot-Instruktionen bleiben unverändert.

## 1. Kontext verstehen

- **Lernziel und Eigenleistung:** Bedürfnisse, Beobachtungen und mögliche Lösungen
  unterscheiden; Aussagen aus P01/S01 begründet einordnen.
- **Artefakte:** Vorhanden sind PV-01/P01/S01. Neu genügt eine kurze, menschlich
  erstellte Zuordnung „Quellenaussage – Interpretation – offene Frage“;
  die Originale werden nicht ergänzt oder umgeschrieben.
- **Kleinstes Beispiel:** Drei Aussagen am Szenario durchgehen: wiederholte Eingaben
  vermeiden, aktuelle Abfahrten erkennen, ein Benutzerkonto einsetzen.
  Noch kein ausführbarer Anwendungscode.
- **Copilot-Rolle und Grenze:** Im KI-freien studentischen Kontext keine konkrete
  Analyse oder Korrektur dieser Eigenleistung. Im freigegebenen künstlichen
  Kollegensetting lassen sich Quellen- und Scopegrenzen demonstrieren (Demo D).
- **Verständnischeck ohne KI:** Erklären, warum „bekannte Strecke wiederverwenden“
  weder ein Konto noch automatische Speicherung festlegt.
- **Prüfung und Grenze:** Quellenverweise und Kennzeichnungen prüfen; das belegt
  weder validierte Nutzerbedürfnisse noch funktionierende Software.
- **Abhängigkeit:** Nur die drei Quellen und die geltenden Kursregeln.

## 2. Anforderungen und Akzeptanzkriterien reflektieren

- **Lernziel und Eigenleistung:** Aus eigener Erstfassung prüfbare Aussagen und
  Beispiele entwickeln, Unklarheiten benennen und Änderungen selbst begründen.
- **Artefakte:** Die künstliche Erstfassung mit RE-D1 bis RE-D3 dient als
  Demonstrationsausgangspunkt. Neu entstehen im Termin getrennt markierte
  Challenge-Beobachtungen, vorläufige Compare-Vorschläge, menschliche Entscheidungen
  und gegebenenfalls revidierte Kriterien; die Erstfassung bleibt erhalten.
- **Kleinstes Beispiel:** Einen Fall für Streckenübernahme und neuen Suchzeitpunkt
  auf Papier durchspielen. I2 erst nach einer expliziten Entscheidung über das
  Zeitfenster präzisieren. Noch keine Anwendung ausführen.
- **Copilot-Rolle und Grenze:** Requirements Challenge (Demo A) fragt nach Lücken;
  erst die gesonderte Compare-Freigabe erlaubt einen begrenzten Vorschlag (Demo B).
  Keine automatische Revision, keine Musterlösung und keine UML-Freigabe daraus
  ableiten. Für reale Studierende bleibt die Erstfassung zunächst KI-frei.
- **Verständnischeck ohne KI:** Eine vorgeschlagene Änderung annehmen oder ablehnen,
  mit Quelle beziehungsweise Demoentscheidung begründen und an einem neuen Fall prüfen.
- **Prüfung und Grenze:** Anforderung, Beispiel und Entscheidung auf Widersprüche
  prüfen; ein schlüssiges Akzeptanzbeispiel ist noch kein ausgeführter Softwaretest.
- **Abhängigkeit:** Stufe 1, vorliegende Erstfassung und getrennte Freigaben.

## 3. Kleine fachliche Implementierung und Tests

- **Lernziel und Eigenleistung:** Einen begrenzten Vertrag in Verhalten übersetzen,
  erwartete Ergebnisse vor der Generierung festlegen und Code erklären können.
- **Artefakte:** Später freigegebener I1-Vertrag, danach I2-Vertrag; ein gemeinsamer
  Fachkern mit Testfällen und kleinem ausführbarem Einstieg. In AP2 entsteht kein Code.
- **Kleinstes ausführbares Beispiel:** Zuerst I1: bekannte Start-/Zielstrecke für
  eine neue Suche übernehmen und einen neu angegebenen Suchzeitpunkt verwenden,
  ohne automatische Persistenz. Danach I2: künstliche Fahrtoptionen gemäß dem
  ausdrücklich beschlossenen Zeitfenster filtern. Exakte Eingaben, Ausgaben und
  Grenzregeln sind vor der jeweiligen Implementierung festzulegen.
- **Copilot-Rolle und Grenze:** Direkte kleine Implementierung samt Tests (Demo C)
  ist bei passendem Kursauftrag erlaubt; dafür keine zusätzliche Challenge- oder
  Compare-Freigabe verlangen. Keine Konten, Speicherung oder Datenanbieter ergänzen.
- **Verständnischeck ohne KI:** Für eine zweite Suche vorhersagen, welche Angaben
  übernommen und welche ersetzt werden; einen neuen I2-Grenzfall erklären.
- **Tests und Grenze:** I1 prüft Streckenübernahme und Austausch des Suchzeitpunkts;
  I2 erhält Normal-, Grenz- und Leerfalltests. Künstliche Daten belegen keine
  aktuellen realen Abfahrten. Testgrün belegt kein Verständnis und keine Nutzerakzeptanz.
- **Abhängigkeit:** Entschiedener Demo-Vertrag aus Stufe 2 und gesonderter Codeauftrag.

## 4. UML, Code und Tests verbinden

- **Lernziel und Eigenleistung:** Fachbegriffe, Modellbeziehungen und beobachtbares
  Codeverhalten aufeinander beziehen; Abstraktion von Widerspruch unterscheiden.
- **Artefakte:** Derselbe I1/I2-Fachkern und seine Tests; später ein eigener kleiner
  UML-Entwurf und eine Zuordnung von Anforderungs-ID, Modellstelle und Testfall.
- **Kleinstes ausführbares Beispiel:** Vorhandene Fälle erneut ausführen und einen
  Fall anhand des Modells erklären. Keine zweite Implementierung für das Diagramm.
- **Copilot-Rolle und Grenze:** Konkreter studentischer UML-Review nur nach eigener
  Modellierung und ausdrücklicher Freigabe; UML-Compare separat. Requirements-
  Freigaben gelten dafür nicht. Keine eigenmächtige Modelländerung.
- **Verständnischeck ohne KI:** Eine Modellbeziehung begründen und zeigen, welches
  Verhalten ein zugeordneter Test tatsächlich prüft und welches nicht.
- **Tests und Grenze:** Regression des Fachkerns und gegebenenfalls Diagrammrendering;
  Renderbarkeit beweist weder UML-Semantik noch fachliche Richtigkeit.
- **Abhängigkeit:** Stufe 3 und eigener Modellstand. Diese Demoabfolge legt nicht
  fest, wann Studierende im Semester erstmals modellieren müssen.

## 5. Sichtbare Benutzerinteraktion

- **Lernziel und Eigenleistung:** Eingabe, Fachlogik und Rückmeldung verbinden und
  verständliches Verhalten aus Sicht Noras beurteilen.
- **Artefakte:** Bestehender Fachkern; später eine dünne Oberfläche mit explizit
  entschiedenen Interaktionskriterien. Technologie und Ausgestaltung bleiben offen.
- **Kleinstes ausführbares Beispiel:** Bekannte Strecke übernehmen, neuen Suchzeitpunkt
  eingeben, künstliche Optionen für das entschiedene Fenster beziehungsweise einen
  Leerhinweis anzeigen. Die Oberfläche verwendet dieselbe Fachlogik.
- **Copilot-Rolle und Grenze:** Kleine, ausdrücklich beauftragte UI-Schritte erzeugen;
  keine Anmeldung, automatische Persistenz oder Ticketzahlung hinzufügen.
- **Verständnischeck ohne KI:** Datenfluss einer erneuten Suche erklären und an
  einer veränderten Eingabe das sichtbare Ergebnis vorhersagen.
- **Tests und Grenze:** Fachkerntests bleiben bestehen; Interaktion und Rückmeldung
  gezielt prüfen. Bestehende Tests beweisen keine Gebrauchstauglichkeit für Nora.
- **Abhängigkeit:** Stufen 3/4, technische Abwägung und expliziter UI-Auftrag.

## 6. Integration und Qualitätsanforderungen

- **Lernziel und Eigenleistung:** Eine Qualitätsforderung messbar machen und
  Fachverhalten von Annahmen über einen Datenlieferanten unterscheiden.
- **Artefakte:** Derselbe Fachkern und UI; später ein beschlossener Datenvertrag,
  messbare Qualitätskriterien und wenige Integrationstests mit künstlichem Lieferanten.
- **Kleinstes ausführbares Beispiel:** Vorschlag: zwei aufeinanderfolgende Suchen
  mit künstlich verzögerten Antworten; eine ältere Antwort soll die neuere Suche
  nicht überlagern. Das ist noch keine entschiedene Produktanforderung.
- **Copilot-Rolle und Grenze:** Innerhalb eines gesonderten Auftrags bei Tests und
  Adapter helfen; keine echten Fahrplandienste, Konten oder Kaufabläufe vorwegnehmen.
- **Verständnischeck ohne KI:** Für zwei vertauschte Antwortreihenfolgen das erwartete
  Ergebnis begründen und eine nicht abgedeckte Qualitätsfrage nennen.
- **Tests und Grenze:** Deterministische Integrationstests prüfen den vereinbarten
  Vertrag, keine reale Datenfrische, Anbieterkompatibilität oder Betriebszuverlässigkeit.
- **Abhängigkeit:** Stufe 5 und ausdrückliche Entscheidung über Vertrag und Qualitätsziel.

## Umsetzung und Vorführung

Zuerst Requirements-Demo und menschliche Entscheidungen erproben (AP2), danach I1
mit Tests, anschließend I2, Modellbezug, UI und Integration gesondert beauftragen.
Ein Technologie-Stack wird hier nicht festgelegt. Künftige Implementierungen liegen
einmal unter `examples/mobilitaet/`; [examples/pilot](../pilot/README.md) bleibt ein
separater Regressionstest. Die [Demoanleitung](demo/requirements.md) bietet einen
30–45-minütigen Ausschnitt mit Schwerpunkt auf Stufen 1/2.

Die Auswertung trennt **fachlichen Lernerfolg** (Begründung und Transfer ohne KI),
**technische Korrektheit** (tatsächlich ausgeführte Tests gegen einen Vertrag) und
**Copilot-Verhalten** (beobachtete Einhaltung von Freigabe und Scope). Keiner dieser
Nachweise ersetzt die anderen; AP2 liefert Dokumente, noch keine Laufzeitergebnisse.
