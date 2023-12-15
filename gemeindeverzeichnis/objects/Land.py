from gemeindeverzeichnis.enums.satzarten import LAND_LEVEL
from gemeindeverzeichnis.objects.DerivedBevoelkerungMixin import DerivedBevoelkerungMixin
from gemeindeverzeichnis.objects.RSObject import RSObject


class Land(RSObject, DerivedBevoelkerungMixin):
    def __init__(self, rs=None, gebietsstand=None,
                 name=None, sitz_landesregierung=None):
        RSObject.__init__(self, rs, rs, gebietsstand)

        self.name = name
        self.sitz_landesregierung = sitz_landesregierung
        self.level = LAND_LEVEL

    def __repr__(self):
        return "<Land: %r %r %r>" % (self.rs, self.name, self.sitz_landesregierung)

    name: str
    sitz_landesregierung: str
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
