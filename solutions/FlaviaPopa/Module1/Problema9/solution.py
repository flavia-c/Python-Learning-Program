import random
nr = 0

try:
    b = int(input("Guess the number: "))
    a = random.randint(1, 9)
    print("Random generated number: ", a)
    while (b != 'exit'):
        if int(b) == a:
            nr += 1
            print("Your guess is right!")
            break
        elif int(b) > a:
            nr += 1
            print("Too high!")
            try:
                b = int(input("Guess again: "))
            except ValueError:
                print("Invalid input. Please input a number!")
                break
        else:
            nr += 1
            print("Too low!")
            try:
                b = int(input("Guess again: "))
            except ValueError:
                print("Invalid input. Please type a number!")
                break
except ValueError:
    nr += 1
    print("Invalid input. Please input a number!")

print("Total number of guesses: ", nr)

