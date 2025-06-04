"""Core SmallChat chatbot implementation."""
import os
from pathlib import Path

from .decision_tree import classify_message, start_word
from .bigram_model import BigramModel
from .english_rules import sanitize_sentence


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "data.txt"


def _get_bot_name():
    return os.getenv("BOT_NAME", "SmallChat")


class SmallChat:
    """Simple logic-based chatbot."""

    def __init__(self):
        self.bot_name = _get_bot_name()
        self.model = BigramModel()
        self._load_corpus()

    def _load_corpus(self):
        corpus = [
            "hello how are you",
            "i am fine",
            "how can i help you",
            "feel free to ask questions",
        ]
        if DATA_FILE.exists():
            with DATA_FILE.open() as f:
                corpus.extend(line.strip().lower() for line in f if line.strip())
        self.model.update(corpus)

    def respond(self, message: str) -> str:
        """Generate a response based on the input message."""
        if not message:
            return ""  # empty input

        msg_type = classify_message(message)
        start = start_word(msg_type)

        self.model.update([message.lower()])
        sentence = self.model.generate(start, max_length=12)
        clean = sanitize_sentence(sentence)
        return clean.capitalize()
