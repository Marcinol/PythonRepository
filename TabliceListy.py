import random
random.seed()

aTablica = ["spoleczenstwo obywatelskie", "Edukacjia", "Sluzba zdrowia", "nasza partia",

            "partia rzadzaca", "wojsko", "unia europejska", "opozycjia", "zwiazek zawodowy"]
bTablica = ["utrudnia", "ulatwia", "umozliwia", "uniemozliwia"]

cTablica = ["przeprowadzenie reform", "budowe nowych drog", "wzmocnienie Polski na arenie miedzynarodowej",
            "rozwoj gospodarki", "wprowadzenie euro w polsce"]

#random.randint losuje randomowego int od a do b
#indexy beda losowymi liczbami od 0 do liczby elementow w tablicy - 1
aindex = random.randint(0, len(aTablica)-1)
bindex = random.randint(0, len(bTablica)-1)
cindex = random.randint(0, len(cTablica)-1)

print (aTablica[aindex], bTablica[bindex], cTablica[cindex])