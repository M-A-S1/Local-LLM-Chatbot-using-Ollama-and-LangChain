# Make new environment using anaconda
# Open VS code and in the conda environment type  "pip install langchain langchain-ollama ollama" in terminal

from langchain_ollama import OllamaLLM                  #importing Ollama LLM
from langchain_core.prompts import ChatPromptTemplate   #importing langchain chap prompt to pass prompt to LLM

#This is our template which we pass to the model it will have previous context and the current question
template = """                      
Answer the question below. 

Here is the conversation history: {context}

Question: {question}

Answer:

"""

model = OllamaLLM(model="llama3")                       # Our model is equal to the LLM we are using Llama in this case
prompt = ChatPromptTemplate.from_template(template)     # we pass the template we define above into the chat prompt 
chain = prompt | model                                  # Here we chain our prompt and the model meaning prompt is send to model where it is invoked automaticaaly

def handle_conversation():                                      # Defining function to handle conversation with bot
    context = ""                                                # Context is empty in start
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:                                                 # Stays in while loop until exit is pressed
        user_input = input("You: ")                             # Get user input/query
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context,"question": user_input})  # we call the model/LLM it gets any previous context and the current user query as input
        print("Bot: ", result)                                              # LLMs response is printed 
        context += f"\nUser: {user_input}\nAI: {result}"                    # user input and LLMs response is stored as context 


if __name__ == "__main__":
    handle_conversation()