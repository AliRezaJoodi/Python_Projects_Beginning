# My GitHub:  		GitHub.com/AliRezaJoodi

from Find_Missing_Number import find_missing_number
from Dispaly import dispaly

numbers=[2, 1, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]

def main():
    missing_numbers = find_missing_number(numbers)
    dispaly ("Orginal Numbers:", numbers)
    dispaly ("Missing Numbers:", missing_numbers)

if __name__ == "__main__":
    main()