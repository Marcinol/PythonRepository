import random
random.seed()
#numer indexu panstwa musi byc taki sam jak numer indexu stolicy
panstwa = ['Niemcy', 'Białorus', 'Litwa', 'Estonia', 'USA', 'Chiny', 'Australia', 'Hiszpania', 'Portugalia', 'Austria',
           "Bangladesz", "Belgia", "Bośnia i Hercegowina", "Bułgaria", "Chorwacja", "Czechy", "Dania", "Egipt",
           "Finlandia", "Francja", "Grecja", "Holandia", "Irlandia", "Japonia", "Kanada", "Korea Południowa", "Kuba",
           "Kuwejt", "Liban", "Łotwa", "Macedonia", "Meksyk", "Monako", "Norwegia", "Panama", "Peru", "Rumunia",
           "Senegal", "Serbia", "Singapur", "Słowacja", "Syria", "Szwajcaria", "Szwecja", "Tajlandia", "Tunezja",
           "Turcja", "Ukraina", "Watykan", "Węgry", "Wielka Brytania", "Włochy"]

stolice = ['Berlin', 'Minsk', 'Wilno', 'Tallinn', 'Waszyngton', 'Pekin', 'Canberra', 'Madryt', 'Lizbona', 'Wieden',
           "Dhaka", "Bruksela", "Sarajewo", "Sofia", "Zagrzeb", "Praga", "Kopenhaga", "Kair", "Helsinki", "Paryz",
           "Ateny", "Amsterdam", "Dublin", "Tokio", "Ottawa", "Seul", "Hawana", "Kuwejt", "Bejrut", "Ryga", "Skopje",
           "Meksyk", "Monako", "Oslo", "Panama", "Lima", "Bukareszt", "Dakar", "Belgrad", "Singapur", "Bratyslawa",
           "Damaszek", "Berno", "Sztokholm", "Bangkok", "Tunis", "Ankara", "Kijow", "Watykan", "Budapeszt", "Londyn",
           "Rzym"]

iloscPunktow = 0
liczbaPytan = 10

def odmianaPunkt(iloscPunktow):  # odmienia przez przypadki slowo punkt
    odmienPunkt = "punkty"
    if iloscPunktow < - 4 or iloscPunktow > 4 or iloscPunktow == 0:
        odmienPunkt = "punktów"
    if iloscPunktow == 1 or iloscPunktow == - 1:
        odmienPunkt = "punkt"
    if iloscPunktow == -2 or iloscPunktow == -3 or iloscPunktow == -4:
        odmienPunkt = "punkty"
    if iloscPunktow == 2 or iloscPunktow == 3 or iloscPunktow == 4:
        odmienPunkt = "punkty"
    return odmienPunkt

for numerPytania in range(1, liczbaPytan + 1):  # dla liczby pytan od 1 do liczby pytan

    print("Pytanie", numerPytania, "/", liczbaPytan)
    index = random.randint(0, len(panstwa) - 1)  # randomowy numer indexu z tablicy panstwa
    iloscPierwszychLiter = 1  # bedzie pokazywac pierwsze litery stolicy
    pierwszeLitery = stolice[index][:iloscPierwszychLiter]

    for iloscPowtorzen in range(1, 4):  # max liczba nie poprawnych odpowiedzi to 3

        pierwszeLitery = stolice[index][:iloscPierwszychLiter]
        guess = input("Podaj stolice państwa " + panstwa[
            index] + ":" + "\n" + pierwszeLitery)  # dokoncz nazwe stolicy wyswietlonego panstwa

        if guess == stolice[index][iloscPierwszychLiter:]:  # jesli zgadles nazwe stolice

            iloscPunktow = iloscPunktow + 4 - iloscPowtorzen  # max liczba punktow za 1 zadanie to 3 za pierwszym razem

            print("Brawo masz", iloscPunktow,
                  odmianaPunkt(iloscPunktow))  # odmienia przez przypadki slowo punkt w zalerznosci od ilosci punktow
            break

        else:  # jesli nie zgadles nazwy stolicy
            iloscPunktow -= 1
            iloscPierwszychLiter += 1
            if iloscPowtorzen < 3:
                print("jeszcze raz masz", iloscPunktow, odmianaPunkt(iloscPunktow))

            if iloscPowtorzen == 3:
                print("prawidlowa odpowiedz to", stolice[index], "masz", iloscPunktow, odmianaPunkt(iloscPunktow))
