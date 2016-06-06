
x = 1

if x == 1:
    print("pierwszy x = ",x)

while x == 1:
    print("drugi x = ",x)
    x += 1

x = 1
while x < 10:
    print("ciag ",x)
    x += 1


x = 783
i = 1
print(x, "dzieli sie bez reszty przez :")
while i <= x / 2:

    if x % i == 0:
        print(i)
    i += 1
# i+=1 musi byc na wysokosci if'a
print(x)
