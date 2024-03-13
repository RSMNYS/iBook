import re
from datetime import datetime
from dataclasses import dataclass, field

from exceptions.validation import *
from prompts.message import PromptMessage


@dataclass
class Prompt:
    prompt: str
    field: str = field(init=False, default="")

    def __post_init__(self):
        self.field = input(self.prompt).strip()
        self.validate()

    def validate(self):
        raise NotImplementedError


@dataclass
class NamePrompt(Prompt):
    prompt: str = PromptMessage.ADD_CONTACT_NAME

    def validate(self):
        if len(self.field) < 5:
            raise NameTooShortException(self.field)


@dataclass
class PhonePrompt(Prompt):
    prompt: str = PromptMessage.ADD_CONTACT_PHONE

    def validate(self):
        if not re.match(r"\d{10,}", self.field):
            raise WrongPhoneFormatException(self.field)


@dataclass
class EmailPrompt(Prompt):
    prompt: str = PromptMessage.ADD_CONTACT_EMAIL

    def validate(self):
        if self.field and not re.match(r"[^@]+@[^@]+\.[^@]+", self.field):
            raise WrongEmailException(self.field)


@dataclass
class BirthdayPrompt(Prompt):
    prompt: str = PromptMessage.ADD_CONTACT_BIRTHDAY

    def validate(self):
        if self.field:
            try:
                datetime.strptime(self.field, "%d.%m.%Y")
            except ValueError:
                raise WrongDateFormatException(self.field)


@dataclass
class AddressPrompt(Prompt):
    prompt: str = PromptMessage.ADD_CONTACT_ADDRESS

    def validate(self):
        ...
        
@dataclass
class RemoveNamePrompt(NamePrompt):
    prompt: str = PromptMessage.REMOVE_CONTACT_NAME


@dataclass
class EditNamePrompt(NamePrompt):
    prompt: str = PromptMessage.EDIT_CONTACT_NAME


@dataclass
class EditNewNamePrompt(NamePrompt):
    prompt: str = PromptMessage.EDIT_CONTACT_NEW_NAME


@dataclass
class EditNewPhonePrompt(Prompt):
    prompt: str = PromptMessage.EDIT_CONTACT_NEW_PHONE

    def validate(self):
        phones = sorted(set([p.strip() for p in self.field.split(',') if p.strip()]))
        for phone in phones:
            if not re.match(r"\d{10,}", phone):
                raise WrongPhoneFormatException(phone)
        self.field = ','.join(phones)


@dataclass
class EditContactPrompt(Prompt):
    prompt: str = PromptMessage.EDIT_CONTACT_INFO
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
        

@dataclass
class AIPrompt(Prompt):
    prompt: str = PromptMessage.AI
    
    def validate(self):
        ...

