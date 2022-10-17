# My GitHub:  		GitHub.com/AliRezaJoodi

from getpass import getpass

def verify(database):
    username = input("Enter Your Username: ")
    password = int(getpass("Enter Your Password: "))
    counter=1
    status=True
    for user_str in database.keys():
        #print (database[u])
        if username==user_str:
            #print (database[u])
            while(True):
                if password==database[user_str]:
                    print("Verified")
                    return True
                print("Password was wrong!")
                if counter>=3:
                    print("Too much trying")
                    print("Didn't verify")
                    return False
                password = int(getpass("Enter Your Password Again: "))
                counter=counter+1
    print("Didn't verify")
    return False

if __name__ == "__main__":
    verify({"bab": 1234})