class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, field):
        super().__init__(field)

class Phone(Field):
    def __init__(self, field):
        super().__init__(field)

class Birthday(Field):
    def __init__(self, field):
        super().__init__(field)
