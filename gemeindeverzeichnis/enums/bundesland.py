from enum import Enum

class Bundesland(Enum):
    SH = "Schleswig-Holstein"
    HH = "Hamburg"
    NI = "Niedersachsen"
    HB = "Bremen"
    NW = "Nordrhein-Westfalen"
    HE = "Hessen"
    RP = "Rheinland-Pfalz"
    BW = "Baden-Württemberg"
    BY = "Bayern"
    SL = "Saarland"
    BE = "Berlin"
    BB = "Brandenburg"
    MV = "Mecklenburg-Vorpommern"
    SN = "Sachsen"
    ST = "Sachsen-Anhalt"
    TH = "Thüringen"

    @staticmethod
    def from_ags_or_rgs(ags_or_rgs: str):
        pref = ags_or_rgs[0:2]

        if pref == "01":
            return Bundesland.SH
        elif pref == "02":
            return Bundesland.HH
        elif pref == "03":
            return Bundesland.NI
        elif pref == "04":
            return Bundesland.HB
        elif pref == "05":
            return Bundesland.NW
        elif pref == "06":
            return Bundesland.HE
        elif pref == "07":
            return Bundesland.RP
        elif pref == "08":
            return Bundesland.BW
        elif pref == "09":
            return Bundesland.BY
        elif pref == "10":
            return Bundesland.SL
        elif pref == "11":
            return Bundesland.BE
        elif pref == "12":
            return Bundesland.BB
        elif pref == "13":
            return Bundesland.MV
        elif pref == "14":
            return Bundesland.SN
        elif pref == "15":
            return Bundesland.ST
        elif pref == "16":
            return Bundesland.TH
        else:
            raise ValueError("Invalid AGS or RGS: " + ags_or_rgs)


