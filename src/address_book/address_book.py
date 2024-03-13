import os
import json
from collections import UserDict
from typing import List
from pprint import pprint

import constants
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
        return f'{[str(record) for record in self.records]}'

    @classmethod
    def load(cls) -> 'AddressBook':
        data = []
        if os.path.exists(constants.FILE_PATH_BOOK):
            with open(constants.FILE_PATH_BOOK, 'r') as f:
                data.extend(json.load(f))

        address_book = cls()
        for record in data:
            address_book.add_record(Record.from_dict(record))

        return address_book
    
    def json(self):
        return "{" + f"contacts:" + json.dumps([r.to_dict() for r in self.records], indent=4) + "}"

    
    def save(self):
        with open(constants.FILE_PATH_BOOK, 'w') as f:
            json.dump([r.to_dict() for r in self.records], f, indent=4)

    def show(self):
        pprint([r.to_dict() for r in self.records])
