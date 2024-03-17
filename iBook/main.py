from prompt_toolkit import prompt
from colorama import Fore
from dotenv import load_dotenv

from iBook.src.services.autocompleter_service import Completer, RainbowLexer
from iBook.src.address_book.address_book import AddressBook
from iBook.src.notes_book.notes import Notes
from iBook.src.commands.command_dispatcher import CommandDispatcher
from iBook.src.parsers.input_parser import parse_input
from iBook.src.localization import get_text
from iBook.src.services.app_arguments_parser import AppArgumentsParser


def main():

    AppArgumentsParser().arguments_parser()
    
    # load_dotenv()
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
        dispatcher.dispatch(command, address_book=book, notes=notes)

        book.save()
        notes.save()

if __name__ == "__main__":
    main()