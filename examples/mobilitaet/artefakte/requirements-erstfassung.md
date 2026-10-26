# Künstliche Requirements-Erstfassung – Nora

**Status:** Künstliche, bewusst unvollständige Erstfassung für die Kollegendemonstration.
Im Engineering-Auftrag mit KI erstellt; keine reale studentische Eigenleistung,
keine ohne KI erbrachte Erstleistung und keine beschlossene Produktspezifikation.
Im Demoablauf steht sie stellvertretend für eine vor einem Review vorliegende
eigene Erstfassung. Sie bleibt als Vergleichsbasis unverändert erhalten.

**Quellen:** [PV-01](../../../docs/product/vision.md),
[P01](../../../docs/personas/P01-junge-pendlerin.md),
[S01](../../../docs/scenarios/S01-taegliche-fahrt.md).
Die Quellen motivieren die folgenden Aussagen, legen aber deren Umsetzung nicht fest.

| ID | Künstliche Anforderung im Entwurfsstand | Fachlicher Anknüpfungspunkt |
|---|---|---|
| RE-D1 | Nora soll eine bekannte Start-/Zielstrecke bei einer weiteren Suche wiederverwenden können, ohne die Haltestellen erneut einzugeben. | P01: wiederholte Eingaben vermeiden; S01: bekannte Strecke erneut aufrufen. |
| RE-D2 | Bei einer erneuten Suche sollen aktuelle Abfahrtsdaten passend zur gewünschten Fahrt angezeigt werden. | P01: alte Ergebnisse nicht mit aktuellen Abfahrten verwechseln; S01: aktuelle Abfahrten für diesen Morgen. |
| RE-D3 | Nora soll schnell erkennen, welche Verbindungen sie rechtzeitig zur Hochschule bringen. | P01: rechtzeitig ankommen, verständliche Bedienung; S01: frühere Vorlesung. |

Die Erstfassung enthält absichtlich noch keine vollständigen Akzeptanzkriterien.
Nicht ausformulierte Details sind offen und dürfen beim Review nicht stillschweigend
ergänzt werden. Anforderungen an Konto, Speicherung, Datenanbieter und Ticketkauf
werden hier nicht festgelegt. Der Kauf bleibt Teil des Quellkontexts, liegt jedoch
außerhalb der geplanten ersten Inkremente I1/I2.

Challenge, Compare-Vorschlag und menschliche Revision werden getrennt von dieser
Erstfassung behandelt. Siehe [Demoablauf](../demo/requirements.md) und
[Entscheidungsübersicht](entscheidungen.md).
