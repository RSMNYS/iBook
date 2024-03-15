from typing import Dict

from ai.ai_commands import RunAIAssistantCommand
from commands.command import Command, HelloCommand

from notes_book.notes_commands import AddNoteCommand, SearchNoteByTilte, SearchNoteByTagCommand, EditNoteCommand, DeleteNoteCommand, AllNotesCommand
from address_book.address_book_commands import (AddBirthdayCommand, AddContactCommand, AllContactsCommand, ChangePhoneCommand,
                              ContactPhoneCommand, ShowBirthdayCommand, ShowBirthdaysCommand,
                              RemoveContactCommand, EditContactCommand, SearchContactsCommand)
from localization import get_text


class CommandDispatcher:
    def __init__(self):
        self.commands: Dict[str, Command] = {
            "hello": HelloCommand(),
            "add-contact": AddContactCommand(),
            "remove-contact": RemoveContactCommand(),
            "edit-contact": EditContactCommand(),
            "change-phone": ChangePhoneCommand(),
            "phone": ContactPhoneCommand(),
            "all": AllContactsCommand(),
            "add-birthday": AddBirthdayCommand(),
            "show-birthday": ShowBirthdayCommand(),
            "birthdays": ShowBirthdaysCommand(),
            "search": SearchContactsCommand(),
            "ai": RunAIAssistantCommand(),
            "add-note": AddNoteCommand(),
            "edit-note": EditNoteCommand(),
            "remove-note": DeleteNoteCommand(),
            "search-note-title": SearchNoteByTilte(),
            "search-note-tag": SearchNoteByTagCommand(),
            "all-notes": AllNotesCommand()
        }
    
    def dispatch(self, command_name, *args, **kwargs):
        command = self.commands.get(command_name)
        if command:
            command.execute(*args, **kwargs)
        else:
            print(get_text("INVALID_COMMAND"))
