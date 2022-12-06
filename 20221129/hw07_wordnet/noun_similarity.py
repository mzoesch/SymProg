import nltk
from nltk.corpus import wordnet as wn


def get_similarity_scores(pairs):

    results = []  # (pair, score)

    for pair in pairs:

        max_score = 0.0
        max_line = ()

        # TODO 1. iterate over all combinations of synsets formed by the synsets of the words in the word pair
        # TODO 2. determine the maximum similarity score
        # TODO 3. save max_line in results in form ("word1-word2", similarity_value) e.g.('car-automobile', 1.0)

        word1, word2 = pair

        for synset1 in wn.synsets(word1):
            for synset2 in wn.synsets(word2):
                score = synset1.path_similarity(synset2)

                if score is not None and score > max_score:
                    max_score = score
                    max_line = (f"{word1}-{word2}", score)

        results.append(max_line)
        # pass

    # TODO 4. return results in order of decreasing similarity

    results.sort(key=lambda x: x[1], reverse=True)
    return results
