from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os
import math
from collections import Counter


def dot(dict_a, dict_b):
    return sum([dict_a.get(tok) * dict_b.get(tok, 0) for tok in dict_a])


def normalized_tokens(text):
    return [token.lower() for token in word_tokenize(text)]


class TextDocument:
    def __init__(self, text, id=None, category=None):
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id
        self.category = category

    @classmethod
    def from_file(cls, filename, category):
        with open(filename, 'r', encoding="ISO-8859-1") as myfile:
            text = myfile.read().strip()
        return cls(text, filename, category)


class DocumentCollection:
    def __init__(self, term_to_df, term_to_docids, docid_to_doc, doc_to_category):
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc
        # TextDocument to category
        self.doc_to_category = doc_to_category

    @classmethod
    def from_dir(cls, dir):
        files = [(os.path.join(root, name), os.path.relpath(root, dir))
                 for root, dirs, f in os.walk(dir, topdown=False) for name in f]
        docs = [TextDocument.from_file(f, cat) for f, cat in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        doc_to_category = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            doc_to_category[doc] = doc.category
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc, doc_to_category)

    def tfidf(self, counts):
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N/self.term_to_df[tok]) for tok, tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, weighted_a, weighted_b):
        dot_ab = dot(weighted_a, weighted_b)
        norm_a = math.sqrt(dot(weighted_a, weighted_a))
        norm_b = math.sqrt(dot(weighted_b, weighted_b))
        if norm_a == 0 or norm_b == 0:
            return 0
        else:
            return dot_ab / (norm_a * norm_b)


class KNNClassifier:
    def __init__(self, n_neighbors=1):
        self.n_neighbors = n_neighbors
        self.doc_collection = None
        self.vectorsOfDoc_collection = None

    def fit(self, doc_collection):
        self.doc_collection = doc_collection
        self.vectorsOfDoc_collection = [(doc, self.doc_collection.tfidf(doc.token_counts))
                                        for doc in self.doc_collection.docid_to_doc.values()]

    def calculate_similarities(self, vec_test_doc, vectors_of_train_docs):
        # TODO calculate similarities between test and train documents and label
        # TODO them [(similarity, label),...] # -> ok
        # TODO have a look at the unittest to see what is the type of vectorsOfTrainDocs

        # pass

        similarities = []
        for vec_train_doc in vectors_of_train_docs:
            similarities.append(
                (
                    self.doc_collection.cosine_similarity(
                        vec_test_doc, vec_train_doc[1]
                    ),
                    vec_train_doc[0].category
                )
            )

        return similarities

    def order_nearest_to_farthest(self, similarities):
        # TODO order the labeled points from nearest to farthest # -> ok

        # pass

        return sorted(
            similarities,
            key=lambda x: x[0],
            reverse=True
        )

    def labels_k_closest(self, sorted_similarities):
        # TODO find the labels for the k closest points # -> ok

        # pass

        return [
            x[1]
            for x in sorted_similarities[
                :self.n_neighbors
            ]
        ]

    def choose_one(self, labels):
        # TODO reduce k until you find a unique winner  # -> ok

        # pass

        return Counter(labels).most_common(1)[0][0]

    def classify(self, test_file):
        # TODO classify test document, have a look at the slides of the course for some help with the order of commands # -> ok
        # test_doc = TextDocument.from_file(test_file, 'unknowcat')

        # pass

        return self.choose_one(
            self.labels_k_closest(
                self.order_nearest_to_farthest(
                    self.calculate_similarities(
                        self.doc_collection.tfidf(
                            TextDocument.from_file(
                                test_file,
                                'unknowcat'
                            ).token_counts
                        ),
                        self.vectorsOfDoc_collection
                    )
                )
            )
        )

    def get_accuracy(self, gold, predicted):
        # TODO calculate accuracy # -> ok

        # pass

        return sum(
            [
                1
                for x, y in zip(
                    gold, predicted
                )
                if x == y
            ]
        ) / len(gold) * 100
