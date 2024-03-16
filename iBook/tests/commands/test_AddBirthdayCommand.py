import pytest
from unittest.mock import MagicMock, patch
from iBook.src.address_book.address_book_commands import AddBirthdayCommand
from iBook.src.address_book.address_book import AddressBook
from iBook.src.address_book.record import Record


@pytest.fixture
def address_book_mock():
    return MagicMock(spec=AddressBook)


@pytest.fixture
def record_mock():
    return MagicMock(spec=Record)


@pytest.fixture
def mock_birthday_prompt(mocker):
    mocker.patch('iBook.src.address_book.address_book_prompts.BirthdayPrompt.__init__', lambda self: None)
    prompt = mocker.patch('iBook.src.address_book.address_book_prompts.BirthdayPrompt.field', new_callable=mocker.PropertyMock)
    return prompt


def test_add_birthday_command_positive(mock_birthday_prompt, address_book_mock, record_mock):
    mock_birthday_prompt.return_value = "01.01.1990"
    address_book_mock.get.return_value = record_mock

    command = AddBirthdayCommand()
    with patch('builtins.input', return_value="01.01.1990"):
        command.execute("John Doe", address_book=address_book_mock)

    record_mock.add_birthday.assert_called_once_with("01.01.1990")


def test_add_birthday_command_key_error(mock_birthday_prompt, address_book_mock):
    address_book_mock.get.side_effect = KeyError("Enter user name")

    command = AddBirthdayCommand()
    with pytest.raises(KeyError):
        command.execute("Nonexistent User", address_book=address_book_mock)


def test_add_birthday_command_empty_birthday_field(mock_birthday_prompt, address_book_mock, record_mock):
    mock_birthday_prompt.return_value = ""
    address_book_mock.get.return_value = record_mock

    command = AddBirthdayCommand()
    with patch('builtins.input', return_value=""):
        command.execute("John Doe", address_book=address_book_mock)

    record_mock.add_birthday.assert_not_called()
