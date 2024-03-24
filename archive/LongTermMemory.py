from langchain_core.messages import SystemMessage

from utils.object_factory import get_engine


class LongTermMemory:
    """
    ARCHIVED

    LongTermMemory is a class that stores
    information about the user's past interactions.
    It is called LongTermMemory because it stores
    information about the user's past interactions
    over a long period of time, but it is general
    and do not remember specific details.
    """

    def __init__(self, config):
        self.memory = None
        self.memory_engine = get_engine(config)

    def update(self, input_message, output_message):
        """
        Update the long-term memory with the
        information from the short-term memory.
        """
        messages = [
            SystemMessage(
                "You are an assistant that summarizes the user's past interactions."
            )
        ]
        if self.memory:
            messages.append(self.memory)
        messages.append(input_message)
        messages.append(output_message)

        response = self.memory_engine.invoke(messages)

        self.memory = SystemMessage(content=response.content)

    def get(self):
        """
        Get the long-term memory.
        """
        memory = []
        if self.memory:
            memory.append(self.memory)

        return memory

    def clear(self):
        """
        Clear the long-term memory.
        """
        self.memory = None

    def print(self):
        """
        Print the long-term memory.
        """

        print("--------------------")
        if not self.memory:
            print("The long-term memory is empty.")
        else:
            print(self.memory.content)
        print("--------------------")
