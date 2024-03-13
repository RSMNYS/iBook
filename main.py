import sys
sys.path.append('src/')

from dotenv import load_dotenv
load_dotenv()

from address_book.address_book import AddressBook
from commands.command_dispatcher import CommandDispatcher
from constants import COMMANDS_DESCRIPTION, WELCOME_MESSAGE, ENTER_COMMAND, \
GOOD_BYE_MESSAGE
from parsers.input_parser import parse_input


def main():
    book = AddressBook.load()
    dispatcher = CommandDispatcher()
    print(WELCOME_MESSAGE)
   
    while True:
        user_input = input(ENTER_COMMAND)
        if len(user_input) == 0:
            continue
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(GOOD_BYE_MESSAGE)
            break
        if command == "hello":
            dispatcher.dispatch(command)
            continue
        if command == "help":
            print(COMMANDS_DESCRIPTION)
            continue
        dispatcher.dispatch(command, *args, address_book=book)
        book.save()


if __name__ == "__main__":
    main()