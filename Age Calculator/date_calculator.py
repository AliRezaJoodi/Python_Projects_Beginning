# My GitHub:  		GitHub.com/AliRezaJoodi

from display import display
from display import LENGHT_TITLE as LENGHT
from datetime import date

debug = False


def calculate_past(date1, date2):
    display("\n", "", debug)
    display("Function:", "calculate", debug)
    display("Start Date:", date1, debug)
    display("Stop Date:", date2, debug)

    past_time = (date2 - date1).days
    display("Past Time (Days):", past_time, debug)
    past_time = int(past_time/365.25)
    display("Past Time (Years):", past_time, debug)
    if date1 > date2:
        display("Note:", "Birth Date Was Invalid", debug)
    return past_time


def get_today():
    display("\n", "", debug)
    display("Function:", "get_today", debug)
    today = date.today()
    display("Today Date:", today, debug)
    return today


def entry_date():
    display("\n", "", debug)
    display("Function:", "entry_date", debug)
    year = int(input("Enter Year:".ljust(LENGHT+1, " ")))
    month = int(input("Enter Month:".ljust(LENGHT+1, " ")))
    day = int(input("Enter Day:".ljust(LENGHT+1, " ")))
    birth = date(year, month, day)
    display("Birth Date:", birth, debug)
    return birth


if __name__ == "__main__":
    debug = True
    calculate_past(entry_date(), get_today())
