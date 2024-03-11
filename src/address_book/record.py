from address_book.field import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if (len(phone) == 10 and phone.isnumeric()):
            self.phones.append(Phone(phone))
        else:
            raise ValueError(f"Phone number: {phone} is wrong")


    def remove_phone(self, phone):
        self.phones.remove[phone]
    

    def edit_phone(self, phone, new_phone):
        for i, item in enumerate(self.phones):
            if item.value == phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item.value
        return None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"
    

if __name__ == "__main__":
    print('main')