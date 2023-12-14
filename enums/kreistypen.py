
Kreis_KreisfreieStadt = 41
Kreis_Stadtkreis = 42
Kreis = 43
Landkreis = 44
Regionalverband = 45

_kreistypen = {
    41: u'Kreisfreie Stadt',
    42: u'Stadtkreis',
    43: u'Kreis',
    44: u'Landkreis',
    45: u'Regionalverband',
}

def kreistyp_string(typ: int) -> str | None:
    if typ in _kreistypen:
        return _kreistypen[typ]

    return None
