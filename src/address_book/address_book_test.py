from address_book.address_book import AddressBook
from address_book.record import Record


def test():
      # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John

    john_record = Record("John")
    add_phone(john_record, "123456890")
    add_phone(john_record, "5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for _, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

def add_phone(record: Record, phone: str):
    try:
        record.add_phone(phone)
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    test()