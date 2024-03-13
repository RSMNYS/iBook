from typing import Dict

from commands.command import Command
from notes_book.notes_commands import AddNoteCommand, EditNoteCommand, DeleteNoteCommand, SearchNoteByTitleCommand, AddTagCommand, EditTagCommand, SearchNoteByTagCommand
from commands.command import (AddBirthdayCommand, AddContactCommand, AllContactsCommand, ChangePhoneCommand,
                              ContactPhoneCommand, HelloCommand, ShowBirthdayCommand, ShowBirthdaysCommand,
                              RemoveContactCommand, EditContactCommand, RunAIAssistantCommand)
from notes_book.notes_commands import AddNoteCommand, EditNoteCommand, DeleteNoteCommand, SearchNoteByTitleCommand, AddTagCommand, EditTagCommand, SearchNoteByTagCommand



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
            "ai": RunAIAssistantCommand()
            "birthdays": ShowBirthdaysCommand(),
            "add-note": AddNoteCommand(),
            "edit-note": EditNoteCommand(),
            "delete-note": DeleteNoteCommand(),
            "search-note-title": SearchNoteByTitleCommand(),
            "add-tag": AddTagCommand(),
            "edit-tag": EditTagCommand(),
            "search-note-tag": SearchNoteByTagCommand()
        }
    
    def dispatch(self, command_name, *args, **kwargs):
        command = self.commands.get(command_name)
        if command:
            command.execute(*args, **kwargs)
        else:
            print('Invalid command')
