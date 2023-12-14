from gemeindeverzeichnis.gemeindeverzeichnis import load_gemeindeverzeichnis

def test_load_gemeindeverzeichnis():
    gemeindeverzeichnis = load_gemeindeverzeichnis()

    assert "064140000000" in gemeindeverzeichnis
