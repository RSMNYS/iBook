from address_book.field import Note_Tag
from commands.command import Command
from constants import ADD_NOTE, SEARCH_RESULTS, NO_NOTES_FOUND, TAGS_ADDED, NO_NOTES_FOUND_BY_TAG 

class AddNoteCommand(Command):

    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note: ")
        content = input("Enter the content of the note: ")
        kwargs['notes'].add_note(title, content)
        print(ADD_NOTE)

class EditNoteCommand(Command):

    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note to edit: ")
        new_content = input("Enter the new content of the note: ")
        kwargs['notes'].edit_note(title, new_content)

class DeleteNoteCommand(Command):
    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note to delete: ")
        kwargs['notes'].delete_notebook(title)

class SearchNoteByTitleCommand(Command):
    def execute(self, *args, **kwargs):
        query = input("Enter the query to search by title: ")
        results = kwargs['notes'].search_by_title(query)
        if results:
            print(SEARCH_RESULTS)
            for result in results:
                print(result)
        else:
            print(NO_NOTES_FOUND)


class AddTagCommand(Command):

    def execute(self, *args, **kwargs):
        tags_input = input("Enter the tags separated by commas: ")
        tags = [tag.strip() for tag in tags_input.split(",")]
        for tag in tags:
            kwargs['tag_manager'].add_tag(tag)
        print(TAGS_ADDED)
        
class EditTagCommand(Command):

    def execute(self, *args, **kwargs):
        old_tag = input("Enter the old tag: ")
        new_tag = input("Enter the new tag: ")
        kwargs['tags'].edit_tags(Note_Tag(old_tag), Note_Tag(new_tag))

class SearchNoteByTagCommand(Command):

    def execute(self, *args, **kwargs):
        tag = input("Enter the tag to search by: ")
        results = kwargs['notes'].search_by_tag(tag)
        if results:
            print(SEARCH_RESULTS)
            for result in results:
                print(result)
        else:
            print(NO_NOTES_FOUND_BY_TAG)