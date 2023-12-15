from gemeindeverzeichnis.enums.bundesland import Bundesland
from gemeindeverzeichnis.gemeindeverzeichnis import load_gemeindeverzeichnis

def test_load_gemeindeverzeichnis():
    gemeindeverzeichnis = load_gemeindeverzeichnis()

    assert "064140000000" in gemeindeverzeichnis
    assert len(gemeindeverzeichnis) == 11307

def test_bundesland():
    gemeindeverzeichnis = load_gemeindeverzeichnis()

    gemeindeverzeichnis_hessen = {k: v for k, v in gemeindeverzeichnis.items() if v.bundesland == Bundesland.HE}

    assert len(gemeindeverzeichnis_hessen) == 455