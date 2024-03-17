import os

FILE_PATH_BOOK = os.path.abspath('address_book.json')
FILE_PATH_NOTES = os.path.abspath('notes.json')


EN = {
     "COMMANDS_DESCRIPTION": """
        Available commands:
        
            ai - call AI assistant
            
            all-contacts - show all contacts
            add-contact - add new contact
            add-birthday - add birthday to the existed contact=
            birthdays - show birthdays within next n days
            close or exist - close the app
            change-phone - change a phone for the specied user
            edit-contact - edit the existed contact
            hello - welcome message
            phone - show a phone for the specied contact
            show-contact - show the contact
            show-birthday - show birthday for the contact
            search - search contacts 
            remove-contact - remove contact
            
            add-note - add new note
            add-tag - add tag to the existed note
            all-notes - show all notes
            delete-note - delete note
            edit-tag - edit the note's tag
            edit-note - edit the existed note
            search-note-title - search notes by the title
            search-note-tag - search notes by the tags
            remove-note - remove note
            remove-tag - remove tag
                                             
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
    "NOTE_IS_NOT_DELETED": "Note is not deleted!",
    "TAG_DELETED": "Tag is deleted",
    "TAG_NOT_DELETED": "Tag is not deleted",
    "TAG_IS_ADDED": "Tag added successfully!",
    "TAG_NOT_ADDED": "Tag was not added!",
    "TAG_NOT_FOUND": "No tag found!",
    "REMOVE_NOTE": "Enter the title of the note to remove: ",
    "NO_CONTACTS": "You don't have any contacts!",
    "NO_NOTES": "You don't have any notes!",
    "NO_DATA": "You don't have any data",   
}

UA = {
     "COMMANDS_DESCRIPTION": """
        Список команд:
            ai - викликати AI помічника
            all-contacts - показати всі контакти
            add-contact - додати новий контакт
            add-birthday - додати день народження до існуючого контакту
            birthdays - показати дні народження в наступні n днів
            close або exist - закрити додаток
            change-phone - змінити номер телефону для вказаного користувача
            edit-contact - редагувати існуючий контакт
            hello - привітальне повідомлення
            phone - показати номер телефону для вказаного контакту
            show-contact - показати контакт
            show-birthday - показати день народження контакту
            search - пошук контактів
            remove-contact - видалити контакт
            add-note - додати нову нотатку
            add-tag - додати тег до існуючої нотатки
            all-notes - показати всі нотатки
            delete-note - видалити нотатку
            edit-tag - редагувати тег нотатки
            edit-note - редагувати існуючу нотатку
            search-note-title - пошук нотаток за заголовком
            search-note-tag - пошук нотаток за тегами
            remove-note - видалити нотатку
            remove-tag - видалити тег
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
    "SWITCH_TO_MAIN_PROMPT": "Введіть 'Exit' щоб переключитися на основне меню.",
    "REMOVE_NOTE": "Введіть ім'я нотатки для видалення: ",
    "NO_CONTACTS": "У Вас немає збережених контактів!",
    "NO_NOTES": "У Вас немає збережених нотатків!",
    "NO_DATA": "Дані відсутні",
}

ES = {
     "COMMANDS_DESCRIPTION": """
        Comandos disponibles:

            ai - call AI assistant
            
            all-contacts - show all contacts
            add-contact - add new contact
            add-birthday - add birthday to the existed contact=
            birthdays - show birthdays within next n days
            close or exist - close the app
            change-phone - change a phone for the specied user
            edit-contact - edit the existed contact
            hello - welcome message
            phone - show a phone for the specied contact
            show-contact - show the contact
            show-birthday - show birthday for the contact
            search - search contacts 
            remove-contact - remove contact
            
            add-note - add new note
            add-tag - add tag to the existed note
            all-notes - show all notes
            delete-note - delete note
            edit-tag - edit the note's tag
            edit-note - edit the existed note
            search-note-title - search notes by the title
            search-note-tag - search notes by the tags
            remove-note - remove note
            remove-tag - remove tag
    """,
    "WELCOME_MESSAGE": "¡Bienvenido al asistente virtual!",
    "ENTER_COMMAND": "Escriba un comando: ",
    "GOOD_BYE_MESSAGE": "¡Adiós!",
    "ADD_NOTE": "Nota agregada.",
    "SEARCH_RESULTS": "Resultados de búsqueda:",
    "NO_NOTES_FOUND": "No se encontraron notas.",
    "TAGS_ADDED": "Etiquetas agregadas.",
    "NO_NOTES_FOUND_BY_TAG": "No se encontraron notas con esa etiqueta.",
    "MAIN": 'principal',
    "INVALID_COMMAND": "Comando inválido",
    "HELP": "¿En qué puedo ayudarlo?",
    "UPDATED_PHONE": "El teléfono se acualizó para el usuario.",
    "BIRTHDAY_UPDATED": "El cumpleaños se actualizó para el usuario.",
    "CONTACT_IS_DELETED": "El contacto se ha borrado",
    "CONTACT_IS_UPDATED":"El contacto se actualizó",
    "CONTACTS": "Contactos:",
    "NOTES":"\nNotas:",
    "NO_CONTACTS_OR_NOTES": "No hay contactos o notas disponibles.",
    "MISSED_PARAMS": "Faltan parámetros en su entrada",
    "NOT_DELETED": "Nota borrada con éxito!",
    "TAG_CHANGED": "¡Etiqueta cambiada!",
    "NO_BIRTHDAYS_MESSAGE": "No hay cumpleaños en los siguientes {n} días",
    "UPCOMING_BIRTHDAYS_MESSAGE": "Especifique los días por adelantado para los próximos cumpleaños: ",
    "EMPTY_DAYS_ERROR_MESSAGE": "Error: Los días por adelantado no puede quedar vacio.",
    "CONTACT_IS_ADDED_MESSAGE":"El contacto ha sido agregado.",
    "CONTACT_IS_NOT_ADDED": "El contacto no se agregó",
    "NOTE_IS_ADDED": "La nota ha sido agregada",
    "NOTE_IS_NOT_ADDED": "La nota no ha sido agregada",
    "NOT_INITIALIZED_AI_CLIENT": "El cliente AI no puede iniciar. Por favor agregue la OPENAI_API_KEY",
    "AI_BY_MESSAGE": "Fue agradable hablar con usted",
    "SEARCH_CONTACTS_INSTRUCTION_MESSAGE":
        """
        Para definir el tipo de búsqueda, por favor introduzca un número del 1 al 5:

       Para buscar por nombre, ingrese 1.
        Para buscar por número teléfonico, ingrese 2.
        Para buscar por email, ingrese 3.
        Para buscar por cumpleaños, ingrese 4.
        Para buscar por dirección, ingrese 5.
        """,
    "SEARCH_PROMPT": "Por favor ingrese su criterio de búsqueda: ",
    "EMPTY_SEARCH_QUERY_ERROR": "Error: por favor ingrese una consulta para continuar.",
    "ADD_NOTE_TITLE": "Ingrese el título: ",
    "ADD_NOTE_CONTENT": "Ingrese el contenido: ",
    "ADD_TAG": "Ingrese la etiqueta: ",
    "SEARCH_NOTE_BY_TAG": "Agregue la etiqueta que desea buscar: ",
    "SEARCH_NOTE_BY_TITLE": "Agregue el título que desea buscar: ",
    "ADD_CONTACT_NAME": "Agregue el nombre del contacto: ",
    "ADD_CONTACT_PHONE": "Agregue el numéro teléfonico del contacto: ",
    "ADD_CONTACT_EMAIL": "Agregue el email, oprima enter para saltar: ",
    "ADD_CONTACT_BIRTHDAY": "Agregue el cumpleaños con el formato ('DD.MM.YYYY'), oprima enter para saltar: ",
    "ADD_CONTACT_ADDRESS": "Agregue la dirección, oprima enter para saltar: ",
    "REMOVE_CONTACT_NAME": "Agregue el nombre del contacto por eliminar: ",
    "EDIT_CONTACT_NAME": "Agregue el nombre del contacto por editar: ",
    "EDIT_CONTACT_INFO": "¿Qué le gustaría editar:\n1. Nombre\n2. Teléfono\n3. 'Salir' para cambiar al menú principal\n",
    "EDIT_CONTACT_NEW_NAME": "Agregue el nuevo nombre para el contacto: ",
    "EDIT_CONTACT_NEW_PHONE": "Agregue los teléfonos de contacto separados por comas: ",
    "AI": "Su pregunta: ",
    "SWITCH_TO_MAIN_PROMPT": "oprima 'Salida' para cambiar al menú principal",
    "NO_CONTACTS": "No tienes contactos guardados!",
    "NO_NOTES": "No tienes notas guardadas!",
    "NO_DATA": "No tienes contactos guardados!"
}