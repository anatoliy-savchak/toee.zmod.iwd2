def get_difficulty():
    # 1 - easy. Vanilla everything except spells.
    # 2 - improved. Vanilla class. 
    # 3 - hard. HoF 1
    # 4 - very hard. HoF 2
    return 2


def get_iwd2_difficulty():
    d = get_difficulty()
    if d == 3: # hard. HoF 1
        return 2 # HoF 1
    elif d >= 4: # very hard. HoF 2
        return 3 # HoF 2
    return 1 # 1 - no HoF, 2 - HoF, 3 - HoF HARD

