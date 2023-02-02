

def find_m(sp):
    w = sp[0][0] - sp[1][0]
    h = sp[0][1] - sp[1][1]
    return abs(w), abs(h)
