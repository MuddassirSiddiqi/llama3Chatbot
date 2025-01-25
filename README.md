# nanoVoltz's ChatBot

Welcome to nanoVoltz's ChatBot, an interactive chatbot that leverages LangChain and OllamaLLM for conversational AI. This guide will help you set up, run, and understand the code.

## Features
- Utilizes LangChain for managing conversational flows.
- Leverages OllamaLLM (llama3 model) for generating AI responses.
- Tracks conversation history for context-aware answers.

---

## Installation Guide

1. Clone the repository or copy the code into a new project folder.
2. Ensure you have Python 3.8+ installed.
3. Install a virtual environment and dependencies:

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# For Windows:
./env/Scripts/activate
# For macOS/Linux:
source env/bin/activate

# Install required Python packages
pip install langchain_core langchain_ollama
```

4. Ensure the Ollama model `llama3` is available in your system or configured in Ollama.

---

## Running the Chatbot

1. Activate the virtual environment:

```bash
# For Windows:
./env/Scripts/activate
# For macOS/Linux:
source env/bin/activate
```

2. Run the script:

```bash
python chatbot.py
```

3. Interact with the chatbot by typing questions. Type `exit` to quit.

---

## Code Explanation

### Imports

```python
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
```
- `OllamaLLM`: Handles the AI model (llama3).
- `ChatPromptTemplate`: Structures the conversation prompt.

### Conversation Template

```python
template = """
Answer the Question Below.
Here is the Convo History: {context}
Question: {question}
Answer:
"""
```
Defines how the chatbot combines conversation history and user input into a prompt for the model.

### Model and Prompt Initialization

```python
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
```
- `OllamaLLM(model="llama3")`: Loads the llama3 model.
- `prompt | model`: Creates a chain to process prompts through the model.

### Conversation Handling

```python
def handle_conversation():
    context = ""  # Initialize conversation history
    print("Welcome to nanoVoltz's ChatBot. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Invoke the chain with current context and user input
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)
        
        # Update context with the latest exchange
        context += f"\nUser: {user_input}\nAI: {result}"
```
- `context`: Tracks conversation history to maintain context.
- `chain.invoke`: Processes the user query and fetches the response.
- Updates `context` to include the latest interaction.

### Main Function

```python
if __name__ == "__main__":
    handle_conversation()
```
- Starts the chatbot loop when the script is executed directly.

---

Feel free to customize and expand the chatbot to meet your needs. Happy coding!
