class ShortTermMemory:
    """
    ARCHIVED

    Short-term memory for the chatbot.
    The short-term memory stores the user's
    past interactions over a short period of time.
    It remembers the user's interactions in great detail,
    but it does not remember the user's past interactions
    that happened a long time ago.
    """

    def __init__(self, config):
        self.memory_size = config["memory_size"]
        self.input_memory = []
        self.output_memory = []

    def update(self, input_message, output_message):
        if len(self.input_memory) >= self.memory_size:
            self.input_memory.pop(0)
            self.output_memory.pop(0)

        self.input_memory.append(input_message)
        self.output_memory.append(output_message)

    def get(self):
        memory = []
        for idx in range(self.memory_size):
            if idx < len(self.input_memory):
                memory.append(self.input_memory[idx])
                memory.append(self.output_memory[idx])
            else:
                break

        return memory

    def clear(self):
        self.input_memory = []
        self.output_memory = []

    def print(self):
        print("--------------------")
        for idx in range(self.memory_size):
            print(f"Memory index: {idx}")
            if idx < len(self.input_memory):
                print(f"Input: {self.input_memory[idx].content}")
                print(f"Output: {self.output_memory[idx].content}")
            else:
                print(f"Input memory length: {len(self.input_memory)}")
                print(f"Output memory length: {len(self.output_memory)}")
                break
        print("--------------------")
