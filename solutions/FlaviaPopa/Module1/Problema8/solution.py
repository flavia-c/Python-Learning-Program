p1 = str(input("Player 1 - Choose one: rock, scissors, paper: "))
p2 = str(input("Player 2 - Choose one: rock, scissors, paper: "))
options = ['rock', 'scissors', 'paper']
sw1 = 0
sw2 = 0

for el in options:
    if p1 == el:
        sw1 = 1
    if p2 == el:
        sw2 = 1
if sw1 == 0 or sw2 == 0:
    print("Invalid input! Please try again.")

while(sw1!=0 and sw2!=0):
    if p1 == p2:
        print("It's a tie!")
        break
    elif p1 == 'rock':
        if p2 == 'scissors':
            print("Player 1 wins!")
            break
        else:
            print("Player 2 wins!")
            break
    elif p1 == 'scissors':
        if p2 == 'paper':
            print('Player 1 wins!')
            break
        else:
            print("Player 2 wins!")
            break
    elif p1 == 'paper':
        if p2 == 'rock':
            print("Player 1 wins!")
            break
        else:
            print("Player 2 wins!")
            break


