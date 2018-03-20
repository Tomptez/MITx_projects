print("Please think of a number between 0 and 100!")

guess = 0
low = 0
high = 100

while True:
    guess = int((low + high)/2)
    print("Is your secret number", guess,"?")
    ipt=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ipt == 'c':
        print("Expected: Game over. Your secret number was:", guess)
        break
    elif ipt == 'l':
        low = guess
    elif ipt == 'h':
        high = guess
    else:
        print("your input was not correct. Please try it again")
