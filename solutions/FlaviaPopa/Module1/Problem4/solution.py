nr = int(input("Add a number: "))
d = []

for i in range(1, (nr + 1)):
    if nr % i == 0:
        d.append(i)

print("Divisors are: ")
print(d)