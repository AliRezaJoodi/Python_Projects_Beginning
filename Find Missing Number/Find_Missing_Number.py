# GitHub.com/AliRezaJoodi

##########################################
def find_missing_number(numbers):
    dibug=True
    if dibug==True: print("\n")
    if dibug==True: print("Function:             ", "find_missing_number")
    if dibug==True: print("numbers (Orginal):    ",numbers)
    
    numbers.sort()
    if dibug==True: print("numbers (Sort):       ",numbers)
    
    max_number=numbers[len(numbers)-1]
    if dibug==True: print("max_number:           ",max_number)
    
    missing_numbers=[]
    visualization_numbers=[]
    for i in range(1,max_number+1):
        if i not in numbers: 
            missing_numbers.append(i)
            if dibug==True: visualization_numbers.append("-")
        else:
            if dibug==True: visualization_numbers.append(i)
    if dibug==True: print("visualization_numbers:", visualization_numbers)
    if dibug==True: print("missing_numbers:      ", missing_numbers)
    
    return missing_numbers