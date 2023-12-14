from datetime import date

from enums.satzarten import LAND_LEVEL, REGIERUNGSBEZIRK_LEVEL, REGION_LEVEL, KREIS_LEVEL, GEMEINDEVERBAND_LEVEL, \
    GEMEINDE_LEVEL
from objects.Gemeinde import Gemeinde
from objects.Gemeindeverband import Gemeindeverband
from objects.Kreis import Kreis
from objects.Land import Land
from objects.Regierungsbezirk import Regierungsbezirk
from objects.Region import Region
from parse_utils import int_or_none


class GV100ADParser:
    # Hier werden die bis zum aktuellen Durchführungsschritt
    # gespeicherten Datensätze abgelegt. Das ist insofern möglich,
    # als die Datei wirklich von oben nach unten durchgegangen werden kann.
    #
    # Der Index wird zwischenzeitlich benötigt, um die Parent-Child-Beziehungen
    # herzustellen.
    #
    # Key ist der Regionalschlüssel, Value ist der Datensatz vom Typ der Objekte
    # RSObject, Land, Regierungsbezirk, Region, Kreis, Gemeindeverband oder Gemeinde.
    index = {}

    # Hier werden alle Datensätze in der Reihenfolge ihres Auftretens
    # gespeichert. Wird auch zwischenzeitlich benötigt.
    list: list

    # Datei aus der gelesen wird
    filename: str
    # Gibt an, ob redundante Gemeindeverbände, solche die selbst nur
    # eine Gemeinde haben, ignoriert werden sollen.
    _ignore_redundant_gemeindeverbaende: bool

    def __init__(self, filename, ignore_redundant_gemeindeverbaende=True):
        self.filename = filename
        self._ignore_redundant_gemeindeverbaende = ignore_redundant_gemeindeverbaende

    def read(self):
        """
        Reads in the data from the file.

        Returns all entries in a dictionary indexed by the Regionalschlüssel.
        """
        self.list = []

        file = open(self.filename, 'r', encoding='utf-8')

        # Jede Zeile enthält einen Datensatz.
        for line in file:
            satzart = int(line[0:2])

            if satzart == LAND_LEVEL:
                self._handle_land(line)
            elif satzart == REGIERUNGSBEZIRK_LEVEL:
                self._handle_regierungsbezirk(line)
            elif satzart == REGION_LEVEL:
                self._handle_region(line)
            elif satzart == KREIS_LEVEL:
                self._handle_landkreis(line)
            elif satzart == GEMEINDEVERBAND_LEVEL:
                self._handle_gemeindeverband(line)
            elif satzart == GEMEINDE_LEVEL:
                self._handle_gemeinde(line)

        if self._ignore_redundant_gemeindeverbaende:
            self._remove_bogus_gv(self.index)

        # Zurücksetzen, dann kann ein erneuter
        # read() Aufruf nicht zu komischen Ergebnissen
        # führen.
        l = self.index
        self.index = None
        return l

    @staticmethod
    def _remove_bogus_gv(index: dict):
        to_remove = []

        for i in index:
            if not isinstance(index[i], Gemeindeverband):
                continue

            gv = index[i]

            if len(gv.children) == 1:
                p = gv.parent
                p.remove_child(gv)
                p.add_child(gv.children[0])
                to_remove.append(i)

        for i in to_remove:
            del index[i]

    @staticmethod
    def _parse_gebietsstand(line):
        return date(int(line[2:6]), int(line[6:8]), int(line[8:10]))

    def _handle_land(self, line):
        rs = ags = line[10:12]

        stand = GV100ADParser._parse_gebietsstand(line)
        name = line[22:72].strip()
        sl = line[72:122].strip()

        l = Land(rs=rs, name=name, gebietsstand=stand, sitz_landesregierung=sl)

        self.list.append(l)
        self.index[l.rs] = l
        pass

    def _handle_regierungsbezirk(self, line):
        stand = self._parse_gebietsstand(line)
        rs = ags = line[10:13]

        name = line[22:72].strip()
        sl = line[72:122].strip()
        rb = Regierungsbezirk(rs=rs, name=name, gebietsstand=stand, sitz_verwaltung=sl)

        parent = self.index[rb.rs[0:2]]
        parent.add_child(rb)

        self.list.append(rb)
        self.index[rb.rs] = rb
        pass

    def _handle_region(self, line):
        stand = self._parse_gebietsstand(line)
        rs = ags = line[10:14]

        name = line[22:72].strip()
        sl = line[72:122].strip()
        reg = Region(rs=rs, name=name, gebietsstand=stand, sitz_verwaltung=sl)

        parent = self.index[reg.rs[0:3]]
        parent.add_child(reg)

        self.list.append(reg)
        self.index[reg.rs] = reg

    def _handle_landkreis(self, line):
        stand = self._parse_gebietsstand(line)
        rs = ags = line[10:15]

        name = line[22:72].strip()
        sl = line[72:122].strip()
        typ = int(line[122:124]) if line[122:124].strip() != '' else None
        k = Kreis(rs=rs, name=name, gebietsstand=stand, sitz_verwaltung=sl, typ=typ)

        # Region?
        if k.rs[0:4] in self.index:
            self.index[k.rs[0:4]].add_child(k)
        # Regierunsbezirk?
        elif k.rs[0:3] in self.index:
            self.index[k.rs[0:3]].add_child(k)
        else:
            # otherwise, Land
            self.index[k.rs[0:2]].add_child(k)

        self.list.append(k)
        self.index[k.rs] = k

    def _handle_gemeindeverband(self, line):
        stand = self._parse_gebietsstand(line)
        rs = line[10:15] + line[18:22]

        name = line[22:72].strip()
        sl = line[72:122].strip()
        typ = int(line[122:124]) if line[122:124].strip() != '' else None
        gv = Gemeindeverband(rs=rs, name=name, gebietsstand=stand, sitz_verwaltung=sl, typ=typ)

        if gv.rs[0:5] in self.index:
            self.index[gv.rs[0:5]].add_child(gv)
        elif gv.rs[0:5].endswith('000'):
            self.index[gv.rs[0:2]].add_child(gv)

        self.list.append(gv)
        self.index[gv.rs] = gv

    def _handle_gemeinde(self, line):
        stand = self._parse_gebietsstand(line)
        rs = line[10:15] + line[18:22] + line[15:18]

        ags = line[10:15] + line[15:18]
        name = line[22:72].strip()
        sl = line[72:122].strip()
        typ = int(line[122:124]) if line[122:124].strip() != '' else None
        gem = Gemeinde(rs=rs, ags=ags, name=name, gebietsstand=stand, typ=typ)
        gem.bevoelkerung = int(line[139:150].strip())
        gem.maennlich = int(line[150:161].strip())
        gem.flaeche = int(line[128:139].strip())
        gem.finanzamtsbezirk = int_or_none(line[177:181])
        gem.oberlandesgerichtsbezirk = line[181:183].strip()
        gem.landgerichtsbezirk = int_or_none(line[183])
        gem.amtsgerichtsbezirk = int_or_none(line[184])
        gem.arbeitsamtsbezirk = int_or_none(line[185:190])

        gem.plz = line[165:170]
        gem.plzeindeutig = line[170:175].strip() == ''

        bwvon = int_or_none(line[190:193])
        bwbis = int_or_none(line[193:196])

        gem.bundestagswahlkreis = (bwvon, bwbis)
        self.index[gem.rs[0:9]].add_child(gem)
        self.list.append(gem)
        self.index[gem.rs] = gem
