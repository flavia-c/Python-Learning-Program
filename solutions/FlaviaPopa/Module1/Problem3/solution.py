a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

nr = int(input("Add a number: "))
for el in a:
    if el < nr:
        x.append(el)

print("Elements less than %s are: " % nr)
print(x)