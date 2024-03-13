import pytest
from exceptions.validation import NameTooShortException, WrongPhoneFormatException, WrongEmailException, WrongDateFormatException
from prompts.field import (NamePrompt, PhonePrompt, EmailPrompt, BirthdayPrompt, AddressPrompt,
                           PromptMessage, RemoveNamePrompt, EditNamePrompt, EditContactPrompt, EditNewNamePrompt,
                           EditNewPhonePrompt)


@pytest.mark.parametrize("input_value", ["Alex", "Jo"])
def test_name_prompt_too_short_validation(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    with pytest.raises(NameTooShortException):
        NamePrompt()


@pytest.mark.parametrize("input_value", ["Alexander", "Elizabeth"])
def test_name_prompt_valid_input(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = NamePrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.ADD_CONTACT_NAME


@pytest.mark.parametrize("input_value", ["123", "abcde12345", "+1(234)567890"])
def test_phone_prompt_invalid_format(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    with pytest.raises(WrongPhoneFormatException):
        PhonePrompt()


@pytest.mark.parametrize("input_value", ["1234567890", "0987654321"])
def test_phone_prompt_valid_input(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = PhonePrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.ADD_CONTACT_PHONE


@pytest.mark.parametrize("input_value", ["email@", "@example.com", "invalidemail"])
def test_email_prompt_invalid_format(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    with pytest.raises(WrongEmailException):
        EmailPrompt()


@pytest.mark.parametrize("input_value", ["", "test@example.com"])
def test_email_prompt_valid_input(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = EmailPrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.ADD_CONTACT_EMAIL


@pytest.mark.parametrize("input_value", ["31-12-1998", "100/01/2000"])
def test_birthday_prompt_invalid_format(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    with pytest.raises(WrongDateFormatException):
        BirthdayPrompt()


@pytest.mark.parametrize("input_value", ["", "01.01.2000"])
def test_birthday_prompt_valid_input(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = BirthdayPrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.ADD_CONTACT_BIRTHDAY


@pytest.mark.parametrize("input_value", ["123 Main St.", ""])
def test_address_prompt_input(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = AddressPrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.ADD_CONTACT_ADDRESS


@pytest.mark.parametrize("input_value", ["Alexander", "Elizabeth"])
def test_remove_name_prompt(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = RemoveNamePrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.REMOVE_CONTACT_NAME


@pytest.mark.parametrize("input_value", ["Alexander", "Elizabeth"])
def test_edit_name_prompt(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = EditNamePrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.EDIT_CONTACT_NAME


@pytest.mark.parametrize("input_value", ["Alexander", "Elizabeth"])
def test_edit_new_name_prompt(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = EditNewNamePrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.EDIT_CONTACT_NEW_NAME


@pytest.mark.parametrize("input_value", ["1234567890,123", "1234567890,0987654321,abcde12345", "+1(234)567890"])
def test_edit_phone_prompt_invalid_format(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    with pytest.raises(WrongPhoneFormatException):
        EditNewPhonePrompt()


@pytest.mark.parametrize("input_value", ["1234567890", "0987654321,0987654321", "1234567890,0987654321, 0987654321, "])
def test_edit_phone_prompt_valid_input(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = EditNewPhonePrompt()
    assert prompt.field == ','.join(sorted(set([p.strip() for p in input_value.split(',') if p.strip()])))
    assert prompt.prompt == PromptMessage.EDIT_CONTACT_NEW_PHONE


def test_edit_contact_prompt_name(monkeypatch, mocker):
    monkeypatch.setattr('builtins.input', lambda _: 'name')
    mocker.patch('prompts.field.EditNewNamePrompt.field', new_callable=mocker.PropertyMock, return_value="John Doe")
    prompt = EditContactPrompt()
    assert prompt.field == 'John Doe'
    assert prompt.prompt == PromptMessage.EDIT_CONTACT_INFO
    assert prompt.attribute == 'name'


def test_edit_contact_prompt_name_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'name')
    with pytest.raises(NameTooShortException):
        EditContactPrompt()


def test_edit_contact_prompt_phone(monkeypatch, mocker):
    monkeypatch.setattr('builtins.input', lambda _: 'phone')
    mocker.patch('prompts.field.EditNewPhonePrompt.field', new_callable=mocker.PropertyMock, return_value="0987654321")
    prompt = EditContactPrompt()
    assert prompt.field == '0987654321'
    assert prompt.prompt == PromptMessage.EDIT_CONTACT_INFO
    assert prompt.attribute == 'phone'


def test_edit_contact_prompt_phone_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'phone')
    with pytest.raises(WrongPhoneFormatException):
        EditContactPrompt()
