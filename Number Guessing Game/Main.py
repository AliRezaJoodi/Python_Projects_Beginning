# GitHub.com/AliRezaJoodi

import random

random_number = random.randrange(1,10)
print("What's your guess number between 1 to 10?")

def main():
    while(True):
        guessed_numbers = int(input("Please enter a number: "))
        if guessed_numbers > random_number:
            print("It was high!")
        elif guessed_numbers < random_number:
            print("It was low!")
        else:
            print("Congratulations, It was right.")
            break            

if __name__ == "__main__":
    main()