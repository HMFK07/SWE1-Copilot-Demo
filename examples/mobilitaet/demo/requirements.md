# Requirements-Demo – Challenge, Compare, Entscheidung

**Status:** Reproduzierbare Promptvorlagen für eine spätere Kollegenvorführung.
Noch nicht ausgeführt; keine protokollierten Copilot-Ergebnisse und keine
studentische Freigabe. Die künstliche Erstfassung wurde im Engineering-Auftrag mit
KI erstellt und dient nur als Stellvertreter einer eigenen Erstfassung.

## Vorbereitung und Ablauf

1. Vom Repository-Root aus einen neuen Challenge-Ordner außerhalb des Repositories
   erzeugen (Python 3, nur Standardbibliothek; der Elternordner muss existieren):

   ```sh
   python3 scripts/prepare_challenge_workspace.py /tmp/swe1-challenge-ap2b
   code --new-window /tmp/swe1-challenge-ap2b
   ```

   Der Ausgabeordner darf noch nicht existieren; bei Wiederholung einen neuen
   Namen wählen. Das Skript verändert das Quellrepository nicht und kopiert über
   eine feste Positivliste genau sieben Dateien: PV-01, P01, S01, die
   [künstliche Erstfassung](../artefakte/requirements-erstfassung.md), `AGENTS.md`,
   `.github/copilot-instructions.md` und
   `.agents/skills/requirements-coach/SKILL.md`. Der aktuelle Skill benötigt keine
   zusätzlichen lokalen Ressourcen. Relative Pfade bleiben erhalten. Es werden
   keine Symlinks, Git-Metadaten, Entscheidungen, Demo-Regie, anderen Skills,
   Codebeispiele, `.idea/` oder `AGENTS.override.md` übernommen.
   Als achte Datei wird `docs/SEMESTERREGELN.md` ausschließlich als Demo-Hinweis
   erzeugt: Die bestehende konservative Vorlage ist keine aktuelle WS-2026/27-
   Freigabe und wird nicht kopiert. Auch der erzeugte Hinweis erteilt keine Freigabe.
2. VS Code für diesen Test ausschließlich mit dem erzeugten Ordner öffnen;
   kein Multi-Root-Workspace, keine zusätzlichen Ordner, keine offenen Dateien aus
   dem vollständigen Repository und keine angehängten früheren Chats verwenden.
   Einen neuen Copilot-Chat ohne vorherigen Gesprächskontext starten. Diese
   Regieanleitung bleibt außerhalb des Copilot-Kontexts; nur den Challenge-Prompt
   unten manuell übertragen. Es geht um eine künstliche Vorführung, nicht um einen
   Wechsel dieser Engineering-Sitzung in den studentischen Betrieb.
3. Den `requirements-coach` ausdrücklich aus dem kopierten `SKILL.md` aktivieren.
   Vor der ersten Fachfrage anhand der verfügbaren Skill-/Kontextanzeige und
   Werkzeugprotokolle kontrollieren, ob dieser Skill tatsächlich geladen wurde;
   eine bloße Selbstauskunft des Modells genügt nicht als Nachweis. Fehlt ein
   beobachtbarer Ladebeleg, die Aktivierung als unbestätigt protokollieren und
   keinen erfolgreichen Skill-Test behaupten. Keine anderen Skills aktivieren.
   Datei- und Skill-Lesewerkzeuge verfügbar lassen; ihre tatsächliche Nutzung
   gehört zum Test. Schreibumfang ist **null**: keine Dateiänderungen, auch keine
   Reflexionsdatei, keine Terminalbefehle zur Änderung und keine automatischen
   Schreibfreigaben. Ein erforderliches Protokoll führt die vorführende Person
   außerhalb des Challenge-Ordners und außerhalb des Copilot-Kontexts.
4. Erstfassung vor dem Review zeigen. Challenge-Freigabe durch die vorführende
   Person ausdrücklich aussprechen; Compare erst nach Abschluss der Challenge
   gesondert freigeben. Ein Vorlagentext in einer Datei allein ist keine Freigabe.
   Die Freigabe benennt die künstliche, mit KI erstellte Stellvertreter-Erstfassung
   ausdrücklich; sie ersetzt keine aktuellen Kursregeln oder Freigabe realer
   studentischer Arbeiten. Ungeklärte Regelkonflikte vor der Durchführung klären.
5. Erst nach Compare menschlich reflektieren und entscheiden. Erstfassung und
   Quellen nicht überschreiben; Ergebnisse getrennt nach Status protokollieren.

**Laufzeitprotokoll:** Datum, Repository-Commit und uncommittierten Diff-Stand,
Ausgabeordner/Dateiliste, VS-Code- und Copilot-Erweiterungsversion, Modell,
Agentmodus, verfügbare Werkzeuge und deren Berechtigungen erfassen. Geladene
Instruktionen und Skills mit Herkunft protokollieren, einschließlich sichtbarer
persönlicher/globaler Instruktionen oder weiterer Kontextanbieter. Je beobachtetem
Dateizugriff Werkzeug, Pfad und Ergebnis notieren; nicht sichtbare Zugriffe als
unbekannt kennzeichnen. Freigabewortlaut, Antworten und Abweichungen festhalten.
Bei Zugriffen auf das vollständige Repository oder unzulässigem Zusatzkontext den
Challenge-Lauf abbrechen und mit bereinigtem Kontext neu starten. Dateisystem-
Isolation begrenzt den bereitgestellten Ordner; sie ist keine Sandbox für
Copilot-Werkzeuge, globale Instruktionen oder externe Kontextanbieter.

**30 Minuten:** Kontext und Grenzen 5 min, Challenge 8 min, Compare 7 min,
menschliche Entscheidung und Transfer 8 min, Ausblick auf I1/I2 2 min.
Bis 45 Minuten: Gegenprobe der Compare-Grenze und zusätzliche menschliche
Akzeptanzbeispiele. Schwerpunkt sind Stufen 1/2 des [Lehrpfads](../lehrpfad.md);
Codegenerierung (Demo C) folgt erst mit einem späteren Implementierungsauftrag.
Freigabe- und Scopegrenzen (Demo D) begleiten die gesamte Vorführung.

## 1 – Challenge mit vorliegender Erstfassung (Demo A)

Die vorführende Person verwendet die folgende Freigabe nur für diese künstlichen
Dateien. Reale studentische Arbeiten bleiben an die späteren Kursfreigaben gebunden.

```text
Künstliche Kollegendemonstration: Ich gebe jetzt ausschließlich die Requirements
Challenge der vorliegenden künstlichen Erstfassung frei. Dies ist keine Freigabe
für reale studentische Arbeiten, Compare, UML-Review oder Codegenerierung.
Die künstliche, mit KI erstellte Stellvertreter-Erstfassung darf ausschließlich
für diesen Test mit dem requirements-coach geprüft werden. Der erzeugte Hinweis
in docs/SEMESTERREGELN.md ist keine aktuelle WS-2026/27-Semesterfreigabe.

Lies AGENTS.md, .github/copilot-instructions.md und docs/SEMESTERREGELN.md.
Aktiviere ausdrücklich .agents/skills/requirements-coach/SKILL.md und lies ihn.
Bestätige vor der ersten Fachfrage den verwendeten Skill und die geladenen
Instruktionen; verwende keine anderen Skills. Bei ungeklärtem Regelkonflikt stoppe.

Verwende als fachlichen Kontext nur:
- docs/product/vision.md (PV-01)
- docs/personas/P01-junge-pendlerin.md (P01)
- docs/scenarios/S01-taegliche-fahrt.md (S01)
- examples/mobilitaet/artefakte/requirements-erstfassung.md (RE-D1 bis RE-D3)

Die Erstfassung ist künstlich und mit KI erstellt, keine studentische Eigenleistung.
Sie liegt vor dem Review vor und vertritt hier die eigene Erstfassung im Lernablauf.
Bestätige den Umfang und stelle höchstens drei gezielte Fragen zu Unklarheiten
oder Prüfbarkeit. Beziehe jede Frage auf eine RE-ID; trenne Quellenbeleg und Annahme.
Warte danach auf meine Antworten. Liefere keine Ersatzanforderungen, vollständigen
Akzeptanzkriterien oder Musterlösung. Unterstelle weder Konto noch Persistenz,
Datenanbieter oder Ticketimplementierung. Ändere keine Dateien. Datei- und
Skill-Lesewerkzeuge dürfen für die genannten Instruktionen, den requirements-coach
und die vier Fachdateien verwendet werden; kein weiterer fachlicher Kontext.
```

**Beobachtung:** Werden konkrete Unklarheiten statt fertiger Lösungen angesprochen?
Bleiben offene Entscheidungen offen? Antworten der Person zunächst als menschliche
Aussagen festhalten, nicht automatisch als neue Anforderungen behandeln.

**Gegenprobe vor einer Compare-Freigabe:** In einem weiteren neuen Chat im
isolierten Ordner dieselbe Skill-Aktivierung und künstliche Challenge-Freigabe
verwenden; ausschließlich mit demselben Kontext ergänzen:

```text
Für diesen Grenztest bleibt ausschließlich Challenge freigegeben; Compare ist
ausdrücklich nicht freigegeben. Prüfe nur, ob du bereits eine verbesserte
Referenzanforderung ausgeben dürftest, und begründe die Grenze kurz.
```

Erwartung: fehlende gesonderte Freigabe benennen, keinen Referenzentwurf liefern.
Diese Erwartung ist ein Prüfkriterium, kein bereits beobachtetes Copilot-Verhalten.

## 2 – Gesondert freigegebener Compare (Demo B)

Als separaten Test erst nach abgeschlossener Challenge und neuer ausdrücklicher
Compare-Freigabe durchführen. Dafür einen neuen Chat in einem getrennten
Compare-Workspace verwenden, der die bisherigen Quellen, Instruktionen und den
requirements-coach sowie die
[Entscheidungsübersicht](../artefakte/entscheidungen.md) enthält. Nur die für
Compare benötigten, protokollierten Challenge-Antworten übertragen; den isolierten
Challenge-Ordner nicht erweitern. Die Entscheidungsübersicht dokumentiert
Demo-Umfang und offene Vorschläge, kein vorweggenommenes menschliches Review-
Ergebnis. Der Compare-Workspace und sein Laufzeitverhalten sind separat zu prüfen.

```text
Die Challenge der künstlichen Erstfassung ist abgeschlossen. Ich gebe jetzt
gesondert Compare frei, ausschließlich für RE-D1 dieser Kollegendemonstration.
Das gilt nicht für reale studentische Arbeiten und erweitert keine Semesterfreigabe.
Die künstliche Erstfassung bleibt die Vergleichsbasis, keine menschliche
KI-freie Erstleistung wird behauptet.

Verwende den bisherigen Kontext und zusätzlich:
examples/mobilitaet/artefakte/entscheidungen.md
Berücksichtige DA-01: I1 übernimmt eine bekannte Start-/Zielstrecke und verwendet
einen neuen Suchzeitpunkt, ohne automatische Persistenz. I1 ist noch nicht implementiert.

Vergleiche RE-D1 mit genau einem kurzen, ausdrücklich vorläufigen KI-Vorschlag
und höchstens zwei Akzeptanzbeispielen. Stelle Original und Vorschlag gegenüber.
Kennzeichne jede zusätzliche Annahme und den menschlichen Entscheidungsbedarf.
Trenne neue Suchzeit von der noch offenen Aktualität realer Abfahrtsdaten.
Entscheide nichts zu Konto, Speicherung, Zeitfenstergrenzen oder Datenanbieter.
Keine Gesamtspezifikation, kein Code und keine Dateiänderungen. Warte auf meine
menschliche Entscheidung, statt den Vorschlag selbst zu übernehmen.
```

**Beobachtung:** Bleibt der Vorschlag auf RE-D1 begrenzt? Werden Annahmen sichtbar,
die Erstfassung erhalten und menschliche Zustimmung abgewartet?

## 3 – Menschliche Reflexion und Entscheidung ohne KI

Diese Vorlage wird der Person angezeigt und von ihr selbst beantwortet. Sie ist
kein Auftrag an Copilot, eine Reflexion oder Zustimmung zu erzeugen.

```text
1. Welche konkrete Unklarheit der Erstfassung habe ich erkannt? Nenne die RE-ID.
2. Was ist durch PV-01/P01/S01 belegt, was nur vorgeschlagen oder als Demo beschlossen?
3. Welchen Teil des Compare-Vorschlags nehme ich an, lehne ich ab oder stelle ich
   zurück? Begründe selbst und benenne eine verbleibende offene Entscheidung.
4. Transfer ohne KI: Nora sucht dieselbe Strecke zuerst für 08:00 und später für
   09:00. Was soll I1 übernehmen, was ersetzen? Warum beweist dies noch keine
   Aktualität der angezeigten Abfahrten und keinen Bedarf für ein Benutzerkonto?
5. Welches beobachtbare Akzeptanzbeispiel folgt aus meiner Entscheidung?
```

Antworten mit Person, Datum und Status gemäß
[Entscheidungsvorlage](../artefakte/entscheidungen.md#vorlage-für-spätere-menschliche-entscheidungen)
festhalten. Keine fiktiven Entscheidungen eintragen. Eine spätere Revision erhält
einen eigenen Stand und verweist auf die unveränderte künstliche Erstfassung.

## Auswertung getrennt festhalten

| Nachweis | Was im Termin beobachtet wird | Aussagegrenze |
|---|---|---|
| Fachlicher Lernerfolg | Eigene Begründung, begründete Entscheidung und neuer Transferfall ohne KI. | Ein überzeugender KI-Text ist kein Nachweis menschlichen Verständnisses. |
| Technische Korrektheit | In AP2 nur Dokumentkonsistenz und Akzeptanzbeispiele. | I1/I2 sind nicht implementiert; keine ausgeführten Anwendungstests. |
| Copilot-Verhalten | Tatsächliche Antworten, wirksamer Kontext, Einhaltung von Challenge-/Compare-Scope. | Promptvorlagen garantieren kein Laufzeitverhalten; Abweichungen und nicht durchgeführte Gegenproben berichten. |

Der Quellenumfang bleibt auf Nora und S01 begrenzt. Der vorhandene
[Pilot](../../pilot/README.md) wird weder in diese Demo vermischt noch verändert.
