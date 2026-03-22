import random 

def GuessTheNumber():
    num = random.randint(1,100)
    while True:
        guess = int(input("Guesse the number: "))
        if guess == num:
            print("Congrats! You've guessed the number!")
            break
        elif guess > num:
            print("Oops! Too high.")
        else:
            print("Oops! Too low.")

GuessTheNumber()