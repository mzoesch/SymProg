from nltk.tokenize import *
import nltk.data
from nltk.corpus import inaugural
from nltk.corpus import webtext
from nltk import FreqDist
from nltk.corpus import swadesh


class Preprocessor(object):

    def __init__(self, text, text_id):
        """ Reads the file text as a string """

        self.text = text
        self.text_id = text_id

    @classmethod
    def from_nltk_book(cls):
        """ Reads the inaugural text from the nltk book as a string. Note that this is a @classmethod
        which will be used instead of the default constructor when creating the object. Remember to
        return cls(something) """

        pass

    @classmethod
    def from_text_file(cls, path, text_id):
        """ Reads the text from given file as a string. Note that this is a @classmethod
        which will be used instead of the default constructor when creating the object.
        Remember to return cls(something) """

        pass

    def get_no_of_sents(self):
        """ Split the input text into sentences and return the length of the text in sentences. """

        pass

    def get_no_of_words(self):
        """ Split the input text into words and return the length of the text in words. """

        pass

    def tokenize_text(self):
        """ Split the text into tokens. Use an nltk method for that, equivalent to s.split() """

        pass

    def lemmatize_token(self, token):
        """ Lemmatize the given token, after converting it to lowercase. """

        pass

    def get_20_most_frequent_words(self):
        """ Return the 20 most frequent words of the text after removing the stopwords and all non-alphanumeric characters
         (in other words, remove all punctuation). Note that the stopwords are stored with their lemmata so you
         will have to make sure you check whether the lemma of each word is contained in the stopwords list.
         Make sure you use the method tokenizeText() that you implemented above """

        pass

    def get_originality_score(self, most_freq_words):
        """ Return the originality score of a text. This score can be measured by counting how many words contained
        in the swadesh list of nltk are also contained in the list with the 20 most frequent words of the text.
        For example, if 10 words can be found in both lists, the originality score is 10.
        The list with the 20 most frequent words should be given to the method as a parameter. """

        pass


if __name__ == '__main__':
    """ Create two instances of the Preprocessor class. One instance should be created through the text file
    ada_lovelace.txt and the other one through the inaugural text included in the nltk book. """

    """ For each instance of the Preprocessor, do the following:
      a) print out the numbers of sentences of the text
      b) print out the 20 most frequent words of the text
      c) print out the originality score of the text. """

    pass
