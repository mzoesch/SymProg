import nltk


class LangModeler(object):

    def __init__(self, languages, words):
        self.languages, self.words = languages, words

    def build_language_models(self):
        # TODO return ConditionalFrequencyDistribution of words
        # TODO in the UDHR corpus conditioned on each language # -> ok
        # hint: use nltk.ConditionalFreqDist

        # pass
        return nltk.ConditionalFreqDist((lang, word.lower())
                                        for lang in self.languages
                                        for word in self.words[lang]
                                        )

    def guess_language(self, language_model_cfd, text):
        """Returns the guessed language for the given text"""

        # TODO for each language calculate the overall score of a given text # -> ok
        # based on the frequency of words accessible by
        # language_model_cfd[language].freq(word) and then
        # identify most likely language for a given text according to this score

        # pass
        return max(  # Lang with highest score
            [
                (
                    self.languages[
                        i
                    ],
                    sum(language_model_cfd[
                        self.languages[
                            i
                        ]
                    ].freq(
                        w
                    )
                        for w in text.
                        lower().
                        split()
                    )
                )
                for i in range(
                    len(
                        self.languages
                    )
                )
            ],
            key=lambda search: search[
                1
            ]
        )[
            0
        ]
