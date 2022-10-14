### Header for pages
```
# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:	   	
```

### Function for Debug
It's a function to display everything. It's useful for debug. Write the code in `Dispaly_Debug.py` then import in your program.
```py
debug = True
lenght = 22

def dispaly_debug (title = "Title", description = ""):
    if debug == True:
        title = title.ljust(lenght, " ")
        print(title, description)
```