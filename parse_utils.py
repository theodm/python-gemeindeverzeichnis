

def int_or_none(s: str) -> int | None:
    if s.strip() == '':
        return None

    return int(s)