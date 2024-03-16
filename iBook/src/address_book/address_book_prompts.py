
from dataclasses import dataclass, field
from datetime import datetime
import re

from iBook.src.localization import get_text
from iBook.src.prompts.field import Prompt
from iBook.src.exceptions.validation import *

class AdressBookPromptMessages:
    ADD_CONTACT_NAME = get_text("ADD_CONTACT_NAME")
    ADD_CONTACT_PHONE = get_text("ADD_CONTACT_PHONE")
    ADD_CONTACT_EMAIL = get_text("ADD_CONTACT_EMAIL")
    ADD_CONTACT_BIRTHDAY = get_text("ADD_CONTACT_BIRTHDAY")
    ADD_CONTACT_ADDRESS = get_text("ADD_CONTACT_ADDRESS")
    REMOVE_CONTACT_NAME = get_text("REMOVE_CONTACT_NAME")
    EDIT_CONTACT_NAME = get_text("EDIT_CONTACT_NAME")
    EDIT_CONTACT_INFO = get_text("EDIT_CONTACT_INFO")
    EDIT_CONTACT_NEW_NAME = get_text("EDIT_CONTACT_NEW_NAME")
    EDIT_CONTACT_NEW_PHONE = get_text("EDIT_CONTACT_NEW_PHONE")
    AI = get_text("AI")


@dataclass
class NamePrompt(Prompt):
    prompt: str = AdressBookPromptMessages.ADD_CONTACT_NAME

    def validate(self):
        if len(self.field) < 5:
            raise NameTooShortException(self.field)


@dataclass
class PhonePrompt(Prompt):
    prompt: str = AdressBookPromptMessages.ADD_CONTACT_PHONE

    def validate(self):
        if not re.match(r"^\d{10}$", self.field):
            raise WrongPhoneFormatException(self.field)


@dataclass
class EmailPrompt(Prompt):
    prompt: str = AdressBookPromptMessages.ADD_CONTACT_EMAIL

    def validate(self):
        if self.field and not re.match(r"[^@]+@[^@]+\.[^@]+", self.field):
            raise WrongEmailException(self.field)


@dataclass
class BirthdayPrompt(Prompt):
    prompt: str = AdressBookPromptMessages.ADD_CONTACT_BIRTHDAY

    def validate(self):
        if self.field:
            try:
                datetime.strptime(self.field, "%d.%m.%Y")
            except ValueError:
                raise WrongDateFormatException(self.field)


@dataclass
class AddressPrompt(Prompt):
    prompt: str = AdressBookPromptMessages.ADD_CONTACT_ADDRESS

    def validate(self):
        ...


@dataclass
class RemoveNamePrompt(NamePrompt):
    prompt: str = AdressBookPromptMessages.REMOVE_CONTACT_NAME


@dataclass
class EditNamePrompt(NamePrompt):
    prompt: str = AdressBookPromptMessages.EDIT_CONTACT_NAME


@dataclass
class EditNewNamePrompt(NamePrompt):
    prompt: str = AdressBookPromptMessages.EDIT_CONTACT_NEW_NAME


@dataclass
class EditNewPhonePrompt(Prompt):
    prompt: str = AdressBookPromptMessages.EDIT_CONTACT_NEW_PHONE

    def validate(self):
        phones = sorted(set([p.strip() for p in self.field.split(',') if p.strip()]))
        for phone in phones:
            if not re.match(r"^\d{10}$", phone):
                raise WrongPhoneFormatException(phone)
        self.field = ','.join(phones)


@dataclass
class EditContactPrompt(Prompt):
    prompt: str = AdressBookPromptMessages.EDIT_CONTACT_INFO
    attribute: str = field(init=False, default="")

    def validate(self):
        if self.field.lower() == "name":
            self.attribute = self.field.lower()
            self.field = EditNewNamePrompt().field
        elif self.field.lower() == 'phone':
            self.attribute = self.field.lower()
            self.field = EditNewPhonePrompt().field
        else:
            raise UnsupportedEditAttributeException(self.field)
