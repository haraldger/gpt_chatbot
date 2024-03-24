import os
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain

from utils.object_factory import get_engine


class KnowledgeBase:
    def __init__(self, config):
        self.gpt_engine = get_engine(config)
        self.knowledge_base = Neo4jGraph(
            url=os.environ["NEO4J_URI"],
            username=os.environ["NEO4J_USERNAME"],
            password=os.environ["NEO4J_PASSWORD"],
        )

        self.knowledge_chain = GraphCypherQAChain.from_llm(
            graph=self.knowledge_base,
            llm=self.gpt_engine,
        )

    def query(self, prompt):
        try:
            response = self.knowledge_chain.run(prompt)
        except ValueError:
            response = "The knowledge base held no information regarding the question."

        return response
