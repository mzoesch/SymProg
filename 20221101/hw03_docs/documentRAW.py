def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """

    pass  # TODO: return list with lower-case tokens.


class TextDocument:

    def __init__(self, text, id=None):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """

        pass  # TODO: Create dictionary that maps words to their counts.

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDocument instance by reading a file. """

        text = ""  # TODO: read text from filename
        return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """

        pass  # TODO: Implement correct return statement.

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """

        pass  # TODO: Implement correct return statement.
