from commands.command import Command
from exceptions.common import ExitFromUserPrompt
from localization import get_text
from notes_book.note import Note
from notes_book.notes import Notes
from notes_book.notes_prompts import ContentPrompt, TagPrompt, TitlePrompt, SearchNoteByTagPrompt, SearchNoteByTitlePrompt

class AddNoteCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes', )
        try:
            self._add_new_note(notes)
        except ExitFromUserPrompt:
            print(get_text("NOTE_IS_NOT_ADDED"))
            
    @staticmethod
    def _add_new_note(notes: Notes):
        note = Note(TitlePrompt().field)
        note.add_content(ContentPrompt().field)
        note.add_tag(TagPrompt().field)

        notes.add_note(note)
        print(get_text("NOTE_IS_ADDED"))

class SearchNoteByTilte(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes', )
        try:
            self._search(notes)
        except ExitFromUserPrompt:
            print("notes search error")
            
    @staticmethod
    def _search(notes: Notes):
        result = []
        search_prompt = SearchNoteByTitlePrompt()
        
        if search_prompt.field:
            result = notes.search_by_title(search_prompt.field)
        
        if not result:
            print(f"No notes found with title '{search_prompt.field}'.")
        else:
            [print(note.__str__()) for note in result]

class SearchNoteByTagCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes', )
        try:
            self._search(notes)
        except ExitFromUserPrompt:
            print("notes search error")
            
    @staticmethod
    def _search(notes: Notes):
        result = []
        search_prompt = SearchNoteByTagPrompt()
        
        if search_prompt.field:
            result = notes.search_by_tag(search_prompt.field)
        
        if not result:
            print(f"No notes found with tag '{search_prompt.field}'.")
        else:
            [print(note.__str__()) for note in result]

class EditNoteCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes')
        try:
            self._edit_note(notes)
        except ExitFromUserPrompt:
            print(get_text("NOTE_IS_NOT_EDITED"))

    @staticmethod
    def _edit_note(notes: Notes):
        note_to_edit = TitlePrompt().field
        if note_to_edit in notes:
            new_content = ContentPrompt().field
            notes.edit_note(note_to_edit, new_content)
            print(get_text("NOTE_IS_EDITED"))
        else:
            print(get_text("NO_NOTES_FOUND"))

class DeleteNoteCommand(Command):

    def execute(self, **kwargs):
        try:
            notes = kwargs.get('notes', {})
            title_to_delete = TitlePrompt().field
            notes.delete_note(title_to_delete)
            print(get_text("NOT_DELETED"))
        except KeyError:
            print(get_text("NO_NOTES_FOUND")) 
        except ExitFromUserPrompt:
            print(get_text("NOTE_IS_NOT_DELETED"))

class AddTagCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes')
        try:
            self._add_tag(notes)
        except ExitFromUserPrompt:
            print(get_text("TAG_NOT_ADDED")) 

    @staticmethod
    def _add_tag(notes: Notes):
        note_to_edit = TitlePrompt().field
        if note_to_edit in notes:
            new_tag = TagPrompt().field
            notes.add_tag(new_tag, note_to_edit)
            print(get_text("TAG_IS_ADDED"))
        else:
            print(get_text("NO_NOTES_FOUND"))

class RemoveTagCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes')
        try:
            self._remove_tag(notes)
        except ExitFromUserPrompt:
            print(get_text("TAG_NOT_DELETED"))

    @staticmethod
    def _remove_tag(notes: Notes):
        note_to_edit = TitlePrompt().field
        if note_to_edit in notes:
            del_tag = TagPrompt().field
            notes.remove_tag(del_tag, note_to_edit)
        else:
            print(get_text("NO_NOTES_FOUND"))

class AllNotesCommand(Command):
   
    def execute(self,  **kwargs):
        notes = kwargs.get('notes', {})
        self._all_notes(notes)
    
    def _all_notes(self, notes: Notes):
        if not notes.notes:
            print(get_text("NO_NOTES_FOUND"))
        else:
            for note in notes.notes:
                print(note)