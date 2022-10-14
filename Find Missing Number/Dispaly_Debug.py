# My GitHub:  		GitHub.com/AliRezaJoodi

debug = True
lenght = 22
    
def dispaly_debug (title = "Title", description = ""):
    if debug == True:
        title = title.ljust(lenght, " ")
        print(title, description)