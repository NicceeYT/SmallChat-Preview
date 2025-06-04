from smallchat import SmallChat

if __name__ == "__main__":
    bot = SmallChat()
    print("SmallChat Preview\nType 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        response = bot.respond(user_input)
        print("SmallChat:", response)
