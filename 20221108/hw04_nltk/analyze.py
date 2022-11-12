from nltk import FreqDist
from nltk import word_tokenize
import nltk


class Analyzer(object):

    def __init__(self, path):
        """ reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution """

        # TODO the list of words from text file -> ok
        with open(path, 'r') as f:
            self.text = f.read()
        self.w_tokens: list[str] = nltk.word_tokenize(self.text)
        self.w_types: set[str] = set(self.w_tokens)

        # TODO frequency distribution of words from text file -> ok
        self.frequency: dict = FreqDist(self.w_tokens)

        # pass

    def numberOfTokens(self):  # Number of tokens
        """ returns number of tokens in the text """  # -> ok

        # pass
        return len(self.w_tokens)

    def vocabularySize(self):  # Number of types
        """ returns the size of the vocabulary of the text """  # -> ok

        # pass
        return len(set(self.w_tokens))

    def lexicalDiversity(self):
        """ returns the lexical diversity of the text """  # -> ok

        # pass
        #
        # return len(set(self.w_tokens)) / len(self.w_tokens)
        # number of tokens / number of types
        # but in script: number of types / number of tokens ??
        return self.numberOfTokens() / self.vocabularySize()

    def getKeywords(self):
        """ return words as possible key words, that are longer than seven characters,
        that occur more than seven times (sorted alphabetically) """  # -> ok

        # pass
        return sorted(  # Built in: sorts alphabetically
            [
                word
                for word in self.w_types
                if len(word) > 7 and self.frequency[word] > 7
            ]
        )

    def numberOfHapaxes(self):
        """ returns the number of hapaxes in the text """  # -> ok

        # pass
        return len(self.frequency.hapaxes())

    def avWordLength(self):
        """ returns the average word length of the text """

        # pass
        # why 6 ??
        return sum([len(w) for w in self.w_tokens]) // self.numberOfTokens()

    # def topSuffixes(self):
    #     '''returns the 10 most frequent 2-letter suffixes in words
    #         (restrict to words of length 5 or more -- insertion order if same frequency)'''
    #     pass

    # def topPrefixes(self):
    #     '''returns the 10 most frequent 2-letter prefixes in words
    #         (restrict to words of length 5 or more -- insertion order if same frequency)'''
    #     pass

    # def tokensTypical(self):
    #     '''returns first 5 tokens of the (alphabetically sorted) vocabulary
    #     that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
    #     and topSuffixes(), Prefixes and Suffixes are 2 characters long.'''
    #     pass
