number = 600851475143
z = 0
for i in range(2, number):
    if number%i == 0:
        mus=i
        if mus%2 == 0:
            print("")
        elif mus%3 == 0:
            print("")
        elif mus%5 == 0:
            print("")
        elif mus%7 == 0:
            print("")
        elif mus>z:
            z = mus
print(z)