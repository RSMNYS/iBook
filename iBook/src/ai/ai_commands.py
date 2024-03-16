import json

from iBook.src.commands.command import Command
from iBook.src.exceptions.common import ExitFromUserPrompt
from iBook.src.ai.ai_service import AIAssistant, AIException
from iBook.src.localization import get_text
from iBook.src.ai.ai_prompts import AIPrompt


class RunAIAssistantCommand(Command):
    
    def execute(self,  **kwargs):
        try:
            address_book = kwargs.get('address_book', {})
            notes = kwargs.get('notes', {})
            ai_client = AIAssistant()
            system_instruction = "Given a JSON structure containing 'contacts' and 'notes', filter the data based on specified criteria (e.g., phone numbers starting with a certain digit, substrings in names, titles, or specific words in tags/content). Return the data in the same structure, under the original 'contacts' and 'notes' keys, respectively. Ensure empty arrays are returned for no matches and omit incomplete entries without altering the structure. If command is not related to the data we have, please return empty arrays"

            self.get_ai_answer(ai_client, system_instruction, address_book=address_book, notes=notes)

        except ExitFromUserPrompt:
            print(get_text("AI_BYE_MESSAGE"))
        except AIException as e:
            print(e)

    def get_ai_answer(self, ai_client, system_instruction, address_book, notes):
        prompt = AIPrompt(break_cmd='exit')
        address_book_str = f"{address_book.json()}"
        notes_str = f"{notes.json()}"
        data_str = "{" + "contacts:" + address_book_str + "," + "notes:" + notes_str + "}"
        data_str = f"{data_str}\n\n{prompt.field}"
    
        messages = [{"role": "system", "content": system_instruction}, {"role": "user", "content": data_str}]
        response = ai_client.create_chat_completion(messages=messages)
        data = json.loads(response.choices[0].message.content)
        self.displayData(data)
        self.get_ai_answer(ai_client, system_instruction, address_book, notes)
            
    def displayData(self, data):
        if data.get("contacts"):
            print(get_text("CONTACTS"))
            for contact in data["contacts"]:
                print(f"Name: {contact['name']}, Phone: {', '.join(contact['phones'])}, "
                f"Birthday: {contact['birthday']}, Email: {contact['email']}, Address: {contact['address']}")

        if data.get("notes"):
            print(get_text("NOTES"))
            for note in data["notes"]:
                print(f"Title: {note['title']}, Content: {note['content']}, Tags: {', '.join(note['tags'])}")