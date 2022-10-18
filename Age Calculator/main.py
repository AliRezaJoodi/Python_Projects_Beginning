# My GitHub:  		GitHub.com/AliRezaJoodi

from display import *
from date_calculator import *
from date_calculator import calculate_past as calculate_age


def main():
    display("When is your brithday?", "")
    birth_date = entry_date()
    today_date = get_today()
    age = calculate_age(birth_date, today_date)

    display("Birth Date:", birth_date)
    display("Today Date:", today_date)
    display("Age:", age)
    if birth_date > today_date:
        display("Note:", "Birth Date Was Invalid")


if __name__ == "__main__":
    main()
