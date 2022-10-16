Note: It's a personal help to manage files.

I need to create few files on the main page. Included:
- `README.md`
- `Display.py`
- `Function.py`
- `Main.py`

### README.md
Its content is:
```
It's my solutions for **function**.

### Assignment

### Development
This program written in a few files.
- **Display.py** (Display everything and usable for debug.)
- **Function.py** (Code for main Task.)
- **Main.py** (Calling  and  management functions.) 

### Output
It's my solutions output

Thanks to: []()  
Source Link:  []()

**Note**: [You can go here to download a single folder or file from GitHub.com](https://minhaskamal.github.io/DownGit/#/home)
```

### Display.py
It's a function to display everything. It's useful for debug.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

def display(title = "Function:", description = "Display", status=True, lenght=22):
    if status == True:
        title = title.ljust(lenght, " ")
        print(title, description)
        
if __name__ == "__main__":
    display()
```

### Function.py
It's the main code that does the work.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

from Display import display

debug = False

def function():
    display("\n", "", debug)
    display("Function:", "function", debug)

if __name__ == "__main__":
    debug = True
    function()
```
### Main.py
you can use `Main.py` to test your function.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

from Function import function
from Display import display

def main():
    display("Function:", "main")
    

if __name__ == "__main__":
    main()
```


