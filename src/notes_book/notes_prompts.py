from dataclasses import dataclass

from exceptions.validation import TitleTooShortException
from prompts.field import Prompt

class NotePromptMessages:
    ADD_NOTE_TITLE = "Enter the title or type 'Exit' to switch on main prompt: "
    ADD_NOTE_CONTENT = "Enter the content or type 'Exit' to switch on main prompt: "
    ADD_TAG = "Enter the tag or type 'Exit' to switch on main prompt: "
    SEARCH_NOTE_BY_TAG = "SEARCH_NOTE_BY_TA"
    SEARCH_NOTE_BY_TITLE = "SEARCH_NOTE_BY_TITLE"


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
        ...

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