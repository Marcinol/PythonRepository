
user = input("Podaj swoje imie")
# wykonuje sie w niskonczonosc lub napotka break
while True:
    # w inpucie moga wystepowac tylko stringi
    x = input(user + " podaj liczbe by pomnorzyc ja przez 2 ")
    # sprobuj wydrukowac x*2
    try:
        x= int(x)
        print(x * 2)
        # przerwie tylko jesli wykona sie funkcjia
        break
    # jesli sie nie uda to informuje o bledzie
    except:
        print("Nie podales liczby")
