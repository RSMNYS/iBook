import re
from abc import ABC, abstractmethod

from decorators.input_error_decorator import input_error
from address_book.address_book import AddressBook
from address_book.record import Record
from address_book.utils import validate_date_format
from constants import CONTACT_PHONE_NUMBER_INPUT_TEXT


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
    
        phone = self._get_phone_from_user()
        email = self._get_email_from_user()

        self._add_contact(name, phone, address_book = address_book)

    def _add_contact(self, name, phone, address_book: AddressBook):
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
        print("Contact added.")

    def get_input(self, prompt):
        return input(prompt)
    
    def _custom_validate_phone(self, number):
        clean_number = number.replace(" ", "").replace("+", "").replace("(", "").replace(")", "").replace("-", "")
        if (len(clean_number) in [10, 12] and clean_number.isnumeric()):
            return True
        else:
            return False
        
    def _get_phone_from_user(self):
        while True:
            phone = self.get_input(CONTACT_PHONE_NUMBER_INPUT_TEXT)
            is_correct_phone = self._custom_validate_phone(phone)
            if not is_correct_phone:
                print("Error: Phone number is not correct. Please try again.")
                continue
            else:
                return phone
            
    def _get_email_from_user(self):
        while True:
            email = self.get_input("Enter the email of the contact: ")
            is_correct_email = self._custom_validate_email(email)
            if not is_correct_email:
                print("Error: Email is not correct. Please try again.")
                continue
            else:
                return email
            
    def _custom_validate_email(self, email):
        pattern = r"[a-zA-Z]+[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}"
        result = re.search(pattern, email, flags=re.IGNORECASE)
        return True if result else False

class ChangePhoneCommand(AddContactCommand):

    @input_error
    def execute(self, name, phone, address_book):
        self._change_username_phone(name, phone, address_book)
    
    def _change_username_phone(self,  name, phone, address_book: AddressBook):
        if not address_book.get(name):
            raise KeyError("Enter user name")
        record = address_book.find(name)
        record.phones.clear()
        if not self._custom_validate_phone(phone):
            phone = self._get_phone_from_user()
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