# Local LLM Chatbot using Ollama and LangChain

This project allows you to interact with a locally downloaded Large Language Model (LLM) using the Ollama platform and LangChain Python library.

## Requirements
- Ollama installed on your system.
- An LLM (like `llama3`) downloaded via Ollama.
- Python 3.6+
- Anaconda for environment management.

## Setup Instructions

1. **Create a new Anaconda environment:**
   ```bash
   conda create --name chatbot_env python=3.6
   conda activate chatbot_env
   ```

2. **Install necessary packages:**
   ```bash
   pip install langchain langchain-ollama ollama
   ```

3. **Ensure Ollama is properly set up:**
   - Download Ollama from the official site.
   - Download a compatible LLM (e.g., `llama3`) using the Ollama CLI:
     ```bash
     ollama pull llama3
     ollama run llama3
     ```

### Key Components:
- **OllamaLLM:** Interacts with the local LLM.
- **ChatPromptTemplate:** Manages the input prompt.
- **Context Management:** Maintains conversation history for context-aware responses.

## Running the Chatbot
1. Ensure Ollama is running and the model is available.
2. Run the Python script:
   ```bash
   python basic_bot.py
   ```
3. Type queries and receive AI-generated responses.
4. Type `exit` to quit the conversation.

## Troubleshooting
- Ensure the `ollama` CLI is correctly installed and the model is available.
- Verify the correct Python environment is activated.

## License
This project is open-source and can be modified as needed.

