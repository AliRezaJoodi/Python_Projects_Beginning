# My GitHub:  		GitHub.com/AliRezaJoodi

def dispaly (title = "Title", description = "", status=True, lenght=22):
    if status == True:
        title = title.ljust(lenght, " ")
        print(title, description)