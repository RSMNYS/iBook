import constants

def get_text(key, language_code = 'en'):
    language_dictionaries = {
        'en': constants.EN
    }
    return language_dictionaries.get(language_code, constants.EN).get(key, '')