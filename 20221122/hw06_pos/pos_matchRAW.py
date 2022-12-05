class Sentences:

    def __init__(self, sentences):
        """ Construct an instance of the class Sentence from a list of
        pos-tagged sentences ([[(word,tag),...],...]) """

        self.sentences = sentences

    def __iter__(self):
        return iter(self.sentences)

    def __getitem__(self, i):
        return self.sentences[i]

    @classmethod
    def from_file(cls, path):
        """ Create an instance of the class Sentences from a
        path. Reads the file and pos-tags the sentences in the
        file. [2 point] """

        pass


class PosExpr:

    def __init__(self, expressions):
        """ Construct an instance of the class PosExpr from a list of
        expressions. """

        self.expressions = expressions

    @classmethod
    def from_string(cls, expr):
        """ Create an instance of the class PosExpr from the given
        string. [1 points] """

        pass

    @staticmethod
    def match_expr(expr, pos):
        """ This method returns True if expr matches pos. An expression
        'XX' matches if pos equals 'XX', the expression '*' matches
        any pos and an expression XX* matches if pos starts with 'XX'
        or is equal to 'XX'.  [2 points] """

        pass

    def match_seq(self, sequence):
        """ This method returns a list of matches in the given sequence
        (a sequence here is a list of (word,pos)-pairs -- see following example).
        A match is a list of (word, pos)-pairs, where the tags in the sequence match
        all expressions provided by PosExpr for all possible positions.
        For example: given
        p=PosPattern.from_string("X Y"),
        p.match_seq([(a,X),(b,Y),(c,Z),(d,X),(e,Y))])
        should return the following list of lists:
        [[(a,X),(b,Y)],[(d,X),(e,Y)]].  [3 points] """

        pass

    @staticmethod
    def find_str(sentences, expr):
        """ Return a list of strings that match the given expression.
        E.g. find_str(sentences, "JJ NN") should return the list
        [...,"prior year",...].  [2 points] """

        pass
