import sys
import dotenv

from config import get_config
from ChatBot import ChatBot


def run(config):
    chat_bot = ChatBot(config)

    print("Ask your questions to the movie chatbot.")
    print("Type 'exit' to exit the program, type 'memory' to print the memory.")
    while True:
        message = input("You: ")

        if message == "exit":
            sys.exit(0)

        response = chat_bot.chat(message)
        print("Bot:", response)


def main():
    # Configure the environment
    dotenv.load_dotenv()
    config = dict()
    config.update(get_config())

    # Run the program
    run(config)


if __name__ == "__main__":
    main()
