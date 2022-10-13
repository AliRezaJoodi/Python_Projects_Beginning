# https://github.com/AliRezaJoodi

def find_missing_number(numbers, dibag=False):
    if dibag==True: print("Orginal List:   ",numbers)
    numbers.sort()
    if dibag==True: print("Sort List:      ",numbers)
    max_number=numbers[len(numbers)-1]
    if dibag==True: print("max_number:     ",max_number)
    missing_number=[]
    for i in range(1,max_number+1):
        if i not in numbers: missing_number.append(i)
    if dibag==True: print("missing_number: ", missing_number)
    return missing_number