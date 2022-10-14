# My GitHub:  		GitHub.com/AliRezaJoodi

from Password_Generator import password_generator_V10
from Password_Generator import password_generator_V20
from Dispaly_Debug import dispaly_debug

def main():
    password_length = int(input("Enter a Length of the Password: "))
    
    password = password_generator_V10(password_length)
    dispaly_debug ("\n")
    dispaly_debug ("Generated Password:", password)
    #print("Generated Password:   ", password)
    
    password = password_generator_V20(password_length, number=True, alphabet=True, special=True)
    dispaly_debug ("\n")
    dispaly_debug ("Generated Password:", password)
    #print("Generated Password:   ", password)

if __name__ == "__main__":
    main()