# GitHub.com/AliRezaJoodi

from Password_Generator import password_generator_V10
from Password_Generator import password_generator_V20

def main():
    password_length = int(input("Enter a Length of the Password: "))
    
    password = password_generator_V10(password_length)
    print("Generated Password V10:", password)
    
    password = password_generator_V20(password_length, number=True, alphabet=True, special=True)
    print("Generated Password V20:", password)

if __name__ == "__main__":
    main()