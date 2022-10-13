# GitHub.com/AliRezaJoodi

import random

##########################################
def password_generator_V20(length, number=True, alphabet=True, special=True):
    pass_str=""
    txt=""
    number_str = "0123456789"
    alphabet_uppercase_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lowercase_str = "abcdefghijklmnopqrstuvwxyz"
    special_str = "!#$%&'()*+,-./[\]^_`{|}~"
    
    if number == True:
        txt = txt + number_str
    if alphabet == True:
        txt = txt + alphabet_uppercase_str + alphabet_lowercase_str 
    if special == True:
        txt = txt + special_str 
        
    if length < len(txt):
        pass_list = random.sample(txt,length)
        pass_str = "".join(pass_list)
    else:
        print("Lenght was too much!")
        
    #print("Generated Password: ", pass_str)
    return pass_str

##########################################
def password_generator_V10(length):
    txt="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    
    pass_list = random.sample(txt,length)
    pass_str = "".join(pass_list)
    #print("Generated Password: ", pass_str)
    
    return pass_str