import os

FILE_PATH_BOOK = os.path.abspath('address_book.json')
FILE_PATH_NOTES = os.path.abspath('notes.json')


EN = {
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
    """,
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
    "NOTE_IS_ADDED": "Note is added",
    "NOTE_IS_NOT_ADDED": "Note is not added",
    "NOT_INITIALIZED_AI_CLIENT": "AI Client can't be initialized. Please provide the OPENAI_API_KEY",
    "AI_BY_MESSAGE": "It was nice to talk with you",
    "SEARCH_CONTACTS_INSTRUCTION_MESSAGE":
        """
        To define the search type, please enter a number from 1 to 5:

        To search by name, enter 1.
        To search by phone number, enter 2.
        To search by email, enter 3.
        To search by birthday, enter 4.
        To search by address, enter 5.
        """,
    "SEARCH_PROMPT": "Please enter your search query: ",
    "EMPTY_SEARCH_QUERY_ERROR": "Error: Please enter a query to proceed.",
    "ADD_NOTE_TITLE": "Enter the title or type 'Exit' to switch on main prompt: ",
    "ADD_NOTE_CONTENT": "Enter the content or type 'Exit' to switch on main prompt: ",
    "ADD_TAG": "Enter the tag or type 'Exit' to switch on main prompt: ",
    "SEARCH_NOTE_BY_TAG": "Enter the tag you want to search or type 'Exit' to return to the main prompt: ",
    "SEARCH_NOTE_BY_TITLE": "Enter the title you want to search or type 'Exit' to return to the main prompt: ",
    "ADD_CONTACT_NAME": "Enter the name of the contact or type 'Exit' to switch on main prompt: ",
    "ADD_CONTACT_PHONE": "Enter the phone number of the contact or type 'Exit' to switch on main prompt: ",
    "ADD_CONTACT_EMAIL": "Enter email, press enter to skip: ",
    "ADD_CONTACT_BIRTHDAY": "Enter birthday in format ('DD.MM.YYYY'), press enter to skip: ",
    "ADD_CONTACT_ADDRESS": "Enter the address, press enter to skip: ",
    "REMOVE_CONTACT_NAME": "Enter the name of the contact to remove or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_NAME": "Enter the name of the contact to edit or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_INFO": "What would you like to edit:\n1. Name\n2. Phone\n3. 'Exit' to switch on main prompt\n",
    "EDIT_CONTACT_NEW_NAME": "Enter the new name for the contact or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_NEW_PHONE": "Enter comma-separated phones for the contact or type 'Exit' to switch on main prompt: ",
    "AI": "Your question: "
}

UA = {
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
    """,
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
    "NOTE_IS_ADDED": "Note is added",
    "NOTE_IS_NOT_ADDED": "Note is not added",
    "NOT_INITIALIZED_AI_CLIENT": "AI Client can't be initialized. Please provide the OPENAI_API_KEY",
    "AI_BY_MESSAGE": "It was nice to talk with you",
    "SEARCH_CONTACTS_INSTRUCTION_MESSAGE":
        """
        To define the search type, please enter a number from 1 to 5:

        To search by name, enter 1.
        To search by phone number, enter 2.
        To search by email, enter 3.
        To search by birthday, enter 4.
        To search by address, enter 5.
        """,
    "SEARCH_PROMPT": "Please enter your search query: ",
    "EMPTY_SEARCH_QUERY_ERROR": "Error: Please enter a query to proceed.",
    "ADD_NOTE_TITLE": "Enter the title or type 'Exit' to switch on main prompt: ",
    "ADD_NOTE_CONTENT": "Enter the content or type 'Exit' to switch on main prompt: ",
    "ADD_TAG": "Enter the tag or type 'Exit' to switch on main prompt: ",
    "SEARCH_NOTE_BY_TAG": "Enter the tag you want to search or type 'Exit' to return to the main prompt: ",
    "SEARCH_NOTE_BY_TITLE": "Enter the title you want to search or type 'Exit' to return to the main prompt: ",
    "ADD_CONTACT_NAME": "Enter the name of the contact or type 'Exit' to switch on main prompt: ",
    "ADD_CONTACT_PHONE": "Enter the phone number of the contact or type 'Exit' to switch on main prompt: ",
    "ADD_CONTACT_EMAIL": "Enter email, press enter to skip: ",
    "ADD_CONTACT_BIRTHDAY": "Enter birthday in format ('DD.MM.YYYY'), press enter to skip: ",
    "ADD_CONTACT_ADDRESS": "Enter the address, press enter to skip: ",
    "REMOVE_CONTACT_NAME": "Enter the name of the contact to remove or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_NAME": "Enter the name of the contact to edit or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_INFO": "What would you like to edit:\n1. Name\n2. Phone\n3. 'Exit' to switch on main prompt\n",
    "EDIT_CONTACT_NEW_NAME": "Enter the new name for the contact or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_NEW_PHONE": "Enter comma-separated phones for the contact or type 'Exit' to switch on main prompt: ",
    "AI": "Your question: "
}

ES = {
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
    """,
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
    "NOTE_IS_ADDED": "Note is added",
    "NOTE_IS_NOT_ADDED": "Note is not added",
    "NOT_INITIALIZED_AI_CLIENT": "AI Client can't be initialized. Please provide the OPENAI_API_KEY",
    "AI_BY_MESSAGE": "It was nice to talk with you",
    "SEARCH_CONTACTS_INSTRUCTION_MESSAGE":
        """
        To define the search type, please enter a number from 1 to 5:

        To search by name, enter 1.
        To search by phone number, enter 2.
        To search by email, enter 3.
        To search by birthday, enter 4.
        To search by address, enter 5.
        """,
    "SEARCH_PROMPT": "Please enter your search query: ",
    "EMPTY_SEARCH_QUERY_ERROR": "Error: Please enter a query to proceed.",
    "ADD_NOTE_TITLE": "Enter the title or type 'Exit' to switch on main prompt: ",
    "ADD_NOTE_CONTENT": "Enter the content or type 'Exit' to switch on main prompt: ",
    "ADD_TAG": "Enter the tag or type 'Exit' to switch on main prompt: ",
    "SEARCH_NOTE_BY_TAG": "Enter the tag you want to search or type 'Exit' to return to the main prompt: ",
    "SEARCH_NOTE_BY_TITLE": "Enter the title you want to search or type 'Exit' to return to the main prompt: ",
    "ADD_CONTACT_NAME": "Enter the name of the contact or type 'Exit' to switch on main prompt: ",
    "ADD_CONTACT_PHONE": "Enter the phone number of the contact or type 'Exit' to switch on main prompt: ",
    "ADD_CONTACT_EMAIL": "Enter email, press enter to skip: ",
    "ADD_CONTACT_BIRTHDAY": "Enter birthday in format ('DD.MM.YYYY'), press enter to skip: ",
    "ADD_CONTACT_ADDRESS": "Enter the address, press enter to skip: ",
    "REMOVE_CONTACT_NAME": "Enter the name of the contact to remove or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_NAME": "Enter the name of the contact to edit or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_INFO": "What would you like to edit:\n1. Name\n2. Phone\n3. 'Exit' to switch on main prompt\n",
    "EDIT_CONTACT_NEW_NAME": "Enter the new name for the contact or type 'Exit' to switch on main prompt: ",
    "EDIT_CONTACT_NEW_PHONE": "Enter comma-separated phones for the contact or type 'Exit' to switch on main prompt: ",
    "AI": "Your question: "
}