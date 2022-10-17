# My GitHub:  		GitHub.com/AliRezaJoodi

from display import *
import random

debug = False
    
##########################################
def generate_V20(length=16, number=True, alphabet=True, special=True):
    display("\n", "", debug)
    display("Function:", "generate_V20", debug)
    
    pass_str=""
    txt_str=""
    number_str = "0123456789"
    alphabet_uppercase_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lowercase_str = "abcdefghijklmnopqrstuvwxyz"
    special_str = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    
    if number == True:
        txt_str = txt_str + number_str
    if alphabet == True:
        txt_str = txt_str + alphabet_uppercase_str + alphabet_lowercase_str 
    if special == True:
        txt_str = txt_str + special_str 
    display("txt_str(Primary):", txt_str, debug)
    
    txt_list = random.sample(txt_str,len(txt_str))
    txt_str = "".join(txt_list)
    display("txt_str(Final):", txt_str, debug)
        
    if length < len(txt_str):
        pass_list = random.sample(txt_str,length)
        pass_str = "".join(pass_list)
    else:
        print("Lenght was too much!")   
    display("Password V20:", pass_str, debug)
    
    return pass_str

##########################################
def generate_V10(length=16):
    display("\n", "", debug)
    display("Function:", "generate_V10", debug)
    txt_str="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    display("txt_str", txt_str, debug)
    
    pass_list = random.sample(txt_str,length)
    pass_str = "".join(pass_list)
    display("Password V10:", pass_str, debug)
    
    return pass_str

##########################################
if __name__ == "__main__":
    debug = True
    password = generate_V10()
    password = generate_V20()