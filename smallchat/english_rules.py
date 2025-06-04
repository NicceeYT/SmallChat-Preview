"""Utilities for filtering generated text using simple English rules."""
import re

COMMON_WORDS = {
    "the",
    "i",
    "you",
    "and",
    "a",
    "an",
    "to",
    "is",
    "are",
    "it",
    "in",
    "for",
    "on",
    "of",
    "with",
    "that",
    "this",
    "there",
    "be",
    "hello",
    "hi",
    "how",
    "what",
    "why",
    "can",
    "help",
    "me",
    "do",
}


def _filter_words(words):
    cleaned = []
    for w in words:
        w = re.sub(r"[^a-zA-Z]", "", w)
        if not w:
            continue
        if len(w) > 20:
            continue
        if len(set(w)) == 1 and len(w) > 2:
            continue
        cleaned.append(w)
    return cleaned


def sanitize_sentence(sentence: str) -> str:
    """Remove obviously invalid words from a sentence."""
    words = sentence.split()
    filtered = _filter_words(words)
    result = []
    for w in filtered:
        if result and result[-1] == w:
            continue
        result.append(w)
    return " ".join(result)
