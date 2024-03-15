class BaseValidationException(Exception):
    error: str

    def __init__(self, item: str):
        super().__init__(self.error.format(item=item))


class NameTooShortException(BaseValidationException):
    error = "Contact name '{item}' is too short"


class WrongEmailException(BaseValidationException):
    error = "Contact email '{item}' is not valid"


class WrongPhoneFormatException(BaseValidationException):
    error = "Contact phone number '{item}' is not in the correct format."


class WrongDateFormatException(BaseValidationException):
    error = "Contact birthday format '{item}' is not correct"


class ContactNameNotFoundException(BaseValidationException):
    error = "Contact name '{item}' does not exist in the address book"


class ContactNameAlreadyExistsException(BaseValidationException):
    error = "Contact name '{item}' already exists in the address book"


class UnsupportedEditAttributeException(BaseValidationException):
    error = "Contact attribute '{item}' is not found or not supported for editing"

#TODO: move to the notes
class TitleTooShortException(BaseValidationException):
    error = "Title '{item}' is too short"

class NoteNotFoundException(BaseValidationException):
    error = "Note '{item}' does not exist in notes"
