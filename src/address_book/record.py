from address_book.address_book_fields import Name, Phone, Birthday, Email, Address

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone):
        if (len(phone) == 10 and phone.isnumeric()):
            self.phones.append(Phone(phone))
        else:
            raise ValueError(f"Phone number: {phone} is wrong")

    def remove_phone(self, phone):
        self.phones.remove(phone)
    
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

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value if self.birthday else ''}"

    def to_dict(self):
        return dict(
            name=self.name.value,
            phones=[p.value for p in self.phones],
            birthday=self.birthday.value if self.birthday else None,
            email=self.email.value if self.email else None,
            address=self.address.value if self.address else None
        )

    @classmethod
    def from_dict(cls, data) -> 'Record':
        record = Record(data['name'])
        for phone in data['phones']:
            record.add_phone(phone)
        if data['birthday']:
            record.add_birthday(data['birthday'])
        if data['email']:
            record.add_email(data['email'])
        if data['address']:
            record.add_address(data['address'])
        return record