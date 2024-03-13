from abc import ABC, abstractmethod
from address_book.field import Note_Title, Note_Content, Note_Tag
from notes import Notes, Tags

class NotesCommand(ABC):

    @abstractmethod
    def execute(self):
        pass

class AddNoteCommand(NotesCommand):

    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note: ")
        content = input("Enter the content of the note: ")
        kwargs['notes'].add_note(title, content)
        print("Note added.")

class EditNoteCommand(NotesCommand):

    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note to edit: ")
        new_content = input("Enter the new content of the note: ")
        kwargs['notes'].edit_note(title, new_content)

class DeleteNoteCommand(NotesCommand):
    def execute(self, *args, **kwargs):
        title = input("Enter the title of the note to delete: ")
        kwargs['notes'].delete_notebook(title)

class SearchNoteByTitleCommand(NotesCommand):
    def execute(self, *args, **kwargs):
        query = input("Enter the query to search by title: ")
        results = kwargs['notes'].search_by_title(query)
        if results:
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No notes found.")


class TagsCommand(ABC):

    @abstractmethod
    def execute(self):
        pass

class AddTagCommand(TagsCommand):

    def execute(self, *args, **kwargs):
        tags_input = input("Enter the tags separated by commas: ")
        tags = [tag.strip() for tag in tags_input.split(",")]
        for tag in tags:
            kwargs['tag_manager'].add_tag(tag)
        print("Tags added.")
        
class EditTagCommand(TagsCommand):

    def execute(self, *args, **kwargs):
        old_tag = input("Enter the old tag: ")
        new_tag = input("Enter the new tag: ")
        kwargs['tags'].edit_tags(Note_Tag(old_tag), Note_Tag(new_tag))

class SearchNoteByTagCommand(TagsCommand):

    def execute(self, *args, **kwargs):
        tag = input("Enter the tag to search by: ")
        results = kwargs['notes'].search_by_tag(tag)
        if results:
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No notes found with the specified tag.")