from __future__ import annotations
from datetime import date

from gemeindeverzeichnis.enums.bundesland import Bundesland

class RSObject(object):
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

    def _get_bundesland(self):
        return Bundesland.from_ags_or_rgs(self.rs)


    # 8-stelliger Schlüssel zur eindeutigen Identifizierung einer Gemeinde mit den Bestandteilen:
    #
    #  - Bundesland (2 Stellen)
    #  - Regierungsbezirk (1 Stelle)
    #  - Kreis (2 Stellen)
    #  - Gemeinde (3 Stellen)
    #
    # https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Glossar/amtlicher-gemeindeschluessel.html
    ags: str

    # Regionalschlüssel: 12-stelliger Schlüssel zur eindeutigen Identifizierung
    # einer Gemeinde mit den Bestandteilen:
    #
    #  - Bundesland (2 Stellen)
    #  - Regierungsbezirk (1 Stelle)
    #  - Kreis (2 Stellen)
    #  - Gemeindeverband (4 Stellen)
    #  - Gemeinde (3 Stellen)
    #
    # https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Glossar/regionalschluessel.html
    rs: str

    # Gebietsstand: Stand des Datensatzes.
    gebietsstand: date

    # Bundesland: Bundesland, in dem das Gebiet liegt.
    bundesland: Bundesland = property(_get_bundesland)

    parent: RSObject | None
    children: list[RSObject]