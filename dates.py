from datetime import timedelta
from datetime import date
from datetime import datetime as dt

# store now, next month
def dates_setup():
    """returns the first day of the following month"""
    now = dt.today()
    one_month = timedelta(days=30)
    next_month = now + one_month
    first_of_next = date(next_month.year,next_month.month,1)
    return first_of_next

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

def main():
    sandwich_dates_to_poll()

if __name__ == '__main__':
    main()