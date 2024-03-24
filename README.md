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
