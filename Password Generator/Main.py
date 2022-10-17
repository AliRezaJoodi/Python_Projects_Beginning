# My GitHub:  		GitHub.com/AliRezaJoodi

from display import *
from display import LENGHT_TITLE as LENGHT
from password_generator import *

def main():
    length = int(input("Enter a Length:".ljust(LENGHT+2, " ")))
    
    password_V10 = generate_V10(length)
    password_V20 = generate_V20(length, number=True, alphabet=True, special=True)
    
    display ("Generated Password V10:", password_V10)
    display ("Generated Password V20:", password_V20)

if __name__ == "__main__":
    main()