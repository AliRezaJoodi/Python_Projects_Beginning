# My GitHub:  		GitHub.com/AliRezaJoodi

from Password_Generator import password_generator_V10
from Password_Generator import password_generator_V20
from Dispaly import dispaly

def main():
    password_length = int(input("Enter a Length of the Password: "))
    
    password_V10 = password_generator_V10(password_length)
    password_V20 = password_generator_V20(password_length, number=True, alphabet=True, special=True)
    
    print("\n")
    dispaly ("Generated Password:", password_V10)
    dispaly ("Generated Password:", password_V20)

if __name__ == "__main__":
    main()