# My GitHub:  		GitHub.com/AliRezaJoodi

def display(title = "Function:", description = "Display", status=True, lenght=22):
    if status == True:
        title = title.ljust(lenght, " ")
        print(title, description)
        
if __name__ == "__main__":
    display()