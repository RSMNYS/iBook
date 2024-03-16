from dataclasses import dataclass, field

from iBook.src.exceptions.validation import *
from iBook.src.exceptions.common import ExitFromUserPrompt


@dataclass
class Prompt:
    prompt: str
    break_cmd: str = 'exit'
    field: str = field(init=False, default="")

    def __post_init__(self):
        if self.break_cmd is not None:
            self.wait_for_valid_prompt()
        else:
            self.field = input(self.prompt).strip()
            self.validate()

    def wait_for_valid_prompt(self):
        while True:
            self.field = input(self.prompt).strip()
            if self.field.lower() == self.break_cmd.lower():
                raise ExitFromUserPrompt()
            try:
                self.validate()
            except BaseValidationException as e:
                print(e)
            else:
                break

    def validate(self):
        raise NotImplementedError
