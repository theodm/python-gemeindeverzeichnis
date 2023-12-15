from gemeindeverzeichnis.enums.satzarten import REGION_LEVEL
from gemeindeverzeichnis.objects.DerivedBevoelkerungMixin import DerivedBevoelkerungMixin
from gemeindeverzeichnis.objects.RSObject import RSObject


class Region(RSObject, DerivedBevoelkerungMixin):
    def __init__(self, rs=None, gebietsstand=None,
                 name=None, sitz_verwaltung=None):
        RSObject.__init__(self, rs, rs, gebietsstand)

        self.name = name
        self.sitz_verwaltung = sitz_verwaltung
        self.level = REGION_LEVEL

    def __repr__(self):
        return "<Region: %r %r %r>" % (self.rs, self.name, self.sitz_verwaltung)

    name: str
    sitz_verwaltung: str
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