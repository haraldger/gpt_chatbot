from archive.LongTermMemory import LongTermMemory
from archive.ShortTermMemory import ShortTermMemory


class LTSTMemory:
    """
    ARCHIVED

    LTSTMemory is a class that stores
    information about the user's past interactions.
    LTST means long-term short-term memory, and the memory
    stores information about the user's past interactions
    over a long period of time summarized, but it also stores
    information about the user's past interactions
    over a short period of time in great detail..
    """

    def __init__(self, config):
        self.long_term_memory = LongTermMemory(config)
        self.short_term_memory = ShortTermMemory(config)

    def update(self, input_message, output_message):
        """
        Update the long-term and short-term memory with the
        new input and output messages.
        """
        self.long_term_memory.update(input_message, output_message)
        self.short_term_memory.update(input_message, output_message)

    def get(self):
        """
        Get the long-term short-term memory.
        """
        memory = []
        memory += self.long_term_memory.get()
        memory += self.short_term_memory.get()

        return memory

    def clear(self):
        """
        Clear the long-term and short-term memory.
        """
        self.long_term_memory.clear()

    def print(self):
        """
        Print the long-term and short-term memory.
        """
        print("Long-term memory:")
        self.long_term_memory.print()
        print()
        print("Short-term memory:")
        self.short_term_memory.print()
