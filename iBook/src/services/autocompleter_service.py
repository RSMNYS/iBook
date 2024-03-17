
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles.named_colors import NAMED_COLORS
from prompt_toolkit.completion import NestedCompleter


class RainbowLexer(Lexer):
    def lex_document(self, document):
        colors = list(sorted({"Teal": "#008080"}, key=NAMED_COLORS.get))

        def get_line(lineno):
            return [
                (colors[i % len(colors)], c)
                for i, c in enumerate(document.lines[lineno])
            ]

        return get_line


Completer = NestedCompleter.from_nested_dict({'all-contacts': None, 
                                              'ai': None,
                                              'add-note': None, 
                                              'add-tag': None, 
                                              'add-contact': None,
                                              'add-birthday': None, 
                                              'all-notes': None,
                                              'birthdays': None, 
                                              'close': None, 
                                              'change-phone': None,
                                              'exit': None,
                                              'edit-note': None, 
                                              'edit-contact': None, 
                                              'hello': None,
                                              'phone': None,
                                              'show-contact': None,
                                              'show-birthday': None, 
                                              'search-note-title': None, 
                                              'search-note-tag': None, 
                                              'search': None,
                                              'remove-contact': None,
                                              'remove-note': None,
                                              'remove-tag': None,
                                              })