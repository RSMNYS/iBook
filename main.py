import sys
from prompt_toolkit import prompt
from colorama import Fore

sys.path.append('src/')

from dotenv import load_dotenv
load_dotenv()


from services.autocompleter_service import Completer, RainbowLexer
from address_book.address_book import AddressBook
from notes_book.notes import Notes
from commands.command_dispatcher import CommandDispatcher
from parsers.input_parser import parse_input
from localization import get_text


def main():
    book = AddressBook.load()
    notes = Notes.load()
    dispatcher = CommandDispatcher()
    print(Fore.BLUE + '\niBook')
    print(Fore.YELLOW + '\n' + get_text("WELCOME_MESSAGE") + '\n')
   
    while True:
        user_input = prompt(get_text("ENTER_COMMAND"), completer=Completer, lexer=RainbowLexer())
        if len(user_input) == 0:
            continue
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.BLUE + '\n' + get_text("GOOD_BYE_MESSAGE") + '\n')
            break
        if command == "hello":
            dispatcher.dispatch(command)
            continue
        if command == "help":
            print(get_text("COMMANDS_DESCRIPTION"))
            continue
        dispatcher.dispatch(command, *args, address_book=book, notes=notes)

        book.save()
        notes.save()


if __name__ == "__main__":
    main()