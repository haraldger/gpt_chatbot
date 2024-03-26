import sys
import dotenv
import warnings

from config import get_config
from ChatBot import ChatBot

warnings.filterwarnings("ignore")


def run(config):
    chat_bot = ChatBot(config)

    print("Type 'exit' to exit the program.")
    print("Hello. I am a movie expert, here to help you with any questions you have about movies. Ask me anything relating to movies, actors, directors, ratings or plots. I can tell you about complex relationships between these, such as how many movies an actor has starred in, or what directors worked with a co-star of an actor.")
    while True:
        message = input("You: ")

        if message == "exit":
            sys.exit(0)

        response = chat_bot.chat(message)
        print("Bot:", response)
        print()


def main():
    # Configure the environment
    dotenv.load_dotenv()
    config = dict()
    config.update(get_config())

    # Run the program
    run(config)


if __name__ == "__main__":
    main()
