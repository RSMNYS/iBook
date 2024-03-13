import json

from collections import UserDict
from typing import List
from address_book.record import Record
from address_book.utils import display_birthdays_per_week as display_birthdays_per_week
from exceptions.validation import ContactNameNotFoundException


class AddressBook(UserDict):

    @property
    def records(self) -> List[Record]:
        records = []
        for _, value in self.data.items():
            records.append(value)
        return records
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name) -> Record:
        try:
            return self.data[name]
        except KeyError:
            raise ContactNameNotFoundException(name)
    
    def delete(self, name):
        try:
            self.data.pop(name)
        except KeyError:
            raise ContactNameNotFoundException(name)

    def get(self, key, default=None) -> Record:
        return super().get(key, default)

    def show_birthdays_per_week(self, days_in_advance):
        display_birthdays_per_week(self.records, days_in_advance)

    def __str__(self):
        contacts_list = []
        for record in self.records:
            # Collecting each contact's information in a dict
            contact_info = {
                'name': record.name.value,
                'phones': [phone.value for phone in record.phones],
                'birthday': record.birthday.value if record.birthday else '',
                'email': record.email.value if record.email else '',
                'address': record.address.value if record.address else '',
            }
            contacts_list.append(contact_info)

        # Constructing the desired JSON-like string
        result_dict = {'contacts': contacts_list}
        return json.dumps(result_dict, ensure_ascii=False)