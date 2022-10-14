# My GitHub:  		GitHub.com/AliRezaJoodi

lenght = 22

def dispaly (title = "Title", description = "", status=True):
    if status == True:
        title = title.ljust(lenght, " ")
        print(title, description)