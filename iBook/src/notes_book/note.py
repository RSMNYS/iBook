from iBook.src.notes_book.notes_fields import Content, Tag, Title
from iBook.src.localization import get_text


class Note():
    def __init__(self, title):
        self.title = Title(title)
        self.content = None
        self.tags = []

    def add_content(self, content):
        self.content = Content(content)

    def add_tag(self, tag):
        self.tags.append(Tag(tag))

    def remove_tag(self, title):
        try:
            tag_to_remove = None
            for tag in self.tags:
                if tag.value == title:
                    tag_to_remove = tag
            self.tags.remove(tag_to_remove)
            print(get_text("TAG_DELETED"))
        except ValueError:
            print(get_text("TAG_NOT_FOUND"))
    
    @classmethod
    def from_dict(cls, data) -> 'Note':
        note = Note(data['title'])
        for tag in data['tags']:
            note.add_tag(tag)
        if data['content']:
            note.add_content(data['content'])
        return note

    def to_dict(self):
        return dict(
            title=self.title.value,
            tags=[t.value for t in self.tags],
            content=self.content.value if self.content else None)
    
    def __str__(self):
        tags_str = ', '.join([tag.value for tag in self.tags])
        content_str = self.content.value if self.content else "No content"
        return f"Title: {self.title.value}\nTags: {tags_str}\nContent: {content_str}\n"