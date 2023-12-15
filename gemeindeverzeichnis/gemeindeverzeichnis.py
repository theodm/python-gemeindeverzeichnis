import os

from gemeindeverzeichnis.GV100ADParser import GV100ADParser

def load_gemeindeverzeichnis(filename: str | None=None, ignore_redundant_gemeindeverbaende=True):
    """
    Lädt das Gemeindeverzeichnis

    Args:
        filename: Dateiname der GV100AD-Datendatei, die für das Einlesen verwendet werden soll.
        ignore_redundant_gemeindeverbaende: Gibt an, ob Gemeindeverbände die selbst nur aus einer Gemeinde bestehen, ignoriert und damit herausgefiltert werden.

    Returns:
        Gibt ein Dictionary zurück, welches die Regionalschlüssel der Regionaleinheiten auf das gesamte Regionaleinheiten-Objekt
        RSObject und entsprechende Subklassen (Land, Kreis, Gemeinde, Gemindeverband, Regierungsbezirk, Region) abbildet.

        z.B.:
        {
            "01": Land(<Schleswig-Holstein>),
            "01001": Kreis(<Flensburg, Stadt>),
            "010010000000": Gemeinde(<Flensburg, Stadt>),
            ...
        }

    """
    if filename is None:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "GV100AD_301123.txt")

    reader = GV100ADParser(filename, ignore_redundant_gemeindeverbaende)

    return reader.read()

