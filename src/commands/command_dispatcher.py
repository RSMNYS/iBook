from typing import Dict
from commands.command import AddBirthdayCommand, AddContactCommand, AllContactsCommand, ChangePhoneCommand, ContactPhoneCommand, HelloCommand, ShowBirthdayCommand, ShowBirthdaysCommand
from commands.command import Command


class CommandDispatcher:
    def __init__(self):
        self.commands: Dict[str, Command] = {
            "hello": HelloCommand(),
            "add": AddContactCommand(),
            "change": ChangePhoneCommand(),
            "phone": ContactPhoneCommand(),
            "all": AllContactsCommand(),
            "add-birthday": AddBirthdayCommand(),
            "show-birthday": ShowBirthdayCommand(),
            "birthdays": ShowBirthdaysCommand()
        }
    
    def dispatch(self, command_name, *args, **kwargs):
        command = self.commands.get(command_name)
        if command:
            command.execute(*args, **kwargs)
        else:
            print('Invalid command')