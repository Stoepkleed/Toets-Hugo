import math

def omtrek_cirkel(straal):
    if straal < 0:
        return 0
    return 2 * math.pi * straal

def oppervlakte_rechthoek(lengte, breedte):
    if lengte < 0 or breedte < 0:
        return 0
    return lengte * breedte

def pyhagoras (a, b):
    return math.sqrt (a**2 + b**2)

def gemiddelde (getallen):
    if getallen != type(list):
        return 0
    return sum(getallen) / len(getallen)

if__name__ == ("__main__") :
    print(f" Start test {__file__}")
    assert math.isclose(omtrek_cirkel(1), 2 * math.pi)
    assert omtrek_cirkel(-1) == 0
    assert oppervlakte_rechthoek(3, 4) == 12
    assert oppervlakte_rechthoek(-3, 4) == 0
    assert math.isclose(pythagoras(3, 4), 5)
    assert gemiddelde([1, 2, 3, 4, 5]) == 3
    assert gemiddelde([]) == 0
    assert gemiddelde("niet een lijst") == 0

    print("Alle tests geslaagd!")
