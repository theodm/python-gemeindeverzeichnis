from __future__ import annotations
from datetime import date

class RSObject(object):
    # 8-stelliger Schlüssel zur eindeutigen Identifizierung einer Gemeinde mit den Bestandteilen:
    # Bundesland (2 Stellen), Regierungsbezirk (1 Stelle), Kreis (2 Stellen) und Gemeinde (3 Stellen).
    # https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Glossar/amtlicher-gemeindeschluessel.html
    ags: str

    # Regionalschlüssel: 12-stelliger Schlüssel zur eindeutigen Identifizierung
    # einer Gemeinde mit den Bestandteilen: Bundesland (2 Stellen),
    # Regierungsbezirk (1 Stelle), Kreis (2 Stellen), Gemeindeverband (4 Stellen) und Gemeinde (3 Stellen).
    # https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Glossar/regionalschluessel.html
    rs: str

    # Gebietsstand: Datum, zu dem die Gemeinde in der angegebenen Abgrenzung gültig ist.
    gebietsstand: date

    parent: RSObject | None
    children: list[RSObject]

    def __init__(self, ags=None, rs=None, gebietsstand=None):
        self.ags = ags
        self.rs = rs
        self.gebietsstand = gebietsstand

        self.parent = None
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self

    def remove_child(self, obj):
        self.children.remove(obj)
        obj.parent = None