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

class SearchNoteByTilte(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes', )
        try:
            self._search(notes)
        except ExitFromUserPrompt:
            print("notes search error")
            
    @staticmethod
    def _search(notes: Notes):
        title = TitlePrompt()
        print("SearchNoteByTilte")

class SearchNoteByTagCommand(Command):

    def execute(self, **kwargs):
        notes = kwargs.get('notes', )
        try:
            self._search(notes)
        except ExitFromUserPrompt:
            print("notes search error")
            
    @staticmethod
    def _search(notes: Notes):
        title = TagPrompt()
        print("SearchNoteByTagCommand")

# class EditNoteCommand(Command):

#     def execute(self, *args, **kwargs):
#         title = input("Enter the title of the note to edit: ")
#         new_content = input("Enter the new content of the note: ")
#         kwargs['notes'].edit_note(title, new_content)

# class DeleteNoteCommand(Command):
#     def execute(self, *args, **kwargs):
#         title = input("Enter the title of the note to delete: ")
#         kwargs['notes'].delete_notebook(title)

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