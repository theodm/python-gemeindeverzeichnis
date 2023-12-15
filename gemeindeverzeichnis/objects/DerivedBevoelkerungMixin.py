from functools import reduce

class DerivedBevoelkerungMixin(object):
    def _get_bevoelkerung(self):
        return reduce(lambda i, x: i + x, [a.bevoelkerung for a in self.children])

    def _get_maennlich(self):
        return reduce(lambda i, x: i + x, [a.maennlich for a in self.children])

    def _get_weiblich(self):
        return reduce(lambda i, x: i + x, [a.weiblich for a in self.children])

    bevoelkerung = property(_get_bevoelkerung)
    maennlich = property(_get_maennlich)
    weiblich = property(_get_weiblich)