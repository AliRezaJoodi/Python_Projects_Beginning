Note: It's a personal help to manage files.

I need to create few files on the main page. Included:
- `README.md`
- `display.py`
- `function.py`
- `main.py`

### README.md
Its content is:
```
It's my solutions for **function**.

### Assignment

### Development
I created some files for modular programming. They are including:
- **display.py** (display everything and usable for debug.)
- **function.py** (Code for main Task.)
- **main.py** (Calling  and  management functions.) 

### Output
It's my solutions output

Thanks to: []()  
Source Link:  []()

**Note**: [You can go here to download a single folder or file from GitHub.com](https://minhaskamal.github.io/DownGit/#/home)
```

### display.py
It's a function to display everything. It's useful for debug.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

LENGHT_TITLE= 22 

def display(title = "Function:", description = "display", status=True, lenght=LENGHT_TITLE):
    if status == True:
	title= str(title)
        title = title.ljust(lenght, " ")
        print(title, description)
        
if __name__ == "__main__":
    display()
```

### function.py
It's the main code that does the work.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

from display import *
from display import LENGHT_TITLE as LENGHT

debug = False

def function():
    display("\n", "", debug)
    display("Function:", "function", debug)

if __name__ == "__main__":
    debug = True
    function()
```
### main.py
you can use `main.py` to test your function.
Its content is:
```py
# My GitHub:  		GitHub.com/AliRezaJoodi

from display import *
from display import LENGHT_TITLE as LENGHT
from function import *

def main():
    display("Function:", "main")
    

if __name__ == "__main__":
    main()
```


