from datetime import timedelta
from datetime import date
from datetime import datetime as dt

# months of interest: previous month, current month, next month
def three_moi():
    """returns strings of the previous, current, and upcoming month"""
    now = dt.today()
    one_month = timedelta(days=30)
    next_month = (now + one_month).strftime("%b %Y")
    previous_month = (now - one_month).strftime("%b %Y")
    current_month = now.strftime("%b %Y")
    return previous_month, current_month, next_month

# store now, next month
def dates_setup():
    """returns the first day of the following month"""
    now = dt.today()
    one_month = timedelta(days=30)
    next_month = now + one_month
    first_of_current = date(now.year,now.month,1)
    first_of_next = date(next_month.year,next_month.month,1)
    return first_of_current, first_of_next

def options(group):
    """returns two lists of strings for current month and upcoming month respectively, in the format of the
    group specified"""
    first_of_current, first_of_next = dates_setup()
    options_current = []
    options_next = []
    date_of_interest_current = first_of_current
    date_of_interest_next = first_of_next
    if group=='comm_601':
        while date_of_interest_current.month == first_of_current.month:
            if date_of_interest_current.weekday() == 4:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 9pm CT'))
            elif date_of_interest_current.weekday() == 5:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 8pm CT'))
            elif date_of_interest_current.weekday() == 6:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 8pm CT'))
            date_of_interest_current += timedelta(days=1)
        while date_of_interest_next.month == first_of_next.month:
            if date_of_interest_next.weekday() == 4:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 9pm CT'))
            elif date_of_interest_next.weekday() == 5:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 8pm CT'))
            elif date_of_interest_next.weekday() == 6:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 8pm CT'))
            date_of_interest_next += timedelta(days=1)
    elif group=='taustin_dnd':
        while date_of_interest_current.month == first_of_current.month:
            if date_of_interest_current.weekday() == 4:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 7pm'))
            elif date_of_interest_current.weekday() == 5:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 10am'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 1pm]'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 4pm'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 7pm'))
            elif date_of_interest_current.weekday() == 6:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 10am'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 1pm'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 4pm'))
            date_of_interest_current += timedelta(days=1)
        while date_of_interest_next.month == first_of_next.month:
            if date_of_interest_next.weekday() == 4:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 7pm'))
            elif date_of_interest_next.weekday() == 5:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 10am'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 1pm'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 4pm'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 7pm'))
            elif date_of_interest_next.weekday() == 6:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 10am'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 1pm'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 4pm'))
            date_of_interest_next += timedelta(days=1)
    elif group=='sandwich':
        while date_of_interest_current.month == first_of_current.month:
            if date_of_interest_current.weekday() == 4:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 7pm PT / 10pm ET'))
            elif date_of_interest_current.weekday() == 5:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 1pm PT / 4pm ET'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 4pm PT / 7pm ET'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 7pm PT / 10pm ET'))
            elif date_of_interest_current.weekday() == 6:
                options_current.append(date_of_interest_current.strftime('%A %m/%d 1pm PT / 4pm ET'))
                options_current.append(date_of_interest_current.strftime('%A %m/%d 4pm PT / 7pm ET'))
            date_of_interest_current += timedelta(days=1)
        while date_of_interest_next.month == first_of_next.month:
            if date_of_interest_next.weekday() == 4:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 7pm PT / 10pm ET'))
            elif date_of_interest_next.weekday() == 5:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 1pm PT / 4pm ET'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 4pm PT / 7pm ET'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 7pm PT / 10pm ET'))
            elif date_of_interest_next.weekday() == 6:
                options_next.append(date_of_interest_next.strftime('%A %m/%d 1pm PT / 4pm ET'))
                options_next.append(date_of_interest_next.strftime('%A %m/%d 4pm PT / 7pm ET'))
            date_of_interest_next += timedelta(days=1)
    return options_current, options_next