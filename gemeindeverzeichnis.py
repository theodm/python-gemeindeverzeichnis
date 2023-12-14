from GV100ADParser import GV100ADParser

def load_gemeindeverzeichnis(filename="data/GV100AD_301123.txt", ignore_redundant_gemeindeverbaende=True):
    reader = GV100ADParser(filename, ignore_redundant_gemeindeverbaende)

    return reader.read()

