Note: It's a personal help to manage files.

I need to create few files on the main page. Included:
- `README.md`
- `Dispaly_Debug.py`
- `Function.py`
- `Main.py`

### README.md
Its content is:
```
It's my solutions for **Python Programming**.

### Assignment

### Development
Write your code in `Function.py`. For development, you can use `Main.py` to test your function. Click the "Run" button and main.py will run.

### Output
It's my solutions output

Thanks to: []()  
Source Link:  []()

**Note**: [You can go here to download a single folder or file from GitHub.com](https://minhaskamal.github.io/DownGit/#/home)

```

### Dispaly_Debug.py
It's a function to display everything. It's useful for debug.
Its content is:
```py
debug = True
lenght = 22

def dispaly_debug (title = "Title", description = ""):
    if debug == True:
        title = title.ljust(lenght, " ")
        print(title, description)
```

### Function.py
It's the main code that does the work.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

from Dispaly_Debug import dispaly_debug

def function():
    print("Function Tested")
    dispaly_debug ("Dispaly Debug:", "OK")
```
### Main.py
you can use `Main.py` to test your function.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

from Function import function
from Dispaly_Debug import dispaly_debug

def main ():
    print("Main Tested")
    function()
    

if __name__ == "__main__":
    main ()
```


