import random



random.seed()

#na poczatku prawda jest ze niezgadl
niezgadl = True
zgadni = random.randint(1,100)

#bedzie sie zwiekszac za kazdym razem gdy uruchomi sie jakas petla if
kroki = 0

bliskoMalo = zgadni - 10
bliskoDuzo = zgadni + 10

print("Zgadni jaka liczba z przedzialu 1 do 100 mam w pamieci masz max 10 szans")

#jezeli prawda jest ze niezgdal wykonuj kod ponirzej
while niezgadl == True:
    try:
        liczba = int(input())

    #w razie znaku innego jak int wypisuje by podac nowa liczbe
    except ValueError:
        print("podaj liczbe od 1 do 100")
        continue
        #niezgadl = True

    if liczba < zgadni:
        print(liczba,"to za malo")
        niezgadl = True
        kroki = kroki + 1
        #jezeli zgadni - 10 < od moja liczba napisz ze jestem blisko
        if bliskoMalo < liczba:
            print("ale jests blisko")
            continue
            # niezgadl = True

    if liczba > zgadni:
         print(liczba, "to za duzo")
         kroki = kroki + 1
         #jezeli zgadni + 10 > od moja liczba napisz ze jestem blisko
         if bliskoDuzo > liczba:
             print("ale jests blisko")
             continue
             #niezgadl = True

    if liczba == zgadni:
        kroki = kroki + 1
        print("Brawo moja liczba to", zgadni, "zgadles ja za",
              kroki,"razem")
        niezgadl = False

    if kroki < 3 and niezgadl == False:
        print("WOOOOOOOOOW  !!! LUCKY YOU !!!")
        break

    if kroki < 6 and niezgadl == False:
        print("WOW!!! Niezle Ci poszło dobry wynik")
        break

    if kroki == 10:
        print("Masz dziś pecha wykorzystałeś swoje 10 szans,"
              " może następnym razem pujdzie Ci lepiej")
        break