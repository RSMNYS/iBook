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
    prompt: str = PromptMessage.NAME

    def validate(self):
        if len(self.field) < 5:
            raise NameTooShortException(self.field)


@dataclass
class PhonePrompt(Prompt):
    prompt: str = PromptMessage.PHONE

    def validate(self):
        if not re.match(r"\d{10,}", self.field):
            raise WrongPhoneFormatException(self.field)


@dataclass
class EmailPrompt(Prompt):
    prompt: str = PromptMessage.EMAIL

    def validate(self):
        if self.field and not re.match(r"[^@]+@[^@]+\.[^@]+", self.field):
            raise WrongEmailException(self.field)


@dataclass
class BirthdayPrompt(Prompt):
    prompt: str = PromptMessage.BIRTHDAY

    def validate(self):
        if self.field:
            try:
                datetime.strptime(self.field, "%d.%m.%Y")
            except ValueError:
                raise WrongDateFormatException(self.field)


@dataclass
class AddressPrompt(Prompt):
    prompt: str = PromptMessage.ADDRESS

    def validate(self):
        ...
