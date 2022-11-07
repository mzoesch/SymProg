import nltk


def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """

    # pass  # TODO: return list with lower-case tokens. -> ok
    return [token.lower() for token in nltk.word_tokenize(text)]


class TextDocument:

    @staticmethod
    def word_to_count(text: str) -> dict:
        """ This takes a string and returns a dictionary that maps words to their counts. """

        dict = {}
        for word in normalized_tokens(text):
            if word in dict:
                dict[word] += 1
                continue

            dict[word] = 1

        return dict

    def __init__(self, text, id=None):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """

        self.text = text

        self.word_to_count =\
            self.word_to_count(
                self.text
            )  # TODO: Create dictionary that maps words to their counts. -> ok
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDocument instance by reading a file. """

        text = ""  # TODO: read text from filename -> ok
        with open(filename, 'r') as f:
            return cls(f.read(), filename)

        ...

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
        # pass  # TODO: Implement correct return statement. -> ok
        return f'{self.text[:25 - 3]}...' if len(self.text) > 25 else self.text

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
        # pass  # TODO: Implement correct return statement. -> ok
        print(self.word_to_count.keys())
        print(set(self.word_to_count.keys()))
        print(len((self.word_to_count.keys())))
        return len(set(self.word_to_count.keys()) & set(other_doc.word_to_count.keys()))
