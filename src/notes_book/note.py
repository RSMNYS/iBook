from notes_book.notes_fields import Content, Tag, Title
from localization import get_text


class Note():
    def __init__(self, title):
        self.title = Title(title)
        self.content = ''
        self.tags = []

    def add_content(self, content):
        self.content = Content(content)

    def add_tag(self, tag):
        self.tags.append(Tag(tag))

    def remove_tag(self, tag):
        tag_to_remove = tag
        for t in self.tags:
            if t.value == tag_to_remove:
                self.tags.remove(t)
                print(get_text("TAG_DELETED")) 
            else:
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