# My GitHub:  		GitHub.com/AliRezaJoodi

def dispaly(title = "Function:", description = "dispaly", status=True, lenght=26):
    if status == True:
        title = title.ljust(lenght, " ")
        print(title, description)
        
if __name__ == "__main__":
    dispaly()