from typing import Dict

from iBook.src.ai.ai_commands import RunAIAssistantCommand
from iBook.src.commands.command import Command, HelloCommand

from iBook.src.notes_book.notes_commands import AddNoteCommand, AddTagCommand, AllNotesCommand, RemoveTagCommand, SearchNoteByTilte, SearchNoteByTagCommand, EditNoteCommand, RemoveNoteCommand
from iBook.src.address_book.address_book_commands import (AddBirthdayCommand, AddContactCommand, AllContactsCommand, ChangePhoneCommand,
                              ContactPhoneCommand, ShowBirthdayCommand, ShowBirthdaysCommand,
                              RemoveContactCommand, EditContactCommand, SearchContactsCommand, ShowContactCommand)
from iBook.src.localization import get_text


class CommandDispatcher:
    def __init__(self):
        self.commands: Dict[str, Command] = {
            "hello": HelloCommand(),
            "add-contact": AddContactCommand(),
            "remove-contact": RemoveContactCommand(),
            "edit-contact": EditContactCommand(),
            "change-phone": ChangePhoneCommand(),
            "phone": ContactPhoneCommand(),
            "all-contacts": AllContactsCommand(),
            "show-contact": ShowContactCommand(),
            "add-birthday": AddBirthdayCommand(),
            "show-birthday": ShowBirthdayCommand(),
            "birthdays": ShowBirthdaysCommand(),
            "search": SearchContactsCommand(),
            "ai": RunAIAssistantCommand(),
            "add-note": AddNoteCommand(),
            "edit-note": EditNoteCommand(),
            "remove-note": RemoveNoteCommand(),
            "search-note-title": SearchNoteByTilte(),
            "search-note-tag": SearchNoteByTagCommand(),
            "add-tag": AddTagCommand(),
            "remove-tag": RemoveTagCommand(),
            "all-notes": AllNotesCommand()
        }
    
    def dispatch(self, command_name, **kwargs):
        command = self.commands.get(command_name)
        if command:
            command.execute(**kwargs)
        else:
            print(get_text("INVALID_COMMAND"))
