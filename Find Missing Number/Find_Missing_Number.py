# My GitHub:  		GitHub.com/AliRezaJoodi

from Dispaly_Debug import dispaly_debug

#######################################################
def find_missing_number(numbers):
    dispaly_debug ("\n")
    dispaly_debug ("Function:", "find_missing_number")
    dispaly_debug ("numbers (Orginal):", numbers)
    
    numbers.sort()
    dispaly_debug ("numbers (Sort):", numbers)
    
    max_number=numbers[len(numbers)-1]
    dispaly_debug ("max_number:", max_number)
    
    missing_numbers=[]
    visualization_numbers=[]
    for i in range(1,max_number+1):
        if i not in numbers: 
            missing_numbers.append(i)
            visualization_numbers.append("-")
        else:
            visualization_numbers.append(i)
    dispaly_debug ("visualization_numbers:", visualization_numbers)
    dispaly_debug ("missing_numbers:", missing_numbers)
    
    return missing_numbers