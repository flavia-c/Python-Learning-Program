s = input("Give me a string: ")

print("s = ", s)
p = s[-1:0:-1] + s[0]
print("p = ", p)
if s == p:
    print("String is a palindrome!")
else:
    print("String is NOT a palindrome")