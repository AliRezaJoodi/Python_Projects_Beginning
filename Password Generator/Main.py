# My GitHub:  		GitHub.com/AliRezaJoodi

from Password_Generator import password_generator_V10
from Password_Generator import password_generator_V20

def main():
    password_length = int(input("Enter a Length of the Password: "))
    
    password = password_generator_V10(password_length)
    print("Generated Password:   ", password)
    
    password = password_generator_V20(password_length, number=True, alphabet=True, special=True)
    print("Generated Password:   ", password)

if __name__ == "__main__":
    main()