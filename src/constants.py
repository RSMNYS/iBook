import os

COMMANDS_DESCRIPTION = """
Available commands:

add-contact [ім'я] [телефон]: Додати новий контакт з іменем та телефонним номером.
remove-contact [ім'я]: Видалити контакт з іменем.
edit-contact [ім'я]: Редагувати контакт.
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
CONTACT_IS_ADDED_MESSAGE = "Contact is added."

FILE_PATH_BOOK = os.path.abspath('address_book.json')
FILE_PATH_NOTES = os.path.abspath('notes.json')

WELCOME_MESSAGE = "Welcome to the assistant bot!"
ENTER_COMMAND = "Enter a command: "
GOOD_BYE_MESSAGE = "Good bye!"