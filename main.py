import sys
sys.path.append('src/')

from address_book.address_book import AddressBook
from commands.command_dispatcher import CommandDispatcher
from constants import COMMANDS_DESCRIPTION
from parsers.input_parser import parse_input
from prompt_toolkit import prompt
from address_book.utils import Completer, RainbowLexer


def main():
    book = AddressBook()
    dispatcher = CommandDispatcher()
    print("Welcome to the assistant bot!")
   
    while True:
        user_input = prompt("Enter a command: ", completer=Completer, lexer=RainbowLexer())
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            dispatcher.dispatch(command)
            continue
        if command == "help":
            print(COMMANDS_DESCRIPTION)
            continue
        dispatcher.dispatch(command, *args, address_book=book)


if __name__ == "__main__":
    main()