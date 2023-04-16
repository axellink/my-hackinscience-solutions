# https://www.hackinscience.org/exercises/friday-the-13th

from datetime import date, timedelta
def friday_the_13th():
    d = date.today()
    # Place on next friday
    d += timedelta(days = (4 - d.weekday())%7)
    # look week by week for next friday 13th
    while d.day != 13:
        d += timedelta(days = 7)
    return d.isoformat()