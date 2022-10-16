# My GitHub:  		GitHub.com/AliRezaJoodi

from Display import display
from datetime import date

debug = False

def age_calculator_v10(birth_date):
    display ("\n", "", debug)
    display ("Function:", "age_calculator_v10", debug)
    
    age=0
    today_date = date.today()
    display ("Today Date:", today_date, debug)
    display ("Birth Date:", birth_date, debug)
    
    if today_date > birth_date:
        age = (today_date - birth_date).days
        display ("Age (Days):", age, debug)
        age=int(age/365.25)
        display ("Age (Years):", age, debug)
    else:
        display ("Note:", "Birth Date Was Invalid", debug)
    return age

if __name__ == "__main__":
    debug = True
    age_calculator_v10(date(1984, 7, 1))