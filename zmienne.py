x = 3
y = "zmienna"

print("na poczatku wartoscia x i y bylo")
print(x)
print(y)

x = x + 2
y = "szkola"

print("po zmianie wartosci sa nastepujace:")

print(x)
print(y)

#tablica
tablica = ["jeden", 'dwa', "trzy", "trzy", "trzy"]
# nie mozna nic zmienic w tablicy tupel
tupel = (1, "dwa", 3)

print(tablica)
print(tupel)
#wydrukuje elemnet bez powturzen
zz = set("aabbcdeeee")
print(zz)
#wydrukuje elementy z tablicy bezpowturzen
ze = set(tablica)
print (ze)

#dictionary

d= {"Audi":25, "honda":45, "mazda":12}
print(d["Audi"])
print(d)
#wydrukuje wszystkie wartosci z dictionary
print(d.values())
#wydrukuje wszystkie elementy z dictionary
print(d.items())

#wartosci boolen musza byc pisane z Duzej Liter
p = True
f = False
n = None
