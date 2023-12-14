from enums.satzarten import REGIERUNGSBEZIRK_LEVEL
from objects.DerivedBevoelkerungMixin import DerivedBevoelkerungMixin
from objects.RSObject import RSObject


class Regierungsbezirk(RSObject, DerivedBevoelkerungMixin):
    def __init__(self, rs=None, gebietsstand=None,
                 name=None, sitz_verwaltung=None):
        RSObject.__init__(self, rs, rs, gebietsstand)

        self.name = name
        self.sitz_verwaltung = sitz_verwaltung
        self.level = REGIERUNGSBEZIRK_LEVEL

    def __repr__(self):
        return "<Regierungsbezirk: %r %r %r>" % (self.rs, self.name, self.sitz_verwaltung)
