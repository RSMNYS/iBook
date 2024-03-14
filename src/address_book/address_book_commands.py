import json

from address_book.record import Record
from commands.command import Command
from decorators.input_error_decorator import input_error
from address_book.address_book import AddressBook
from exceptions.common import ExitFromUserPrompt
from exceptions.validation import ContactNameNotFoundException, ContactNameAlreadyExistsException
from prompts.field import (NamePrompt, BirthdayPrompt, PhonePrompt, EmailPrompt,
                           AddressPrompt, RemoveNamePrompt, EditNamePrompt, EditContactPrompt, AIPrompt)

from services.ai_service import AIAssistant, AIException
from localization import get_text


class AddContactCommand(Command):
    
    def execute(self, **kwargs):
        address_book = kwargs.get('address_book', {})
        try:
            self._add_new_contact(address_book)
        except ExitFromUserPrompt:
            print(get_text("CONTACT_IS_NOT_ADDED"))
            
    @staticmethod
    def _add_new_contact(address_book: AddressBook):
        record = Record(NamePrompt().field)
        record.add_phone(PhonePrompt().field)

        birthday = BirthdayPrompt()
        email = EmailPrompt()
        address = AddressPrompt()

        if birthday.field:
            record.add_birthday(birthday.field)
        if email.field:
            record.add_email(email.field)
        if address.field:
            record.add_address(address.field)

        address_book.add_record(record)
        print(get_text("CONTACT_IS_ADDED_MESSAGE"))


class ChangePhoneCommand(Command):

    @input_error
    def execute(self, name, phone,  **kwargs):
        address_book = kwargs.get('address_book', {})
        self._change_username_phone(name, phone, address_book)
    
    def _change_username_phone(self,  name, phone, address_book: AddressBook):
        if not address_book.get(name):
            raise KeyError("Enter user name")
        record = address_book.find(name)
        record.phones.clear()
        record.add_phone(phone)
        print(get_text("UPDATED_PHONE"))


class ContactPhoneCommand(Command):
    
    def execute(self, name,  **kwargs):
        address_book = kwargs.get('address_book', {})
        self._phone_for_username(name, address_book)
    
    def _phone_for_username(self, name, address_book):
        record: Record = address_book.find(name)
        print('; '.join(p.value for p in record.phones))


class AllContactsCommand(Command):
   
    def execute(self,  **kwargs):
        address_book = kwargs.get('address_book', {})
        self._all_contacts(address_book)
    
    def _all_contacts(self, address_book: AddressBook):
        for record in address_book.records:
            print(record)
        

class AddBirthdayCommand(Command):
    
    def execute(self, name,  **kwargs):
        address_book = kwargs.get('address_book', {})
        record: Record = address_book.get(name)
        if not record:
            raise KeyError("Enter user name")

        birthday = BirthdayPrompt()
        if birthday.field:
            record.add_birthday(birthday.field)
            print(get_text("BIRTHDAY_UPDATED"))
       

class ShowBirthdayCommand(Command):
    
    def execute(self, name,  **kwargs):
        address_book = kwargs.get('address_book', {})
        self._show_birthday(name, address_book)

   
    def _show_birthday(self, name, address_book: AddressBook):
        record: Record = address_book.get(name)
        if not record:
            raise KeyError("Enter user name")

        print(f"Birthday for the contact: {record.name.value} is on {record.birthday.value}. Don't forget to congrat him")


class ShowBirthdaysCommand(Command):

    def execute(self,  **kwargs):
        address_book = kwargs.get('address_book', {})
        days_in_advance = self.get_input(get_text("UPCOMING_BIRTHDAYS_MESSAGE"))
        if not days_in_advance:
            print(get_text("EMPTY_DAYS_ERROR_MESSAGE"))
            return

        self._show_birthdays(address_book, days_in_advance)

    def _show_birthdays(self, address_book: AddressBook, days_in_advance):
        if address_book:
            address_book.show_birthdays_per_week(days_in_advance)

    def get_input(self, prompt):
        return input(prompt)


class RemoveContactCommand(Command):

    def execute(self,  **kwargs):
        try:
            address_book = kwargs.get('address_book', {})
            address_book.delete(RemoveNamePrompt().field)
        except ContactNameNotFoundException as e:
            print(e)
            self.execute(address_book=address_book)
        except ExitFromUserPrompt:
            print("Contact is not deleted")
        else:
            print(get_text("CONTACT_IS_DELETED"))


class EditContactCommand(Command):

    def execute(self,  **kwargs):
        address_book = kwargs.get('address_book', {})
        try:
            self._edit_contact(address_book)
        except ContactNameNotFoundException as e:
            print(e)
            self.execute(address_book=address_book)
        except ExitFromUserPrompt:
            print("Contact is not updated")
        else:
            print(get_text("CONTACT_IS_UPDATED"))

    @staticmethod
    def _edit_contact(address_book: AddressBook):
        existing_name = EditNamePrompt().field
        record = address_book.get(existing_name)
        if not record:
            raise ContactNameNotFoundException(existing_name)

        edit = EditContactPrompt()

        if edit.attribute == 'name':
            if edit.field == existing_name:
                raise ContactNameAlreadyExistsException(edit.field)
            record.name.value = edit.field
            address_book.pop(existing_name)
            address_book.add_record(record)

        elif edit.attribute == 'phone':
            record.phones.clear()
            for phone in edit.field.split(','):
                record.add_phone(phone)
                    

class RunAIAssistantCommand(Command):
    
    def execute(self,  **kwargs):
        try:
            address_book = kwargs.get('address_book', {})
            ai_client = AIAssistant()
            system_instruction = "Given a JSON structure containing 'contacts' and 'notes', filter the data based on specified criteria (e.g., phone numbers starting with a certain digit, substrings in names, titles, or specific words in tags/content). Return the data in the same structure, under the original 'contacts' and 'notes' keys, respectively. Ensure empty arrays are returned for no matches and omit incomplete entries without altering the structure. If command is not related to the data we have, please return empty arrays"

            self.get_ai_answer(ai_client, system_instruction, address_book=address_book)

        except ExitFromUserPrompt:
            print(get_text("AI_BYE_MESSAGE"))
        except AIException as e:
            print(e)

    def get_ai_answer(self, ai_client, system_instruction, address_book):
        prompt = AIPrompt(break_cmd='exit')
        data_str = f"{address_book.json()}"
        data_str = data_str + f"\n\nQ{prompt.field}"
        messages = [{"role": "system", "content": system_instruction}, {"role": "user", "content": data_str}]
        response = ai_client.create_chat_completion(messages=messages)
        data = json.loads(response.choices[0].message.content)
        self.displayData(data)
        self.get_ai_answer(ai_client, system_instruction, address_book)
            
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