#!/usr/bin/env python3
"""Erzeugt einen isolierten Demo-Kontext; prüft kein Copilot-Laufzeitverhalten."""

import argparse
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
# Bewusste Positivliste: keine Verzeichnisse rekursiv kopieren.
# Der aktuelle requirements-coach hat keine erforderlichen lokalen Ressourcen.
COPIED_FILES = (
    "AGENTS.md",
    ".github/copilot-instructions.md",
    ".agents/skills/requirements-coach/SKILL.md",
    "docs/product/vision.md",
    "docs/personas/P01-junge-pendlerin.md",
    "docs/scenarios/S01-taegliche-fahrt.md",
    "examples/mobilitaet/artefakte/requirements-erstfassung.md",
)
RULES_PATH = "docs/SEMESTERREGELN.md"
DEMO_RULES = """# Semesterregeln – isolierter künstlicher Challenge-Test

Dieser Hinweis wurde für den isolierten Demo-Workspace erzeugt. Die konservative
Vorlage des Quellrepositories wurde nicht übernommen. Hier liegen keine aktuellen
Übungsblätter und keine verbindliche WS-2026/27-Semesterfreigabe vor.

Vor dem Test muss die vorführende Person im neuen Copilot-Chat ausdrücklich nur
die Requirements-Challenge der vier benannten künstlichen Demoartefakte freigeben.
Die mit KI erstellte Erstfassung vertritt allein für diese Vorführung eine eigene
Erstfassung. Dieser Dateitext und das Vorhandensein des Skills erteilen keine Freigabe.
Ohne ausdrückliche Demo-Freigabe keine konkrete Analyse beginnen.

Die Demo-Freigabe umfasst keine reale studentische Arbeit, keinen Compare,
kein UML-/Architektur-Review, keinen Code und keine Dateiänderungen.
Veröffentlichte aktuelle Kursregeln bleiben verbindlich; ungeklärte Widersprüche
sind vor dem Test zu klären. Für reale Arbeiten sind die aktuellen Übungsblätter
und phasenbezogenen Freigaben gesondert erforderlich.
"""


def prepare(output):
    """Kopiert nur freigegebene Dateien in einen neu angelegten Ausgabeordner."""
    output = output.expanduser()
    if not output.is_absolute():
        raise ValueError("Der Ausgabeordner muss als absoluter Pfad angegeben werden.")
    # Auch einen defekten Symlink niemals als freien Ausgabeordner behandeln.
    if output.exists() or output.is_symlink():
        raise ValueError("Der Ausgabeordner existiert bereits; nichts überschrieben.")
    output = output.resolve()
    if output == ROOT or ROOT in output.parents:
        raise ValueError("Der Ausgabeordner muss außerhalb des Quellrepositories liegen.")

    # Quellen vor jeder Ausgabe prüfen. Symlinks auch in Elternpfaden ablehnen.
    for relative in COPIED_FILES:
        source = ROOT / relative
        for part in (source, *source.parents):
            if part == ROOT:
                break
            if part.is_symlink():
                raise ValueError(f"Symlink als Quelle nicht erlaubt: {relative}")
        if not source.is_file():
            raise ValueError(f"Erforderliche Quelldatei fehlt: {relative}")

    # mkdir ist exklusiv: auch bei zwischenzeitlichem Anlegen nichts überschreiben.
    # Der Elternordner muss bereits existieren. Bei I/O-Fehlern bleibt eine
    # Teilausgabe zur Prüfung erhalten; ein erneuter Aufruf lehnt sie ab.
    output.mkdir()
    for relative in COPIED_FILES:
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with (ROOT / relative).open("rb") as source, target.open("xb") as destination:
            shutil.copyfileobj(source, destination)
    with (output / RULES_PATH).open("x", encoding="utf-8", newline="\n") as rules:
        rules.write(DEMO_RULES)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output", type=Path,
        help="neuer absoluter Ausgabeordner außerhalb des Repositories; Elternordner existiert",
    )
    args = parser.parse_args()
    try:
        output = prepare(args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Abbruch: {error}\n")
    print(f"Challenge-Workspace: {output}")
    print("Kopiert (relative Pfade):")
    for relative in sorted(COPIED_FILES):
        print(f"  {relative}")
    print(f"Erzeugt (keine Semesterfreigabe):\n  {RULES_PATH}")


if __name__ == "__main__":
    main()
