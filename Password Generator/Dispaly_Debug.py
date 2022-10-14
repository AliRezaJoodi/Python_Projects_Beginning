# My GitHub:  		GitHub.com/AliRezaJoodi

def dispaly_debug (title = "Title", description = ""):
    debug = True
    lenght = 22
    if debug == True:
        title = title.ljust(lenght, " ")
        print(title, description)