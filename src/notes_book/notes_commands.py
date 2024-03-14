from commands.command import Command
from exceptions.common import ExitFromUserPrompt
from localization import get_text
from notes_book.note import Note
from notes_book.notes import Notes
from notes_book.notes_prompts import ContentPrompt, TagPrompt, TitlePrompt

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
        note = notes.get(note_to_edit)
        if note:
            new_content = ContentPrompt().field
            new_tags = TagPrompt().field.split(',') if TagPrompt().field else None
            notes.edit_note(note_to_edit, new_content, new_tags)
            print(get_text("NOTE_IS_EDITED"))
        else:
            print(get_text("NOTE_NOT_FOUND"))

class DeleteNoteCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes')
        try:
            self._delete_note(notes)
        except ExitFromUserPrompt:
            print(get_text("NOTE_IS_NOT_DELETED"))

    @staticmethod
    def _delete_note(notes: Notes):
        title_to_delete = TitlePrompt().field
        if title_to_delete in notes:
            notes.delete_note(title_to_delete)
            print(get_text("NOTE_IS_DELETED"))
        else:
            print(get_text("NOTE_NOT_FOUND"))

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