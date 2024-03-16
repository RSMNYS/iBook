import iBook.src.constants as constants

def get_text(key, language_code='en', format=None):

    """
    Retrieve a localized text message from a dictionary of language-specific constants.

    Parameters:
        key (str): The key corresponding to the desired text message.
        language_code (str, optional): The language code specifying which set of constants to use.
                                       Defaults to 'en' (English).
        format (dict, optional): A dictionary containing placeholder values for substitution.
                                 Defaults to None.

    Returns:
        str: The localized text message with placeholders replaced, if any.

    Example:
        # Retrieve a message without placeholders
        message = get_text("WELCOME_MESSAGE")
        print(message)
        # Output: "Welcome to the assistant bot!"

        # Retrieve a message with placeholders
        #"EXAMPLE_MESSAGE": "Hello {name}, you have {count} new messages."
        placeholders = {'name': 'John', 'count': 3}
        message = get_text("EXAMPLE_MESSAGE", format=placeholders)
        print(message)
        # Output: "Hello John, you have 3 new messages."
    """
    
    language_dictionaries = {
        'en': constants.EN
    }
    text = language_dictionaries.get(language_code, constants.EN).get(key, '')
    if format:
        text = text.format(**format)

    return text
