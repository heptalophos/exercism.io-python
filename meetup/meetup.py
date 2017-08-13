import datetime

WEEKDAY = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday' : 4, 'Saturday': 5, 'Sunday': 6}


def last(d):
    return d.month != (d + datetime.timedelta(days=7)).month

def nth(n):
    inweek = lambda d: (d.day - 1) // 7 == n - 1
    return inweek

def teenth(d):
    return (d.day > 12 and d.day < 20)

WHICH = {'teenth': teenth, 'last': last, '1st': nth(1), '2nd': nth(2), '3rd': nth(3), '4th': nth(4), '5th': nth(5)}

def meetup_day(year, month, weekday, which):

    day = datetime.date(year, month, 1)
    
    while day.month == month:
        if day.weekday() == WEEKDAY[weekday] and WHICH[which](day):
            return day
        day += datetime.timedelta(days=1)
    raise Exception("Not a valid meetup day")









