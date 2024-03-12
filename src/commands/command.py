from abc import ABC, abstractmethod

from decorators.input_error_decorator import input_error
from address_book.address_book import AddressBook
from address_book.record import Record
from address_book.utils import validate_date_format
from src.constants import *
from prompts.field import NamePrompt, BirthdayPrompt, PhonePrompt, EmailPrompt, AddressPrompt


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class HelloCommand(Command):
    def execute(self):
        print("How can I help you?")


class AddContactCommand(Command):
    
    def execute(self, address_book: AddressBook):
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
