COMMANDS_DESCRIPTION = """
Available commands:

add [ім'я] [телефон]: Додати новий контакт з іменем та телефонним номером.
change [ім'я] [новий телефон]: Змінити телефонний номер для вказаного контакту.
phone [ім'я]: Показати телефонний номер для вказаного контакту.
all: Показати всі контакти в адресній книзі.
add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
show-birthday [ім'я]: Показати дату народження для вказаного контакту.
birthdays: Показати дні народження, які відбудуться протягом наступного тижня.
hello: Отримати вітання від бота.
close або exit: Закрити програму.
"""
NO_BIRTHDAYS_MESSAGE = "No birthdays for the next {n} days to be notified about"
UPCOMING_BIRTHDAYS_MESSAGE = "Specify days in advance for upcoming birthdays: "
EMPTY_DAYS_ERROR_MESSAGE = "Error: Days in advance can't be empty."
