"""Keyword-based message classification and starting words."""

CATEGORIES = {
    "greeting": {"hello", "hi", "hey", "good morning", "good afternoon"},
    "farewell": {"bye", "goodbye", "see you", "later"},
    "thanks": {"thanks", "thank you", "thx"},
    "weather": {"weather", "rain", "sunny", "snow", "forecast"},
    "time": {"time", "clock", "date"},
    "name": {"your name", "who are you"},
}

START_WORDS = {
    "greeting": "hello",
    "farewell": "goodbye",
    "thanks": "you",
    "weather": "the",
    "time": "the",
    "name": "i",
    "question": "i",
    "statement": "tell",
}


def classify_message(message: str) -> str:
    msg = message.lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in msg:
                return category
    if msg.strip().endswith("?"):
        return "question"
    return "statement"


def start_word(category: str) -> str:
    return START_WORDS.get(category, "i")
