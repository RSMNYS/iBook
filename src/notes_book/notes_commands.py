from address_book.field import Note_Tag
from commands.command import Command

class AddNoteCommand(Command):

    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note: ")
        content = input("Enter the content of the note: ")
        kwargs.get('notes').add_note(title, content)
        print("Note added.")

class EditNoteCommand(Command):

    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note to edit: ")
        new_content = input("Enter the new content of the note: ")
        kwargs.get('notes').edit_note(title, new_content)

class DeleteNoteCommand(Command):
    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note to delete: ")
        kwargs.get('notes').delete_notebook(title)

class SearchNoteByTitleCommand(Command):
    def execute(self, *args, **kwargs):
        query = input("Enter the query to search by title: ")
        results = kwargs.get('notes').search_by_title(query)
        if results:
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No notes found.")


class AddTagCommand(Command):

    def execute(self, *args, **kwargs):
        tags_input = input("Enter the tags separated by commas: ")
        tags = [tag.strip() for tag in tags_input.split(",")]
        for tag in tags:
            kwargs['tag_manager'].add_tag(tag)
        print("Tags added.")
        
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
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No notes found with the specified tag.")