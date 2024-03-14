import os

FILE_PATH_BOOK = os.path.abspath('address_book.json')
FILE_PATH_NOTES = os.path.abspath('notes.json')

SEARCH_CONTACTS_INSTRUCTION_MESSAGE = """
Search Parameters:
1. Search by Name
2. Search by Phone Number
3. Search by Email
4. Search by Birthday
"""
EN = {
    "WELCOME_MESSAGE": "Welcome to the assistant bot!",
    "ENTER_COMMAND": "Enter a command: ",
    "GOOD_BYE_MESSAGE": "Good bye!",
    "ADD_NOTE": "Note added.",
    "SEARCH_RESULTS": "Search results:",
    "NO_NOTES_FOUND": "No notes found.",
    "TAGS_ADDED": "Tags added.",
    "NO_NOTES_FOUND_BY_TAG": "No notes found with the specified tag.",
    "MAIN": 'main',
    "INVALID_COMMAND": 'Invalid command',
    "HELP": "How can I help you?",
    "UPDATED_PHONE": "Phone is updated for the user.",
    "BIRTHDAY_UPDATED": "Birthday is updated for the user.",
    "CONTACT_IS_DELETED": "Contact is deleted",
    "CONTACT_IS_UPDATED":"Contact is updated",
    "CONTACTS": "Contacts:",
    "NOTES":"\nNotes:",
    "NO_CONTACTS_OR_NOTES": "No contacts or notes available.",
    "MISSED_PARAMS": "Missed params in your input",
    "NOT_DELETED": "Note deleted successfully!",
    "TAG_CHANGED": "Tag changed!",
    "NO_BIRTHDAYS_MESSAGE": "No birthdays for the next {n} days to be notified about",
    "UPCOMING_BIRTHDAYS_MESSAGE": "Specify days in advance for upcoming birthdays: ",
    "EMPTY_DAYS_ERROR_MESSAGE": "Error: Days in advance can't be empty.",
    "CONTACT_IS_ADDED_MESSAGE":"Contact is added.",
    "CONTACT_IS_NOT_ADDED": "Contact is not added",
    "NOT_INITIALIZED_AI_CLIENT": "AI Client can't be initialized. Please provide the OPENAI_API_KEY",
    "AI_BY_MESSAGE": "It was nice to talk with you",
    "COMMANDS_DESCRIPTION": """
        Available commands:
        add-contact [ім'я] [телефон]: Додати новий контакт з іменем та телефонним номером
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
}
