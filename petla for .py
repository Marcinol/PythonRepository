

for i in [2, 4, 5, 7, 3, 9]:
    print(i, "do kwadratu")
    print ("to:", i*i)

#od 1 do 5 ale bez 5
for i in range(1, 5):
    print(i, "do kwadratu")
    print ("to:", i*i)

for i in range(1, 10):
    if i == 5:
        print("nie lubie tej", i)
        #wraca na gore petli
        continue
    if i == 7:
        print(i, "jeszcze bardziej")
        #konczy petle mimo ze nie wykonala wszystkich obliczen
        break
    print("obecna liczba to", i)
    print(i*i)
print("to na tyle")