**Dependencies**

Required dependencies and packages are provided in `requirements.txt`. To install these, navigate (`cd`) into the root directory of the project, and create a python virtual environment:
```
python -m venv .venv
source .venv/bin/activate
```
Verify that the environment is clean:
```
pip freeze
```
The command should not return anything.

Using pip, install the required dependencies:
```
pip install --upgrade -r requirements.txt
```
Run `pip freeze` again to verify that the packages have all been installed.

**Configure the environment**

Some environment variables are necessary - these should be placed in a file named `.env` in the root directory of the project. Create the file with `touch .env`.

The following template should be used for the env file, please configure it as such and provide all the necessary environment variables:

```
NEO4J_URI=<Your Neo4j URI>
NEO4J_USERNAME=<Your Neo4j Username>
NEO4J_PASSWORD=<Your Neo4j Password>
AURA_INSTANCEID=<Your Neo4j Aura Instance ID>
AURA_INSTANCENAME=<Your Neo4j Aura Instance Name>
OPENAI_API_KEY=<Your OpenAI API Key>
```

**Executing the program**

Execution is as easy as running `main.py` from the root directory:
```
python main.py
```

**Additional configuration**

Additional configuration parameters can be found in the file `config.py` in the root directory. To change these, simply edit the values at the top of the file. For example, you can change the LLM that is being used (currently GPT 3.5 Turbo) or the size of the memory. The memory is currently set to 500 tokens, which is a relatively small value. Increasing it will give the Chat Bot more detailed context and a longer memory.


**Navigation and System Design**

The `main.py` file handles the main execution flow of the application. It instantiates all the required objects and runs the chat bot. 

The class `ChatBot` (found in `ChatBot.py`) is the main structure that controls the user's interaction with the LLMs. It consists of a memory to log the user's past interaction, and a KnowledgeBase object. The knowledge base takes prompts and queries the Neo4j database to retrieve information about movies and actors. The ChatBot object is responsible for linking the memory and the database LLM, and performs some prompt engineering to get accurate responses. It makes sure that the user gets accurate information from the database (avoiding model hallucination) while keeping a memory such that the chat bot remembers the past interactions with the user, and can use the context of the conversation to create more aligned responses. The memory makes the user's interaction feel like a conversation, where previous messages are implicitly used to guide the responses - for example, if the user has been talking about Tom Cruise, they can ask "Which one is his most popular movie?" and wouldn't have to rephrase the question as "Which one is Tom Cruise's most popular movie?" every time they ask a new question.

The utility class `Memory.py` is used to encapsulate the memory functionality and some processing related to it. It is implemented as a summarization-buffer memory, acting as both a long-term and as a short-term memory. Recent conversation is retained in exact detail, while a (LLM-powered) summary is maintained of the entire conversation as a long-term memory.

`KnowledgeBase.py` is another utility class, and is perhaps the most important component of the chat bot. It is the LLM that generates the Cypher queries that interact with the Neo4j database, and retrieves data to answer the user's questions. The knowledge base is not inherently aware of the context, including past interactions, but takes only a prompt and generates an informed response. If context is provided in the input prompt, it is able to use this context to generate responses conditioned on the history. It is the `ChatBot` object that is responsible for providing this context, through some simple prompt engineering.
