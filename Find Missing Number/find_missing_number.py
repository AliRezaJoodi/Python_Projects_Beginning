# My GitHub:  		GitHub.com/AliRezaJoodi

from display import display

debug: bool= False

#######################################################
def finder(numbers):
    display("\n", "",debug)
    display("Function:", "find_missing_number", debug)
    display("numbers (Orginal):", numbers, debug)
    
    numbers.sort()
    display("numbers (Sort):", numbers, debug)
    
    max_number: int=numbers[len(numbers)-1]
    display("max_number:", max_number, debug)
    
    missing_numbers: list=[]
    visualization_numbers: list=[]
    for i in range(1, max_number+1):
        if i not in numbers: 
            missing_numbers.append(i)
            visualization_numbers.append("-")
        else:
            visualization_numbers.append(i)
    display("visualization_numbers:", visualization_numbers, debug)
    display("missing_numbers:", missing_numbers, debug)
    
    display("\n", "",debug)
    return missing_numbers

if __name__ == "__main__":
    debug = True
    finder([2, 1, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16])
    