# https://github.com/AliRezaJoodi

def find_missing_number(numbers, dibag=False):
    if dibag==True: print("Orginal List:   ",numbers)
    numbers.sort()
    if dibag==True: print("Sort List:      ",numbers)
    max_number=numbers[len(numbers)-1]
    if dibag==True: print("max_number:     ",max_number)
    missing_numbers=[]
    for i in range(1,max_number+1):
        if i not in numbers: missing_numbers.append(i)
    if dibag==True: print("missing_numbers: ", missing_numbers)
    return missing_numbers