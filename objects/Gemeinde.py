from enums.gemeindetypen import gemeindetyp_string
from enums.satzarten import GEMEINDE_LEVEL
from objects.RSObject import RSObject

class Gemeinde(RSObject):

    def __init__(self, ags=None, rs=None, gebietsstand=None,
                 name=None, typ=None):
        RSObject.__init__(self, ags, rs, gebietsstand)

        self.name = name
        self.typ = typ
        self.bevoelkerung = 0
        self.maennlich = 0
        self.flaeche = 0
        self.level = GEMEINDE_LEVEL

    def _flaeche_in_km2(self) -> float:
        return self.flaeche / 10
    def _get_typ_string(self):
        return gemeindetyp_string(self.typ)


    def _get_weiblich(self):
        return self.bevoelkerung - self.maennlich


    def __repr__(self):
        return "<Gemeinde: %r %r %r %r %r %r >" % (self.rs, self.ags, self.name, gemeindetyp_string(self.typ), self.flaeche, self.bevoelkerung)


    name: str

    typ: int
    typ_string = property(_get_typ_string)

    bevoelkerung: int
    maennlich: int
    weiblich = property(_get_weiblich)

    # Fläche in km² * 10
    flaeche: int
    flaeche_in_km2 = property(_flaeche_in_km2)

    finanzamtsbezirk: int | None
    oberlandesgerichtsbezirk: str
    landgerichtsbezirk: int | None
    amtsgerichtsbezirk: int | None
    arbeitsamtsbezirk: int | None

    plz: str
    plzeindeutig: bool

    bundestagswahlkreis: tuple[int | None, int | None]



