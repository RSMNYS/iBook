from collections import UserDict
from typing import List
from address_book.record import Record
from address_book.utils import display_birthdays_per_week as birthdays_per_week

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
        return self.data[name]
    
    def delete(self, name):
        self.data.pop(name)

    def show_birthdays_per_week(self):
        birthdays_per_week(self.records)
        