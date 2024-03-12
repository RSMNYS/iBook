import pytest
from prompts.field import NamePrompt, PhonePrompt, EmailPrompt, BirthdayPrompt, AddressPrompt, PromptMessage
from exceptions.validation import NameTooShortException, WrongPhoneFormatException, WrongEmailException, WrongDateFormatException


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
    assert prompt.prompt == PromptMessage.NAME


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
    assert prompt.prompt == PromptMessage.PHONE


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
    assert prompt.prompt == PromptMessage.EMAIL


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
    assert prompt.prompt == PromptMessage.BIRTHDAY


@pytest.mark.parametrize("input_value", ["123 Main St.", ""])
def test_address_prompt_input(monkeypatch, input_value):
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    prompt = AddressPrompt()
    assert prompt.field == input_value
    assert prompt.prompt == PromptMessage.ADDRESS
