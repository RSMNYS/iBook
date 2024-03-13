from abc import ABC, abstractmethod
import json

from decorators.input_error_decorator import input_error
from address_book.address_book import AddressBook
from address_book.record import Record
from src.constants import *
from exceptions.validation import (BaseValidationException, ContactNameNotFoundException,
                                   ContactNameAlreadyExistsException)
from prompts.field import (NamePrompt, BirthdayPrompt, PhonePrompt, EmailPrompt,
                           AddressPrompt, RemoveNamePrompt, EditNamePrompt, EditContactPrompt, AIPrompt)

from services.ai_service import create_chat_completion


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class HelloCommand(Command):
    def execute(self):
        print("How can I help you?")


class AddContactCommand(Command):
    
    def execute(self, address_book: AddressBook):
        try:
            self._add_new_contact(address_book)
        except BaseValidationException as e:
            print(e)

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


class ChangePhoneCommand(Command):

    @input_error
    def execute(self, name, phone, address_book):
        self._change_username_phone(name, phone, address_book)
    
    def _change_username_phone(self,  name, phone, address_book: AddressBook):
        if not address_book.get(name):
            raise KeyError("Enter user name")
        record = address_book.find(name)
        record.phones.clear()
        record.add_phone(phone)
        print("Phone is updated for the user.")


class ContactPhoneCommand(Command):
    
    def execute(self, name, address_book):
        self._phone_for_username(name, address_book)
    
    def _phone_for_username(self, name, address_book):
        record: Record = address_book.find(name)
        print('; '.join(p.value for p in record.phones))


class AllContactsCommand(Command):
   
    def execute(self, address_book: AddressBook):
        self._all_contacts(address_book)
    
    def _all_contacts(self, address_book: AddressBook):
        for record in address_book.records:
            print(record)
        

class AddBirthdayCommand(Command):
    
    @input_error
    def execute(self, name, birthday, address_book):
        record: Record = address_book.get(name)
        if not record:
            raise KeyError("Enter user name")

        birthday = BirthdayPrompt()
        if birthday.field:
            record.add_birthday(birthday.field)
            print("Birthday is updated for the user.")
       

class ShowBirthdayCommand(Command):
    
    def execute(self, name, address_book):
        self._show_birthday(name, address_book)

   
    def _show_birthday(self, name, address_book: AddressBook):
        record: Record = address_book.get(name)
        if not record:
            raise KeyError("Enter user name")

        print(f"Birthday for the contact: {record.name.value} is on {record.birthday.value}. Don't forget to congrat him")


class ShowBirthdaysCommand(Command):

    def execute(self, address_book):
        days_in_advance = self.get_input(UPCOMING_BIRTHDAYS_MESSAGE)
        if not days_in_advance:
            print(EMPTY_DAYS_ERROR_MESSAGE)
            return

        self._show_birthdays(address_book, days_in_advance)

    def _show_birthdays(self, address_book: AddressBook, days_in_advance):
        if address_book:
            address_book.show_birthdays_per_week(days_in_advance)

    def get_input(self, prompt):
        return input(prompt)


class RemoveContactCommand(Command):

    def execute(self, address_book: AddressBook):
        try:
            address_book.delete(RemoveNamePrompt().field)
        except BaseValidationException as e:
            print(e)
        else:
            print("Contact is deleted")


class EditContactCommand(Command):

    def execute(self, address_book: AddressBook):
        try:
            self._edit_contact(address_book)
        except BaseValidationException as e:
            print(e)
        else:
            print("Contact is updated")

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
                record.add_phone(phone)\
                    
class RunAIAssistantCommand(Command):
    
    def execute(self, address_book: AddressBook):
        prompt = AIPrompt()
        system_instruction = "Given a JSON structure containing 'contacts' and 'notes', filter the data based on specified criteria (e.g., phone numbers starting with a certain digit, substrings in names, titles, or specific words in tags/content). Return the data in the same structure, under the original 'contacts' and 'notes' keys, respectively. Ensure empty arrays are returned for no matches and omit incomplete entries without altering the structure."
        
        # print(system_instruction)
        
        while prompt.field != 'exit':
            data_str = f"{str(address_book)}"
            data_str = data_str + f"\n\nQ{prompt.field}"
            print(data_str)
            messages = [{"role": "system", "content": system_instruction}, {"role": "user", "content": data_str}]
            
            
            # print(messages)
        
            response = create_chat_completion(messages=messages)
            # print(response)
            # print(response.choices)
            # print(response.choices[0])
            # print(response.choices[0].message.content)
            # choice = response.choices[0]
            # data = choice.message
            # print("data:", data)
            # print(response.choices[0].message)
            data = json.loads(response.choices[0].message.content)
            print(data)
            self.displayData(data)
        
            prompt = AIPrompt()
            
    def displayData(self, data):
        if data.get("contacts"):
            print("Contacts:")
            for contact in data["contacts"]:
                print(f"Name: {contact['name']}, Phone: {', '.join(contact['phones'])}, "
                f"Birthday: {contact['birthday']}, Email: {contact['email']}, Address: {contact['address']}")

        if data.get("notes"):
            print("\nNotes:")
            for note in data["notes"]:
                print(f"Title: {note['title']}, Content: {note['content']}, Tags: {', '.join(note['tags'])}")
            else:
                if not data["contacts"]:
                   print("No contacts or notes available.")
       