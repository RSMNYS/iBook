from typing import List

from iBook.src.address_book.record import Record
from iBook.src.address_book.search_parameters import SearchParameter
from iBook.src.localization import get_text


class AddressBookSearcher:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def search_contact(self, address_book, parameter, query: str) -> List[Record]:
        searchType = int(parameter)
        searchType = SearchParameter(searchType)

        if searchType == SearchParameter.NAME:
            return self.search_by_name(address_book, query)
        elif searchType == SearchParameter.PHONE_NUMBER:
            return self.search_by_phone(address_book, query)
        elif searchType == SearchParameter.EMAIL:
            return self.search_by_email(address_book, query)
        elif searchType == SearchParameter.BIRTHDAY:
            return self.search_by_birthday(address_book, query)
        elif searchType == SearchParameter.ADDRESS:
            return self.search_by_address(address_book, query)
        else:
            return []

    def search_by_name(self, address_book, query: str) -> List[Record]:
        matching_records = []
        for record in address_book.records:
            if query.lower() in record.name.value.lower():
                matching_records.append(record)
            else:
                return print(get_text("NO_CONTACTS_MESSAGE"))
        return matching_records

    def search_by_phone(self, address_book, query: str) -> List[Record]:
        matching_records = []
        for record in address_book.records:
            for phone in record.phones:
                if query.lower() in phone.value.lower():
                    matching_records.append(record)
                else:
                    return print(get_text("NO_CONTACTS_MESSAGE"))
        return matching_records

    def search_by_birthday(self, address_book, query: str) -> List[Record]:
        matching_records = []
        for record in address_book.records:
            if query.lower() in record.birthday.value.lower():
                matching_records.append(record)
            else:
                return print(get_text("NO_CONTACTS_MESSAGE"))
        return matching_records

    def search_by_email(self, address_book, query: str) -> List[Record]:
        matching_records = []
        for record in address_book.records:
            if query.lower() in record.email.value.lower():
                matching_records.append(record)
            else:
                return print(get_text("NO_CONTACTS_MESSAGE"))
        return matching_records

    def search_by_address(self, address_book, query: str) -> List[Record]:
        matching_records = []
        for record in address_book.records:
            if query.lower() in record.address.value.lower():
                matching_records.append(record)
            else:
                return print(get_text("NO_CONTACTS_MESSAGE"))
        return matching_records
