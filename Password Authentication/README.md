It's my solutions for **Password Authentication**.

### Assignment
Password Authentication is the process of checking the identity of a user.  
There is a database to store usernames and passwords. It's dictionary data type.
for eample:
```py
database = {
    "bab": 1234,
    "Noah": 7410,
    "dfrvu": 6958
}
```
you have to ask for user input as the username by using the input function.  
Then you have to use the getpass module in Python to ask for user input as the password. 
Here we are using the getpass module instead of the input function to make sure that the user doesn’t get to see what he/she write in the password field.  
If the username was correct, the user can try for the password up to three times.

### Development
I created some files for modular programming. They are including:
- **password_authentication.py** (Code for main Tasks.)
- **main.py** (Calling  and  management functions.) 

### Output
It's my solutions output
```
Enter Your Username: bab
Enter Your Password:
Password was wrong!
Enter Your Password Again:
Verified
True
```

Source Link:  [Password Authentication using Python](https://thecleverprogrammer.com/2021/05/02/password-authentication-using-python/)

**Note**: [You can go here to download a single folder or file from GitHub.com](https://minhaskamal.github.io/DownGit/#/home)
