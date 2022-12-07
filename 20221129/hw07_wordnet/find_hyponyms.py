import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet


class HyponymSearcher(object):

    def __init__(self, text_path):

        self.noun_lemmas = []

        # TODO Read text as a string
        with open(text_path, "r") as f:
            text = f.read()

        # TODO Split into sentences: use nltk.sent_tokenize
        sentences = nltk.sent_tokenize(text)

        # TODO Split into tokens: use nltk.word_tokenize
        sentences_tokens = [
            nltk.word_tokenize(
                sentence
            )
            for sentence in sentences
        ]

        # TODO Perform POS tagging on all tokens of all sentences (not on each sentence separately)
        tokens = []
        for sentence in sentences_tokens:
            for token in sentence:
                tokens.append(token)
        tagged_tokens = nltk.pos_tag(tokens)

        # TODO lemmatize nouns (any token whose POS tags starts with "N"): use WordNetLemmatizer()
        lemmatizer = WordNetLemmatizer()

        # TODO determine all noun lemmas and save it in self.noun_lemmas
        for token, tag in tagged_tokens:
            if tag.startswith('N'):
                self.noun_lemmas.append(
                    lemmatizer.lemmatize(token).lower()
                )

    def hypernym_of(self, synset1, synset2):

        # TODO Is synset2 a hypernym of synset 1? (Or the same synset), return True or False

        if synset1 == synset2:
            return True
        synset_1_hypernyms = synset1.hypernyms()
        synset2_hypernyms = synset2.hypernyms()

        for hypernym in synset_1_hypernyms:

            if hypernym in synset2_hypernyms:
                return True

            return self.hypernym_of(hypernym, synset2)

    def get_hyponyms(self, hypernym):

        # TODO determine set of noun lemmas in ada_lovelace.txt that are hyponyms of the given hypernym
        # use the implemented method hypernymOf(self, synset1, synset2)

        hyponyms = set()
        for lemma in self.noun_lemmas:
            for synset in wordnet.synsets(lemma):
                if self.hypernym_of(synset, hypernym):
                    hyponyms.add(lemma)

        return hyponyms
