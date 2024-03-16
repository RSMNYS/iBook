
from dataclasses import dataclass

from iBook.src.prompts.field import Prompt
from iBook.src.exceptions.validation import *
from iBook.src.localization import get_text

class AIPromptMessages:
    AI = get_text("AI")
    

@dataclass
class AIPrompt(Prompt):
    prompt: str = AIPromptMessages.AI
    
    def validate(self):
        ...


