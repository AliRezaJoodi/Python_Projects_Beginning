# GitHub.com/AliRezaJoodi

import random

##########################################
def password_generator_V20(length, number=True, alphabet=True, special=True):
    debug=True
    if debug==True: print("\n")
    if debug==True: print("Function:              ", "password_generator_V20")
    pass_str=""
    txt_str=""
    number_str = "0123456789"
    alphabet_uppercase_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lowercase_str = "abcdefghijklmnopqrstuvwxyz"
    special_str = "!#$%&'()*+,-./[\]^_`{|}~"
    
    if number == True:
        txt_str = txt_str + number_str
    if alphabet == True:
        txt_str = txt_str + alphabet_uppercase_str + alphabet_lowercase_str 
    if special == True:
        txt_str = txt_str + special_str 
    if debug==True: print("txt_str(Primary):      ", txt_str)
    
    txt_list = random.sample(txt_str,len(txt_str))
    txt_str = "".join(txt_list)
    if debug==True: print("txt_str(Final):        ", txt_str)
        
    if length < len(txt_str):
        pass_list = random.sample(txt_str,length)
        pass_str = "".join(pass_list)
    else:
        print("Lenght was too much!")   
    if debug==True: print("Password V20:          ", pass_str)
    
    return pass_str


##########################################
def password_generator_V10(length):
    debug=True
    if debug==True: print("\n")
    if debug==True: print("Function:              ", "password_generator_V10")
    txt_str="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    if debug==True: print("txt_str:               ", txt_str)
    
    pass_list = random.sample(txt_str,length)
    pass_str = "".join(pass_list)
    if debug==True: print("Password V10:          ", pass_str)
    
    return pass_str