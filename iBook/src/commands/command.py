from abc import ABC, abstractmethod
from iBook.src.localization import get_text

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class HelloCommand(Command):
    def execute(self):
        print(get_text("HELP"))
