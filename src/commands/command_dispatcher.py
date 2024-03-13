from typing import Dict

from commands.command import Command
from commands.command import (AddBirthdayCommand, AddContactCommand, AllContactsCommand, ChangePhoneCommand,
                              ContactPhoneCommand, HelloCommand, ShowBirthdayCommand, ShowBirthdaysCommand,
                              RemoveContactCommand, EditContactCommand, RunAIAssistantCommand, SearchContactsCommand)


class CommandDispatcher:
    def __init__(self):
        self.commands: Dict[str, Command] = {
            "hello": HelloCommand(),
            "add-contact": AddContactCommand(),
            "remove-contact": RemoveContactCommand(),
            "edit-contact": EditContactCommand(),
            "change": ChangePhoneCommand(),
            "phone": ContactPhoneCommand(),
            "all": AllContactsCommand(),
            "add-birthday": AddBirthdayCommand(),
            "show-birthday": ShowBirthdayCommand(),
            "birthdays": ShowBirthdaysCommand(),
            "search": SearchContactsCommand(),
            "ai": RunAIAssistantCommand()
        }
    
    def dispatch(self, command_name, *args, **kwargs):
        command = self.commands.get(command_name)
        if command:
            command.execute(*args, **kwargs)
        else:
            print('Invalid command')
