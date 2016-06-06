x = input()
x = int(x)
#lub x = int(input())
i = 1
print(x, "dzieli sie bez reszty przez :")
while i <= x / 2:

    if x % i == 0:
        print(i)
    i += 1
# i+=1 musi byc na wysokosci if'a
print(x)