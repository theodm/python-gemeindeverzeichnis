

VerbandsfreieGemeinde = 50
Amt = 51
Samtgemeinde = 52
Verbandsgemeinde = 53
Verwaltungsgemeinschaft = 54
Kirchspielslandgemeinde = 55
Verwaltungsverband = 56
VGTraegermodell = 57
ErfuellendeGemeinde = 68


_verbandtypen = {
    50: u'Verbandsfreie Gemeinde',
    51: u'Amt',
    52: u'Samtgemeinde',
    53: u'Verbandsgemeinde',
    54: u'Verwaltungsgemeinschaft',
    55: u'Kirchspielslandgemeinde',
    56: u'Verwaltungsverband',
    57: u'VG Trägermodell',
    58: u'Erfüllende Gemeinde',
}


def verbandstyp_string(typ: int) -> str | None:
    if typ in _verbandtypen:
        return _verbandtypen[typ]

    return None