from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os
import math
from os.path import basename


# Write test for this function -> ok
def dot(dict_a, dict_b):
    """
    >>> dot({'a': 1, 'b': 2}, {'a': 2, 'b': 1})
    4
    """

    return sum(
        [
            dict_a.get(tok) * dict_b.get(tok, 0)
            for tok in dict_a
        ]
    )


# Write test for this function -> ok
def normalized_tokens(text):
    """
    >>> normalized_tokens('The cat sat on a mat.')
    ['the', 'cat', 'sat', 'on', 'a', 'mat', '.']
    """

    return [
        token.lower()
        for token in word_tokenize(text)
    ]


class TextDocument:

    def __init__(self, text, id=None):

        # TODO: Exercise 3.2, remove line breaks (see unittest for example) # -> ok

        self.text = text
        self.text = self.text.replace('-\n', '')
        self.text = self.text.replace('\n', ' ')

        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id

    @classmethod
    def from_file(cls, filename):

        with open(filename, 'r') as myfile:
            text = myfile.read().strip()

        return cls(
            text, basename(filename)
        )


class DocumentCollection:

    def __init__(self, term_to_df, term_to_docids, docid_to_doc):

        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc

    @classmethod
    def from_dir(cls, directory, file_suffix):

        files = [
            (directory + '/' + f)
            for f in os.listdir(directory)
            if f.endswith(file_suffix)
        ]

        docs = [
            TextDocument.from_file(f)
            for f in files
        ]

        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):

        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()

        for doc in docs:
            docid_to_doc[doc.id] = doc
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)

        return cls(
            term_to_df, term_to_docids, docid_to_doc
        )

    def docs_with_all_tokens(self, tokens):
        docids_for_each_token = [
            self.term_to_docids[token]
            for token in tokens
        ]
        docids = set.intersection(*docids_for_each_token)

        return [
            self.docid_to_doc[_id]
            for _id in docids
        ]

    def docs_with_some_tokens(self, tokens):

        # pass  # TODO: Exercise 3.3 # -> ok

        docids_for_each_token = [
            self.term_to_docids[token]
            for token in tokens
        ]
        docids = set.union(*docids_for_each_token)

        return [
            self.docid_to_doc[_id]
            for _id in docids
        ]

    def tfidf(self, counts):
        N = len(self.docid_to_doc)

        return {
            tok: tf * math.log(N / self.term_to_df[tok])
            for tok, tf in counts.items()
            if tok in self.term_to_df
        }

    def cosine_similarity(self, doc_a, doc_b):
        """ Make the existing test pass by changing the functionality of this function. """

        # TODO: Exercise 3.1 # -> ok

        tfidf_a = self.tfidf(doc_a.token_counts)
        tfidf_b = self.tfidf(doc_b.token_counts)

        if not tfidf_a or not tfidf_b:
            return 0
        if math.sqrt(dot(tfidf_a, tfidf_a)) == 0 or math.sqrt(dot(tfidf_b, tfidf_b)) == 0:
            return 0

        return dot(tfidf_a, tfidf_b) / (
            math.sqrt(dot(tfidf_a, tfidf_a)) * math.sqrt(dot(tfidf_b, tfidf_b))
        )


class SearchEngine:

    def __init__(self, doc_collection):
        self.doc_collection = doc_collection

    def ranked_documents(self, query):
        query_doc = TextDocument(query)
        query_tokens = query_doc.token_counts.keys()

        # TODO: Exercise 3.3 (replace docs_with_all_tokens with your implementation
        # TODO: of docs_with_some_tokens) # -> ok

        # docs = self.doc_collection.docs_with_all_tokens(query_tokens)
        docs = self.doc_collection.docs_with_some_tokens(query_tokens)

        docs_sims = [
            (
                doc, self.doc_collection.cosine_similarity(
                    query_doc, doc
                )
            )
            for doc in docs
        ]

        return sorted(
            docs_sims, key=lambda x: -x[1]
        )

    def snippets(self, query, document, window=50):

        text = document.text

        # TODO: Exercise 3.4 # -> ok

        if query in text:

            start = text.find(query)
            if start == -1:
                return

            end = start + len(query)
            line = f'...{text[start - window:start]}[{text[start:end]}]{text[end:end + window]}...'

            yield line
            return

        query_tokens = normalized_tokens(query)
        for token in query_tokens:
            start = text.lower().find(token.lower())

            if -1 == start:
                continue

            end = start + len(token)
            line = f'...{text[start - window:start]}[{text[start:end]}]{text[end:end + window]}...'

            yield line

        return
