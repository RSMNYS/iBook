import re
from datetime import datetime
from collections import defaultdict
from typing import List

from iBook.src.address_book.record import Record
from iBook.src.constants import *

from iBook.src.localization import get_text

def display_birthdays_per_week(users: List[Record], delta):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        if not user.birthday:
            continue
        name = user.name.value
        birthday =  datetime.strptime(user.birthday.value, "%d.%m.%Y")
        birthday = birthday.date()
        birthday_this_year = birthday.replace(year=today.year)
       
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        delta = int(delta)
        if delta_days < delta:
            weekday_name = _workday_name_for_date(birthday_this_year)
            birthdays[weekday_name].append(name)

    if len(birthdays) > 0:
        _display_birthdays(birthdays)
    else:
        message = get_text("NO_BIRTHDAYS_MESSAGE").format(n=delta)
        print(message)
    
    

def _display_birthdays(birthdays):
    for birthday, users in birthdays.items():
        row = "{0:9}: {1}".format(birthday, ", ".join(users))
        print(row)


def _workday_name_for_date(date):
     is_saturday = date.weekday() == 5
     is_sunday = date.weekday() == 6
     is_weekend = is_saturday or is_sunday
     weekday_name = date.strftime('%A')
     return weekday_name if not is_weekend else 'Monday'

def validate_date_format(date_string):
    pattern = r'^[0-3][0-9]\.[0-1][0-9]\.[0-9]{4}$'
    if re.match(pattern, date_string):
        return True
    else:
        return False