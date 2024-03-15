
from dataclasses import dataclass

from src.prompts.field import Prompt
from exceptions.validation import *
from localization import get_text

class AIPromptMessages:
    AI = get_text("AI")
    

@dataclass
class AIPrompt(Prompt):
    prompt: str = AIPromptMessages.AI
    
    def validate(self):
        ...


