import os
import json
from typing import List
from collections import UserDict

import iBook.src.constants as constants
from iBook.src.notes_book.note import Note
from iBook.src.notes_book.notes_fields import Content, Title
from iBook.src.exceptions.validation import NoteNotFoundException

class Notes(UserDict):
    @property
    def notes(self) -> List[Note]:
        notes = []
        for _, value in self.data.items():
            notes.append(value)
        return notes

    def edit_title(self, title, new_title):
        if title in self.data:
            self.data[new_title] = self.data.pop(title)
            self.data[new_title].title = Title(new_title)

    def add_note(self, note: Note):
        self.data[note.title.value] = note

    def edit_note(self, title, new_content=None):
        if title in self.data:
            note = self.data[title]
            if new_content:
                note.content = Content(new_content)

    def delete_note(self, title):
        try:
            self.data.pop(title)
        except KeyError:
            raise NoteNotFoundException(title)
        
    def add_tag(self, tag, title):
        if title in self.data:
            note = self.data[title]
            note.add_tag(tag)

    def remove_tag(self, tag, title):
        note: Note = self.data[title]
        note.remove_tag(tag)

    def get(self, key, default=None) -> Note:
        return self.data.get(key, default)

    @classmethod
    def load(cls) -> 'Notes':
        data = []
        if os.path.exists(constants.FILE_PATH_NOTES):
            with open(constants.FILE_PATH_NOTES, 'r') as f:
                data.extend(json.load(f))

        notes = cls()
        for note in data:
            notes.add_note(Note.from_dict(note))

        return notes

    def save(self):
        with open(constants.FILE_PATH_NOTES, 'w') as f:
            json.dump([r.to_dict() for r in self.notes], f, indent=4)
    
    def search_by_tag(self, tag_query: str) -> List[Note]:
        matching_notes = []
        for note in self.notes:
            for tag in note.tags:
                if tag_query.lower() in tag.value.lower():
                    matching_notes.append(note)
                    break
        return matching_notes

    def search_by_title(self, title_query: str) -> List[Note]:
        matching_notes = []
        for note in self.notes:
            if title_query.lower() in note.title.value.lower():
                matching_notes.append(note)
        return matching_notes

    def json(self):
        return json.dumps([r.to_dict() for r in self.notes], indent=4)
