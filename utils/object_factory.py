from langchain_openai import ChatOpenAI


def get_engine(config):
    return ChatOpenAI(model=config["model"])
