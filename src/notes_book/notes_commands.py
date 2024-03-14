from commands.command import Command
from exceptions.common import ExitFromUserPrompt
from localization import get_text
from notes_book.note import Note
from notes_book.notes import Notes
from notes_book.notes_prompts import ContentPrompt, TagPrompt, TitlePrompt
from exceptions.validation import ContactNameNotFoundException

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
            print(get_text("NOTE_NOT_FOUND"))

class DeleteNoteCommand(Command):

    def execute(self, **kwargs):
        try:
            notes = kwargs.get('notes', {})
            title_to_delete = TitlePrompt().field
            notes.data.pop(title_to_delete)
            print(get_text("NOTE_IS_DELETED"))
        except KeyError:
            print(get_text("NOTE_NOT_FOUND")) 
        except ExitFromUserPrompt:
            print(get_text("NOTE_IS_NOT_DELETED"))


# class SearchNoteByTitleCommand(Command):
#     def execute(self, *args, **kwargs):
#         query = input("Enter the query to search by title: ")
#         results = kwargs['notes'].search_by_title(query)
#         if results:
#             print(get_text("SEARCH_RESULTS"))
#             for result in results:
#                 print(result)
#         else:
#             print(get_text("NO_NOTES_FOUND"))


# class AddTagCommand(Command):

#     def execute(self, *args, **kwargs):
#         tags_input = input("Enter the tags separated by commas: ")
#         tags = [tag.strip() for tag in tags_input.split(",")]
#         for tag in tags:
#             kwargs['tag_manager'].add_tag(tag)
#         print(get_text("TAGS_ADDED"))
        
# class EditTagCommand(Command):

#     def execute(self, *args, **kwargs):
#         old_tag = input("Enter the old tag: ")
#         new_tag = input("Enter the new tag: ")
#         kwargs['tags'].edit_tags(Note_Tag(old_tag), Note_Tag(new_tag))

# class SearchNoteByTagCommand(Command):

#     def execute(self, *args, **kwargs):
#         tag = input("Enter the tag to search by: ")
#         results = kwargs['notes'].search_by_tag(tag)
#         if results:
#             print(get_text("SEARCH_RESULTS"))
#             for result in results:
#                 print(result)
#         else:
#             print(get_text("NO_NOTES_FOUND_BY_TAG"))