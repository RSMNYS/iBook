import pytest
from unittest.mock import MagicMock, patch
from iBook.src.address_book.address_book_commands import RemoveContactCommand
from iBook.src.address_book.address_book import AddressBook
from iBook.src.exceptions.validation import BaseValidationException


@pytest.fixture
def mock_remove_name_prompt(mocker):
    mocker.patch('iBook.src.address_book.address_book_prompts.RemoveNamePrompt.__init__', return_value=None)
    prompt_mock = mocker.patch('iBook.src.address_book.address_book_prompts.RemoveNamePrompt.field', new_callable=mocker.PropertyMock)
    return prompt_mock


def test_remove_contact_success(capsys, mock_remove_name_prompt):
    mock_remove_name_prompt.return_value = "John Doe"
    address_book_mock = MagicMock(spec=AddressBook)
    address_book_mock.delete = MagicMock()

    command = RemoveContactCommand()
    with patch('builtins.input', return_value="John Doe"):
        command.execute(address_book=address_book_mock)

    address_book_mock.delete.assert_called_once_with("John Doe")
    captured = capsys.readouterr()
    assert "Contact is deleted" in captured.out


def test_remove_contact_validation_exception(capsys, mock_remove_name_prompt):
    mock_remove_name_prompt.return_value = "Invalid Name"
    address_book_mock = MagicMock(spec=AddressBook)
    BaseValidationException.error = 'Validation error {item}'
    address_book_mock.delete.side_effect = BaseValidationException("Validation error")

    command = RemoveContactCommand()
    with patch('builtins.input', return_value="Invalid Name"):
        with pytest.raises(BaseValidationException):
            command.execute(address_book=address_book_mock)
