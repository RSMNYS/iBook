

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
