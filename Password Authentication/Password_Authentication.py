# GitHub.com/AliRezaJoodi

import getpass

def authentication(database):
    username = input("Enter Your Username: ")
    password = int(getpass.getpass("Enter Your Password: "))
    counter=1
    status=True
    for u in database.keys():
        #print (database[u])
        if username==u:
            #print (database[u])
            while(True):
                if password==database[u]:
                    print("Verified")
                    return True
                print("Password was wrong!")
                if counter>=3:
                    print("Too much trying")
                    print("Didn't authentication ")
                    return False
                password = int(getpass.getpass("Enter Your Password Again: "))
                counter=counter+1
    print("Didn't authentication ")
    return False