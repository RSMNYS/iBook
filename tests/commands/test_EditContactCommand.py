import pytest
from unittest.mock import MagicMock, PropertyMock
from commands.command import EditContactCommand
from address_book.address_book import AddressBook, Record


@pytest.fixture
def address_book_mock():
    return MagicMock(spec=AddressBook)


@pytest.fixture
def record_mock(mocker):
    mock = MagicMock(spec=Record)
    name_mock = mocker.PropertyMock(return_value='Initial Name')
    type(mock).name = PropertyMock(return_value=MagicMock(value=name_mock))
    return mock


@pytest.fixture
def mock_prompts(mocker):
    mocker.patch('prompts.field.EditNamePrompt.__init__', lambda self: None)
    mocker.patch('prompts.field.EditNamePrompt.field', new_callable=mocker.PropertyMock, return_value="John Doe")
    mocker.patch('prompts.field.EditContactPrompt.__init__', lambda self, attribute=None: None)
    edit_contact_prompt_mock = mocker.patch('prompts.field.EditContactPrompt.field', new_callable=mocker.PropertyMock)
    edit_contact_prompt_mock.return_value = "Jane Doe"


def test_edit_contact_success(address_book_mock, record_mock, mock_prompts):
    address_book_mock.get.return_value = record_mock
    record_mock.name.value = "Jane Doe"
    command = EditContactCommand()
    command.execute(address_book_mock)
    assert record_mock.name.value == "Jane Doe", "Expected name to be updated to 'Jane Doe'"
