from address_book.field import Note_Title, Note_Content, Note_Tag
from collections import UserDict


class Notes(UserDict):

    def __init__(self, title="Untitled"):
        super().__init__()
        self.title = Note_Title(title)

    def edit_title(self, title, new_title):
        if title in self.data:
            self.data[new_title] = self.data.pop(title)
            self.data[new_title].title = Note_Title(new_title)

    def add_note(self, title, content):
        self.data[title] = Note_Content(content)

    def edit_note(self, title, new_content):
        if title in self.data:
            self.data[title] = Note_Content(new_content)
        else:
            print(f"Error: Note with title '{title}' not found.")

    def delete_notebook(self, title):
        if title in self.data:
            del self.data[title]
            print("Note deleted successfully!")
        else:
            print(f"Error: Note with title '{title}' not found.")

    def search_by_title(self, query):
        results = []
        for title, content in self.data.items():
            if query.lower() in title.lower():
                results.append((title, content))
        return results


class Tags:
    def __init__(self):
        self.tags = []

    def add_tags(self, tag):
        self.tags.append(Note_Tag(tag))

    def edit_tags(self, old_tag, new_tag):
        try:
            index = self.tags.index(old_tag)
            self.tags[index] = Note_Tag(new_tag)
            print("Tag changed!")
        except ValueError:
            print(f"Error: Note with tag '{old_tag}' not found.")

    def search_by_tag(self, tag, notes):
        results = []
        for title, content in notes.items():
            if tag in self.tags:
                results.append((title, content))
        return results


if __name__ == "__main__":
    print('main')
