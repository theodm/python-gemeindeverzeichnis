
Markt = 60
Gemeinde_KreisfreieStadt = 61
Gemeinde_Stadtkreis = 62
Stadt = 63
KreisangehoerigeGemeinde = 64
GemeindefreiesGebietBewohnt = 65
GemeindefreiesGebietUnbewohnt = 66
GrosseKreisstadt = 67
AmtsangehoerigeGemeinde = 68
AmtsfreieGemeinde = 69

_gemeindetypen = {
    60: u'Markt',
    61: u'Kreisfreie Stadt',
    62: u'Stadtkreis',
    63: u'Stadt',
    64: u'Kreisangehörige Gemeinde',
    65: u'gemeindefreies Gebiet, bewohnt',
    66: u'gemeindefreies Gebiet, unbewohnt',
    67: u'große Kreisstadt',
    68: u'Amtsangehörige Gemeinde',
    69: u'Amtsfreie Gemeinde',
}

def gemeindetyp_string(typ: int) -> str | None:
    if typ in _gemeindetypen:
        return _gemeindetypen[typ]

    return None
