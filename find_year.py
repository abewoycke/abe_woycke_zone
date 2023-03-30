from datetime import datetime as dt, timedelta
import re

def find_year(key):
    if re.compile('(\d\d)').findall(key)[0] != 1:
        year = dt.today().year
    else:
        year = (dt.today() + timedelta(days=32)).year
    return year