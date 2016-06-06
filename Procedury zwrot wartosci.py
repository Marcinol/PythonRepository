def pobierzLiczbe(zmienna):
    while True:
        x = input("podaj " + "liczbe " + zmienna)
        try:
            x = int(x)
            break
        except:
            print("podaj prawidłowa liczbe")
    return x


print('iloczyn to: ', pobierzLiczbe("x") * pobierzLiczbe("y"))
