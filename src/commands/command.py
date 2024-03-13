from abc import ABC, abstractmethod

from decorators.input_error_decorator import input_error
from address_book.address_book import AddressBook
from address_book.record import Record
from address_book.utils import validate_date_format



class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class HelloCommand(Command):
    def execute(self):
        print("How can I help you?")

        
class AddContactCommand(Command):
    
    def execute(self, *args, address_book):

        name = self.get_input("Enter the name of the contact: ")
        if not name:
            print("Error: Name cannot be empty.")
            return
        
        phone = self.get_input("Enter the phone number of the contact: ")
        if not phone:
            print("Error: Phone number cannot be empty.")
            return

        self._add_contact(name, phone, address_book = address_book)

    def _add_contact(self, name, phone, address_book: AddressBook):
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
        print("Contact added.")

    def get_input(self, prompt):
        return input(prompt)


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
        self._add_birthday(name, birthday, address_book)

    def _add_birthday(self, name, birthday, address_book):
        record: Record = address_book.get(name)
        if not record:
            raise KeyError("Enter user name")
        if not validate_date_format(birthday):
            raise ValueError("Birthday has wrong format. Please use: DD.MM.YYYY")
        else:
            record.add_birthday(birthday)
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
        self._show_birthdays(address_book)

    def _show_birthdays(self, address_book: AddressBook):
        if address_book:
            address_book.show_birthdays_per_week()