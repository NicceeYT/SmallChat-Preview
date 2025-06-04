# SmallChat Preview

SmallChat Preview is a simple, logic-based chatbot that responds to messages without using neural networks or machine learning. Instead, it uses smart decision trees and word prediction to hold conversations that feel natural and helpful.

## How It Works

1. **Message Analysis:**  
   When you send a message, SmallChat analyzes it using a decision tree. It figures out what type of message you sent (like a greeting, question, etc.), pulls out important details, and decides how it should respond.

2. **Building the Reply:**  
   Based on its analysis, the chatbot gathers a set of helpful phrases and filters out anything that wouldn’t make sense in a reply. It also considers hints or instructions for what to say or avoid.

3. **Word Prediction:**  
   SmallChat uses a database that tracks which words usually come after each other, using two sources:  
   - Example conversations built into the system  
   - Words and phrases it has learned from your recent messages  
   The bot starts with a chosen word and builds a sentence by picking the most likely next word each time, making sure the reply stays grammatically correct and logical.

4. **Final Response:**  
   The generated sentence is checked for proper English and then sent back to you as the chatbot’s response.

## Features

- Fast, logic-based message processing
- No neural networks or deep learning required
- Learns patterns from your conversations in real time
- Uses simple word prediction to generate smooth sentences
- Easy to customize and expand

## Data and Privacy

SmallChat Preview stores word patterns and message examples only for the current chat session. It does **not** use or require large datasets, and all learning happens on-the-fly, keeping things light and fast.

## Getting Started

1. **Clone or download this repository**
2. **Run `main.py`** (or the entry file for your programming language)
3. **Start chatting!** Type your message and see SmallChat reply instantly.

## Usage Example

```python
from smallchat import SmallChat

# Initialize the chatbot
chatbot = SmallChat()

print("SmallChat Preview\nType 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        break
    response = chatbot.respond(user_input)
    print("SmallChat:", response)
```

## Contributing

Contributions, suggestions, and improvements are welcome! Please open an issue or submit a pull request.

## Disclaimer

This is a preview version, so some responses may not always be perfect. Feedback is appreciated!

## Development Setup

1. Copy `.env.example` to `.env` and adjust any variables you need.
2. Run `./setup.sh` to create a Python virtual environment and install dependencies.
3. Launch the chatbot with `python main.py`.

## Training Data

SmallChat automatically loads extra training sentences from `data/data.txt`. You can add any text to this file to influence the word prediction model.

## English Rules

Generated text is filtered using simple heuristics defined in `smallchat/english_rules.py` to remove repeated or invalid words.
