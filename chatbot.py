from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the conversation template
template = """
Answer the Question Below.
Here is the Convo History: {context}
Question: {question}
Answer:
"""

# Initialize the model and prompt
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""  # Initialize conversation history
    print("Welcome to nanoVoltz's ChatBot. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Invoke the chain with current context and user input
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)
        
        # Update context with the latest exchange
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
