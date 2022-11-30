from datetime import date, timedelta 

DAYS = { 'Monday': 0, 
         'Tuesday': 1, 
         'Wednesday': 2, 
         'Thursday': 3, 
         'Friday' : 4, 
         'Saturday': 5, 
         'Sunday': 6}

last = lambda d : d.month != (d + timedelta(days=7)).month
teenth = lambda d : d.day > 12 and d.day < 20
nth = lambda n : lambda d : (d.day - 1) // 7 == n - 1 

NTH = {'teenth': teenth, 
       'last': last, 
       'first': nth(1), 
       'second': nth(2), 
       'third': nth(3), 
       'fourth': nth(4), 
       'fifth': nth(5)}

def meetup(year, month, which, weekday):
    dt = date(year, month, 1)
    while dt.month == month:
        if dt.weekday() == DAYS[weekday] and NTH[which](dt):
            return dt
        dt += timedelta(days=1)
    raise MeetupDayException("That day does not exist.")

class MeetupDayException(ValueError):
    pass