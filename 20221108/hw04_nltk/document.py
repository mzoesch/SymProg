from collections import Counter
from nltk import word_tokenize
import PyPDF2


def load_pdf(path):
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        text = ' '.join(page.extract_text() for page in pdf.pages)
    return text


class TextDocument:
    def __init__(self, docid, text):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """
        self.text = text
        self.docid = docid
        self.word_to_count = Counter(self.normalized_tokens(text))

    @classmethod
    def normalized_tokens(cls, text):
        """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
        return [w.lower() for w in word_tokenize(text)]

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDocument instance by reading a file. """
        with open(filename) as f:
            text = f.read().strip()
        return cls(text, filename)


# TODO: implement Author class and constructor # -> ok
# Needs to be above class PDFDocument - do not change
class Author:

    def __init__(self, firstname, lastname, age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


# TODO: Inherit from TextDocument -> ok
class PDFDocument(TextDocument):

    # TODO: implement constructor (use load_pdf() and call parent constructor) # -> ok
    # pass
    def __init__(self, docid, filepath, author: Author = None) -> None:
        self.text = load_pdf(filepath)
        super().__init__(docid, self.text)
        self.author = author
