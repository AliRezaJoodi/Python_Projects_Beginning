# My GitHub:  		GitHub.com/AliRezaJoodi

def display(title = "Function:", description = "display", status=True, lenght=22):
    if status == True:
        title= str(title)
        title = title.ljust(lenght, " ")
        print(title, description)
        
if __name__ == "__main__":
    display()