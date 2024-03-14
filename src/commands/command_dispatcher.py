from typing import Dict

from commands.command import Command, HelloCommand

from notes_book.notes_commands import AddNoteCommand
from address_book.address_book_commands import (AddBirthdayCommand, AddContactCommand, AllContactsCommand, ChangePhoneCommand,
                              ContactPhoneCommand, ShowBirthdayCommand, ShowBirthdaysCommand,
                              RemoveContactCommand, EditContactCommand, RunAIAssistantCommand)
from localization import get_text


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
            "ai": RunAIAssistantCommand(),
            "add-note": AddNoteCommand(),
            # "edit-note": EditNoteCommand(),
            # "delete-note": DeleteNoteCommand(),
            # "search-note-title": SearchNoteByTitleCommand(),
            # "add-tag": AddTagCommand(),
            # "edit-tag": EditTagCommand(),
            # "search-note-tag": SearchNoteByTagCommand()
        }
    
    def dispatch(self, command_name, *args, **kwargs):
        command = self.commands.get(command_name)
        if command:
            command.execute(*args, **kwargs)
        else:
            print(get_text("INVALID_COMMAND"))
