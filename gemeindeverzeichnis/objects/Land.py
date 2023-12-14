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
