import pytest
from unittest.mock import create_autospec
from iBook.src.address_book.address_book_commands import AddContactCommand
from iBook.src.address_book.address_book import AddressBook
from iBook.src.address_book.record import Record


@pytest.fixture
def address_book_mock(mocker):
    return create_autospec(AddressBook)


@pytest.fixture
def record_mock(mocker):
    mock = create_autospec(Record)
    mocker.patch('address_book.record.Record', return_value=mock)
    return mock


@pytest.fixture
def setup_prompts(mocker):
    mocker.patch('iBook.src.address_book.address_book_prompts.NamePrompt.__init__', return_value=None)
    mocker.patch('iBook.src.address_book.address_book_prompts.PhonePrompt.__init__', return_value=None)
    mocker.patch('iBook.src.address_book.address_book_prompts.BirthdayPrompt.__init__', return_value=None)
    mocker.patch('iBook.src.address_book.address_book_prompts.EmailPrompt.__init__', return_value=None)
    mocker.patch('iBook.src.address_book.address_book_prompts.AddressPrompt.__init__', return_value=None)

    mocker.patch('iBook.src.address_book.address_book_prompts.NamePrompt.field', new_callable=mocker.PropertyMock, return_value="John Doe")
    mocker.patch('iBook.src.address_book.address_book_prompts.PhonePrompt.field', new_callable=mocker.PropertyMock, return_value="1234567890")
    mocker.patch('iBook.src.address_book.address_book_prompts.BirthdayPrompt.field', new_callable=mocker.PropertyMock, return_value="")
    mocker.patch('iBook.src.address_book.address_book_prompts.EmailPrompt.field', new_callable=mocker.PropertyMock, return_value="")
    mocker.patch('iBook.src.address_book.address_book_prompts.AddressPrompt.field', new_callable=mocker.PropertyMock, return_value="")


@pytest.mark.parametrize("name,phone,birthday,email,address,expect_phone_call,expect_birthday_call,expect_email_call,expect_address_call", [
    ("John Doe", "1234567890", "", "", "", True, False, False, False),
    ("", "1234567890", "01.01.2000", "test@example.com", "123 Main St", True, True, True, True),
    ("Jane Doe", "", "02.02.2000", "", "456 Elm St", True, True, False, True),
    ("Jake Doe", "0987654321", "", "jake@example.com", "", True, False, True, False),
])
def test_execute_various_inputs(setup_prompts, address_book_mock, record_mock, mocker, name, phone, birthday, email, address, expect_phone_call, expect_birthday_call, expect_email_call, expect_address_call):
    mocker.patch('iBook.src.address_book.address_book_prompts.NamePrompt.field', new_callable=mocker.PropertyMock, return_value=name)
    mocker.patch('iBook.src.address_book.address_book_prompts.PhonePrompt.field', new_callable=mocker.PropertyMock, return_value=phone)
    mocker.patch('iBook.src.address_book.address_book_prompts.BirthdayPrompt.field', new_callable=mocker.PropertyMock, return_value=birthday)
    mocker.patch('iBook.src.address_book.address_book_prompts.EmailPrompt.field', new_callable=mocker.PropertyMock, return_value=email)
    mocker.patch('iBook.src.address_book.address_book_prompts.AddressPrompt.field', new_callable=mocker.PropertyMock, return_value=address)

    command = AddContactCommand()
    command.execute(address_book=address_book_mock)

    if expect_phone_call:
        record_mock.add_phone.assert_called_with(phone)
    else:
        record_mock.add_phone.assert_not_called()

    if expect_birthday_call:
        record_mock.add_birthday.assert_called_with(birthday)
    else:
        record_mock.add_birthday.assert_not_called()

    if expect_email_call:
        record_mock.add_email.assert_called_with(email)
    else:
        record_mock.add_email.assert_not_called()

    if expect_address_call:
        record_mock.add_address.assert_called_with(address)
    else:
        record_mock.add_address.assert_not_called()
