MEMORY_SIZE = 500
MODEL = "gpt-3.5-turbo"

SYSTEM_CONTEXT = """System: You are a movie expert that helps customers with information about movies and actors."""


def get_config():
    return {
        "memory_size": MEMORY_SIZE,
        "model": MODEL,
        "system_context": SYSTEM_CONTEXT,
    }
