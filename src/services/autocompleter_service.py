
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


Completer = NestedCompleter.from_nested_dict({'hello': None, 'exit': None,
                                              'close': None, 'show-birthday': None, 'add-contact': None,
                                              'change': None, 'add-birthday': None, 'phone': None,
                                              'show': None, 'all': None, 'remove-contact': None,
                                              'edit-contact': None, 'birthdays': None, 'ai': None,
                                              'add-note': None, 'edit-note': None, 'remove-note': None,
                                              'search-note-title': None, 'add-tag': None, 'remove-tag': None,
                                              'search-note-tag': None, 'all-notes': None})
