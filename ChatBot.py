from langchain.prompts import (
    PromptTemplate,
)

from utils.object_factory import get_engine
from utils.Memory import Memory
from utils.KnowledgeBase import KnowledgeBase


class ChatBot:
    def __init__(self, config):
        self.gpt_engine = get_engine(config)
        self.knowledge_base = KnowledgeBase(config)
        self.memory = Memory(config)

        self.prompt_template = PromptTemplate.from_template("""{system_context}\n{chat_history}\nHuman: {human_input}""")
        self.prompt_template = self.prompt_template.partial(system_context=config["system_context"])

    def chat(self, input_message):
        # Get the memory context
        chat_context = self.memory.get_prompt()

        prompt = self.prompt_template.format(
            chat_history=chat_context, human_input=input_message
        )

        # Query the knowledge base
        response = self.knowledge_base.query(prompt)

        # Update the memory
        self.memory.update_memory(input_message, response)

        return response
