from gemeindeverzeichnis.enums.satzarten import GEMEINDEVERBAND_LEVEL
from gemeindeverzeichnis.enums.verbandstypen import verbandstyp_string
from gemeindeverzeichnis.objects.DerivedBevoelkerungMixin import DerivedBevoelkerungMixin
from gemeindeverzeichnis.objects.RSObject import RSObject

class Gemeindeverband(RSObject, DerivedBevoelkerungMixin):
    def __init__(self, rs=None, gebietsstand=None,
                 name=None, sitz_verwaltung=None, typ=None):
        RSObject.__init__(self, None, rs, gebietsstand)
        self.name = name
        self.sitz_verwaltung = sitz_verwaltung
        self.typ = typ
        self.level = GEMEINDEVERBAND_LEVEL

    def _get_typ_string(self):
        return verbandstyp_string(self.typ)


    def __repr__(self):
        return "<Gemeindeverband: %r %r %r %r>" % (self.rs, self.name, self.sitz_verwaltung, verbandstyp_string(self.typ))

    name: str
    sitz_verwaltung: str
    typ: int
    typ_string = property(_get_typ_string)
    level: int


    # from DerivedBevoelkerungMixin:
    #
    # bevoelkerung: int
    # maennlich: int
    # weiblich: int
    #

    # from RSObject:
    #
    # rs: str
    # ags: str
    # gebietsstand: int
    # bundesland: Bundesland
    #
    # parent: RSObject | None
    # children: RSObject[]
