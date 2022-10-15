# My GitHub:  		GitHub.com/AliRezaJoodi

from Age_Calculator import age_calculator_v10
from Dispaly import dispaly

from datetime import date

def main():
    year_int=   int(input("Enter Year of Your Birth:  "))
    month_int=  int(input("Enter Month of Your Birth: "))
    day_int=    int(input("Enter Day of Your Birth:   "))
    birth_date= date(year_int, month_int, day_int)
    age=        age_calculator_v10(birth_date)
    dispaly ("Age:", age)

if __name__ == "__main__":
    main()