# My GitHub:  		GitHub.com/AliRezaJoodi

from Dispaly import dispaly
from datetime import date

debug = False

def age_calculator_v10(birth_date):
    dispaly ("\n", "", debug)
    dispaly ("Function:", "age_calculator_v10", debug)
    
    today_date = date.today()
    dispaly ("Today Date:", today_date, debug)
    dispaly ("Birth Date:", birth_date, debug)
    
    age = (today_date - birth_date).days
    dispaly ("Age (Days):", age, debug)
    age=int(age/365.25)
    dispaly ("Age (Years):", age, debug)
    
    return age

if __name__ == "__main__":
    debug = True
    age_calculator_v10(date(1984, 12, 30))