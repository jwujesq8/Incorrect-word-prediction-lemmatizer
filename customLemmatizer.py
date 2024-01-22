# import nltk
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import numpy as np


class CustomLemmatizer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def guess_word(self, word):
        word_set = wordnet.synsets(word)

        if word_set:
            word_lemma = word_set[0].lemmas()[0].name()
            return word_lemma
        else:
            similar_word = self.find_similar_word(word)
            if similar_word:
                word_lemma = self.lemmatizer.lemmatize(similar_word)
                return word_lemma
            else:
                return f"not found for {word}"

    def find_similar_word(self, word):
        candidates = self.generate_candidates(word)
        distances_list = [self.levenshtein_distance(word, candidate) for candidate in candidates]
        min_distance_index = np.argmin(distances_list)

        if distances_list[min_distance_index] <= 2:
            min_dist = distances_list[min_distance_index]
            for i, dist in enumerate(distances_list):
                if dist == min_dist:
                    word_to_check_set = wordnet.synsets(candidates[i])
                    if word_to_check_set:
                        return word_to_check_set[0].lemmas()[0].name()
        else:
            return None

    def generate_candidates(self, word):
        keyboard_errors = {
            'a': 'qwsz',
            'b': 'vghn',
            'c': 'xdfv',
            'd': 'erfcxs',
            'e': 'rdsw',
            'f': 'rtgdcv',
            'g': 'tyhbvf',
            'h': 'yujnbg',
            'i': 'uojk',
            'j': 'uikmnh',
            'k': 'iolmj',
            'l': 'opk',
            'm': 'njk',
            'n': 'bhjm',
            'o': 'iklp',
            'p': 'ol',
            'q': 'wa',
            'r': 'edft',
            's': 'awedcxz',
            't': 'rfgy',
            'u': 'yhji',
            'v': 'cfgb',
            'w': 'qesa',
            'x': 'zsdc',
            'y': 'tghu',
            'z': 'asx'
        }
        candidates = list()

        for i, char in enumerate(word):
            for key in keyboard_errors.get(char):
                candidate = list(word)
                candidate[i] = key
                candidates.append(''.join(candidate))

        # for i, char in enumerate(word):
        #     candidate = list(word)
        #     candidate = candidate[:i+1] + list(char) + candidate[i+1:]
        #     candidates.append(''.join(candidate))

        return list(candidates)

    def levenshtein_distance(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        matrix = np.zeros((len1 + 1, len2 + 1))

        for i in range(len1 + 1):
            matrix[i, 0] = i

        for j in range(len2 + 1):
            matrix[0, j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                diff = 0 if word1[i - 1] == word2[j - 1] else 1
                matrix[i, j] = min(matrix[i - 1, j] + 1, matrix[i, j - 1] + 1, matrix[i - 1, j - 1] + diff)

        # print(word1 + " / " + word2)
        # print(matrix)

        return matrix[len1, len2]