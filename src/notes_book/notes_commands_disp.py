from notes_commands import AddNoteCommand, EditNoteCommand, DeleteNoteCommand, SearchNoteByTitleCommand, AddTagCommand, EditTagCommand, SearchNoteByTagCommand


class NotesCommandDispatcher:

    def __init__(self):
        self.commands = {
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
