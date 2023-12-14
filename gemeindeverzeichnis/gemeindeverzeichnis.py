import os

from gemeindeverzeichnis.GV100ADParser import GV100ADParser

def load_gemeindeverzeichnis(filename: str | None=None, ignore_redundant_gemeindeverbaende=True):
    if filename is None:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "GV100AD_301123.txt")

    reader = GV100ADParser(filename, ignore_redundant_gemeindeverbaende)

    return reader.read()

