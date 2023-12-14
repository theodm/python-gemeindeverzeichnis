from enums.kreistypen import kreistyp_string
from enums.satzarten import KREIS_LEVEL
from objects.DerivedBevoelkerungMixin import DerivedBevoelkerungMixin
from objects.RSObject import RSObject


class Kreis(RSObject, DerivedBevoelkerungMixin):
    def __init__(self, rs=None, gebietsstand=None,
                 name=None, sitz_verwaltung=None, typ=None):
        RSObject.__init__(self, rs, rs, gebietsstand)
        self.name = name
        self.sitz_verwaltung = sitz_verwaltung
        self.typ = typ
        self.level = KREIS_LEVEL

    def _get_typ_string(self):
        return kreistyp_string(self.typ)

    typ_string = property(_get_typ_string)

    def __repr__(self):
        return "<Kreis: %r %r %r %r>" % (self.rs, self.name, self.sitz_verwaltung, kreistyp_string(self.typ))
