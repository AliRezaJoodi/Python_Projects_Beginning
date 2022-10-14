# My GitHub:  		GitHub.com/AliRezaJoodi

from Dispaly import dispaly

#######################################################
def find_missing_number(numbers):
    debug=True
    dispaly ("\n", "",debug)
    dispaly ("Function:", "find_missing_number", debug)
    dispaly ("numbers (Orginal):", numbers, debug)
    
    numbers.sort()
    dispaly ("numbers (Sort):", numbers, debug)
    
    max_number=numbers[len(numbers)-1]
    dispaly ("max_number:", max_number, debug)
    
    missing_numbers=[]
    visualization_numbers=[]
    for i in range(1,max_number+1):
        if i not in numbers: 
            missing_numbers.append(i)
            visualization_numbers.append("-")
        else:
            visualization_numbers.append(i)
    dispaly ("visualization_numbers:", visualization_numbers, debug)
    dispaly ("missing_numbers:", missing_numbers, debug)
    
    dispaly ("\n", "",debug)
    return missing_numbers