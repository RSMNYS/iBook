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
    "NO_CONTACTS_MESSAGE": "There are no contacts matching '{query}'.",
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
    "ADD_NOTE_TITLE": "Enter the title: ",
    "ADD_NOTE_CONTENT": "Enter the content: ",
    "ADD_TAG": "Enter the tag: ",
    "SEARCH_NOTE_BY_TAG": "Enter the tag you want to search: ",
    "SEARCH_NOTE_BY_TITLE": "Enter the title you want to search: ",
    "ADD_CONTACT_NAME": "Enter the name of the contact: ",
    "ADD_CONTACT_PHONE": "Enter the phone number of the contact: ",
    "ADD_CONTACT_EMAIL": "Enter email, press enter to skip: ",
    "ADD_CONTACT_BIRTHDAY": "Enter birthday in format ('DD.MM.YYYY'), press enter to skip: ",
    "ADD_CONTACT_ADDRESS": "Enter the address, press enter to skip: ",
    "REMOVE_CONTACT_NAME": "Enter the name of the contact to remove: ",
    "EDIT_CONTACT_NAME": "Enter the name of the contact to edit: ",
    "EDIT_CONTACT_INFO": "What would you like to edit:\n1. Name\n2. Phone\n3. 'Exit' to switch on main prompt\n",
    "EDIT_CONTACT_NEW_NAME": "Enter the new name for the contact: ",
    "EDIT_CONTACT_NEW_PHONE": "Enter comma-separated phones for the contact: ",
    "AI": "Your question: ",
    "SWITCH_TO_MAIN_PROMPT": "Type 'Exit' to switch on main prompt",
    "NOTE_IS_NOT_EDITED": "Note was not edited",
    "NOTE_IS_EDITED": "Note edited successfully",
    "NOTE_IS_NOT_DELETED": "Note is not deleted!"
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
    "WELCOME_MESSAGE": "Вас вітає бот-асистент!",
    "ENTER_COMMAND": "Введіть команду: ",
    "GOOD_BYE_MESSAGE": "До побачення!",
    "ADD_NOTE": "Замітку додано.",
    "SEARCH_RESULTS": "Пошук результатів:",
    "NO_NOTES_FOUND": "Заміток не знайдено.",
    "TAGS_ADDED": "Теги додані.",
    "NO_NOTES_FOUND_BY_TAG": "Заміток по вказаним тегам не знайдено.",
    "MAIN": 'основна',
    "INVALID_COMMAND": 'Невірна команда.',
    "HELP": "Як я можу Вам допомогти?",
    "UPDATED_PHONE": "Телефон юзера оновлено.",
    "BIRTHDAY_UPDATED": "День Народження юзера оновлено.",
    "CONTACT_IS_DELETED": "Контакт видалено.",
    "CONTACT_IS_UPDATED":"Контакт оновлено.",
    "CONTACTS": "Контакти:",
    "NOTES":"\nЗамітки:",
    "NO_CONTACTS_OR_NOTES": "Доступних контактів або заміток не має.",
    "MISSED_PARAMS": "В Вашому вводі упущені параметри.",
    "NOT_DELETED": "Замітка успішно видалена!",
    "TAG_CHANGED": "Тегу змінено!",
    "NO_BIRTHDAYS_MESSAGE": "Наступні {n} днів , Днів Народження не має.",
    "NO_CONTACTS_MESSAGE": "Немає контактів, що відповідають запиту '{query}'.",
    "UPCOMING_BIRTHDAYS_MESSAGE": "Вкажіть завчасно кількість днів до наступних Днів Народження: ",
    "EMPTY_DAYS_ERROR_MESSAGE": "Графа Дні наперед не може бути пустою",
    "CONTACT_IS_ADDED_MESSAGE":"Контакт додано.",
    "CONTACT_IS_NOT_ADDED": "Контакт не додано.",
    "NOTE_IS_ADDED": "Замітку додано.",
    "NOTE_IS_NOT_ADDED": "Замітку не додано.",
    "NOT_INITIALIZED_AI_CLIENT": "Неможливо ініціалізувати клієнта AI. Будь ласка, введіть OPENAI_API_KEY",
    "AI_BY_MESSAGE": "З Вами було приємно поспілкуватись!",
    "SEARCH_CONTACTS_INSTRUCTION_MESSAGE":
        """
        Для того, щоб оприділити тип пошуку, будь ласка, введіть номер від 1 до 5:

        Для пошуку по імені, введіть 1.
        Для пошуку по номеру телефона, введіть 2.
        Для пошуку по електронній пошті, введіть 3.
        Для пошуку по Дню Народження, введіть 4.
        Для пошуку за адресою, введіть 5.
        """,
    "SEARCH_PROMPT": "Будь ласка, введіть Ваш пошуковий запит: ",
    "EMPTY_SEARCH_QUERY_ERROR": "Помилка: будь ласка, для продовження введіть запит.",
    "ADD_NOTE_TITLE": "Введіть назву: ",
    "ADD_NOTE_CONTENT": "Введіть контент: ",
    "ADD_TAG": "Введіть тегу: ",
    "SEARCH_NOTE_BY_TAG": "Введіть тегу за якою Ви хочете шукати: ",
    "SEARCH_NOTE_BY_TITLE": "Введіть назву за якою Ви хочете шукати: ",
    "ADD_CONTACT_NAME": "Введіть ім'я контакта: ",
    "ADD_CONTACT_PHONE": "Введіть телефонний номер контакта: ",
    "ADD_CONTACT_EMAIL": "Введіть електронну адресу, натисніть enter щоб пропустити: ",
    "ADD_CONTACT_BIRTHDAY": "Ведіть дату народження в форматі('DD.MM.YYYY'), натисніть enter щоб пропустити: ",
    "ADD_CONTACT_ADDRESS": "Введіть адресу, натисніть enter щоб пропустити: ",
    "REMOVE_CONTACT_NAME": "Введіть ім'я контакта, який необхідно видалити: ",
    "EDIT_CONTACT_NAME": "Введіть ім'я контакта, який необхідно змінити: ",
    "EDIT_CONTACT_INFO": "Що Ви хочете змінити:\n1. Ім'я\n2. Номер телефона\n3. 'Exit' щоб переключитися на основне меню\n",
    "EDIT_CONTACT_NEW_NAME": "Введіть нове ім'я контакту: ",
    "EDIT_CONTACT_NEW_PHONE": "Через кому введіть номера телефону контакта: ",
    "AI": "Ваше питання: ",
    "SWITCH_TO_MAIN_PROMPT": "Введіть 'Exit' щоб переключитися на основне меню."
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
    "NO_CONTACTS_MESSAGE": "No hay contactos coincidiendo con '{query}'.",
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
    "ADD_NOTE_TITLE": "Enter the title: ",
    "ADD_NOTE_CONTENT": "Enter the content: ",
    "ADD_TAG": "Enter the tag: ",
    "SEARCH_NOTE_BY_TAG": "Enter the tag you want to search: ",
    "SEARCH_NOTE_BY_TITLE": "Enter the title you want to search: ",
    "ADD_CONTACT_NAME": "Enter the name of the contact: ",
    "ADD_CONTACT_PHONE": "Enter the phone number of the contact: ",
    "ADD_CONTACT_EMAIL": "Enter email, press enter to skip: ",
    "ADD_CONTACT_BIRTHDAY": "Enter birthday in format ('DD.MM.YYYY'), press enter to skip: ",
    "ADD_CONTACT_ADDRESS": "Enter the address, press enter to skip: ",
    "REMOVE_CONTACT_NAME": "Enter the name of the contact to remove: ",
    "EDIT_CONTACT_NAME": "Enter the name of the contact to edit: ",
    "EDIT_CONTACT_INFO": "What would you like to edit:\n1. Name\n2. Phone\n3. 'Exit' to switch on main prompt\n",
    "EDIT_CONTACT_NEW_NAME": "Enter the new name for the contact: ",
    "EDIT_CONTACT_NEW_PHONE": "Enter comma-separated phones for the contact: ",
    "AI": "Your question: ",
    "SWITCH_TO_MAIN_PROMPT": "Type 'Exit' to switch on main prompt"
}