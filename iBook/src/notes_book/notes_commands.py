from iBook.src.commands.command import Command
from iBook.src.exceptions.common import ExitFromUserPrompt
from iBook.src.localization import get_text
from iBook.src.notes_book.note import Note
from iBook.src.notes_book.notes import Notes
from iBook.src.notes_book.notes_prompts import ContentPrompt, RemoveNotePrompt, TagPrompt, TitlePrompt, SearchNoteByTagPrompt, SearchNoteByTitlePrompt
from iBook.src.exceptions.validation import NoteNotFoundException

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

class RemoveNoteCommand(Command):

    def execute(self, **kwargs):
        try:
            notes: Notes = kwargs.get('notes', {})
            title_to_delete = RemoveNotePrompt().field
            notes.delete_note(title_to_delete)
        except NoteNotFoundException as e:
            print(e)
            self.execute(notes=notes)
        except ExitFromUserPrompt:
            print(get_text("NOTE_IS_NOT_DELETED"))
        else:
            print(get_text("NOT_DELETED"))


class AddTagCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes')
        try:
            self._add_tag(notes)
        except NoteNotFoundException as e:
            print(e)
            self.execute(notes=notes)
        except ExitFromUserPrompt:
            print(get_text("TAG_NOT_ADDED")) 

    @staticmethod
    def _add_tag(notes: Notes):
        title = TitlePrompt().field
        note = notes.get(title)
        if not note:
            raise NoteNotFoundException(get_text("NO_NOTES_FOUND"))

        new_tag = TagPrompt().field
        note.add_tag(new_tag)
        print(get_text("TAG_IS_ADDED"))


class RemoveTagCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes')
        try:
            self._remove_tag(notes)
        except NoteNotFoundException as e:
            print(e)
            self.execute(notes=notes)
        except ExitFromUserPrompt:
            print(get_text("TAG_NOT_DELETED"))

    @staticmethod
    def _remove_tag(notes: Notes):
        title = TitlePrompt().field
        note = notes.get(title)
        if not note:
            raise NoteNotFoundException(get_text("NO_NOTES_FOUND"))
        del_tag = TagPrompt().field

        note.remove_tag(del_tag)


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