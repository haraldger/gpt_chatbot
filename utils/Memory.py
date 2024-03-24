from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts import (
    PromptTemplate,
)

from utils.object_factory import get_engine


class Memory:
    def __init__(self, config):
        self.gpt_engine = get_engine(config)
        self.memory = ConversationSummaryBufferMemory(
            llm=self.gpt_engine,
            max_token_limit=config["memory_size"],
            memory_key="chat_history",
        )

        self.prompt_template = PromptTemplate.from_template(
            """
            {chat_history}
            """
        )

    def update_memory(self, input_message, response):
        self.memory.save_context({"input": input_message}, {"output": response})

    def get_prompt(self):
        chat_context = self.memory.load_memory_variables({})["chat_history"]
        prompt = self.prompt_template.format(chat_history=chat_context)
        return prompt
