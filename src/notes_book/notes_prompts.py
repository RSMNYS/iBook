from dataclasses import dataclass

from exceptions.validation import TitleTooShortException
from prompts.field import Prompt

from localization import get_text

class NotePromptMessages:
    ADD_NOTE_TITLE = get_text("ADD_NOTE_TITLE")
    ADD_NOTE_CONTENT = get_text("ADD_NOTE_CONTENT")
    ADD_TAG = get_text("ADD_TAG")
    SEARCH_NOTE_BY_TAG = get_text("SEARCH_NOTE_BY_TAG")
    SEARCH_NOTE_BY_TITLE = get_text("SEARCH_NOTE_BY_TITLE")


@dataclass
class TitlePrompt(Prompt):
    prompt: str = NotePromptMessages.ADD_NOTE_TITLE

    def validate(self):
        if len(self.field) < 5:
            raise TitleTooShortException(self.field)

@dataclass
class ContentPrompt(Prompt):
    prompt: str = NotePromptMessages.ADD_NOTE_CONTENT

    def validate(self):
        pass

@dataclass
class TagPrompt(Prompt):
    prompt: str = NotePromptMessages.ADD_TAG

    def validate(self):
        ...
@dataclass
class SearchNoteByTagPrompt(Prompt):
    prompt: str = NotePromptMessages.SEARCH_NOTE_BY_TAG
    
    def validate(self):
        ...

@dataclass
class SearchNoteByTitlePrompt(Prompt):
    prompt: str = NotePromptMessages.SEARCH_NOTE_BY_TITLE
    
    def validate(self):
        ...
@dataclass
class SearchNoteByTagPrompt(Prompt):
    prompt: str = NotePromptMessages.SEARCH_NOTE_BY_TAG
    
    def validate(self):
        ...

@dataclass
class SearchNoteByTitlePrompt(Prompt):
    prompt: str = NotePromptMessages.SEARCH_NOTE_BY_TITLE
    
    def validate(self):
        pass