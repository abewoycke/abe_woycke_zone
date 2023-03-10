from datetime import timedelta
from datetime import date
from datetime import datetime as dt

# store now, next month
def dates_setup():
    """returns the first day of the following month"""
    now = dt.today()
    one_month = timedelta(days=30)
    next_month = now + one_month
    first_of_current = date(now.year,now.month,1)
    first_of_next = date(next_month.year,next_month.month,1)
    return first_of_current

# next month's relevant dates for sandwich
def sandwich_dates_to_poll():
    """returns a list of strings, containing the Fridays, Saturdays, and Sundays
    for an upcoming month, with corresponding times Sandwich could Zoom"""
    first_of_next = dates_setup()
    sandwich_poll_options = []
    date_of_interest = first_of_next
    while date_of_interest.month == first_of_next.month:
        if date_of_interest.weekday()==4:
            sandwich_poll_options.append(date_of_interest.strftime('%A %m/%d 7pm PT / 10pm ET'))
        elif date_of_interest.weekday()==5:
            sandwich_poll_options.append(date_of_interest.strftime('%A %m/%d 1pm PT / 4pm ET'))
            sandwich_poll_options.append(date_of_interest.strftime('%A %m/%d 4pm PT / 7pm ET'))
            sandwich_poll_options.append(date_of_interest.strftime('%A %m/%d 7pm PT / 10pm ET'))
        elif date_of_interest.weekday()==6:
            sandwich_poll_options.append(date_of_interest.strftime('%A %m/%d 1pm PT / 4pm ET'))
            sandwich_poll_options .append(date_of_interest.strftime('%A %m/%d 4pm PT / 7pm ET'))
        date_of_interest += timedelta(days=1)
    return sandwich_poll_options

# next month's relevant dates for taustin_dnd
def taustin_dnd_dates_to_poll():
    """returns a list of strings, containing the Fridays, Saturdays, and Sundays for an upcoming month,
    with corresponding times Taustin DnD could meet"""
    first_of_next = dates_setup()
    taustin_dnd_poll_options = []
    date_of_interest = first_of_next
    while date_of_interest.month == first_of_next.month:
        if date_of_interest.weekday()==4:
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 7-10pm'))
        elif date_of_interest.weekday()==5:
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 10am-1pm'))
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 1-4pm'))
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 4-7pm'))
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 7-10pm'))
        elif date_of_interest.weekday()==6:
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 10am-1pm'))
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 1-4pm'))
            taustin_dnd_poll_options.append(date_of_interest.strftime('%A %m/%d 4-7pm'))
        date_of_interest += timedelta(days=1)
    return taustin_dnd_poll_options

# next month's relevant dates for comm_601
def comm_601_dates_to_poll():
    """returns a list of strings, containing the Fridays, Saturdays, and Sundays for an upcoming month,
        with corresponding times comm_601"""
    first_of_next = dates_setup()
    comm_601_poll_options = []
    date_of_interest = first_of_next
    while date_of_interest.month == first_of_next.month:
        if date_of_interest.weekday() == 4:
            comm_601_poll_options.append(date_of_interest.strftime('%A %m/%d 9pm CT'))
        elif date_of_interest.weekday() == 5:
            comm_601_poll_options.append(date_of_interest.strftime('%A %m/%d 8pm CT'))
        elif date_of_interest.weekday() == 6:
            comm_601_poll_options.append(date_of_interest.strftime('%A %m/%d 8pm CT'))
        date_of_interest += timedelta(days=1)
    return comm_601_poll_options

# the prior month year combo, as well as this month and next
def results_dates():
    """returns a list of strings containing the prior month year combo, as well as this month and next"""
    dates = []
    dates.append((dt.today() - timedelta(days=30)).strftime('%B %Y').replace(" ","_"))  # prior month year
    dates.append(dt.today().strftime('%B %Y').replace(" ","_")) # current Month Year (as in March_2023)
    dates.append((dt.today() + timedelta(days=30)).strftime('%B %Y').replace(" ","_")) # next month year
    return dates

def main():
    sandwich_dates_to_poll()

if __name__ == '__main__':
    main()