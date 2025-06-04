"""Very small bigram-based word prediction."""
from collections import defaultdict, Counter
import random


class BigramModel:
    def __init__(self):
        self.bigrams = defaultdict(Counter)

    def update(self, sentences):
        for sentence in sentences:
            words = sentence.strip().lower().split()
            for i in range(len(words) - 1):
                self.bigrams[words[i]][words[i + 1]] += 1

    def next_word(self, word):
        choices = self.bigrams.get(word)
        if not choices:
            return None
        return max(choices, key=choices.get)

    def generate(self, start_word, max_length=10):
        words = [start_word]
        while len(words) < max_length:
            next_w = self.next_word(words[-1])
            if not next_w:
                break
            words.append(next_w)
        return " ".join(words)
