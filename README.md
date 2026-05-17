# Stateful Agentic AI Chatbot

An end-to-end stateful, agentic AI application built using LangGraph, LangChain, and Streamlit. This project provides multiple AI use cases including a basic chatbot, a tool-augmented chatbot capable of web searches, and an automated AI news summarization pipeline.

## Features

- **Basic Chatbot**: A simple, conversational AI interface using Groq LLMs.
- **ChatBot with Web Search**: An agentic chatbot augmented with the Tavily search tool, capable of searching the web to provide up-to-date and context-aware responses.
- **AI News Summarizer**: A workflow that fetches recent AI news, summarizes the content, and saves the results directly to the filesystem.
- **Interactive UI**: Built with Streamlit for a clean, user-friendly web interface.
- **Stateful Workflows**: Leverages LangGraph (`StateGraph`) to manage complex, multi-node agentic workflows with persistent state across interactions.

## Tech Stack

- **Frameworks**: LangGraph, LangChain, Streamlit
- **LLM Provider**: Groq
- **Tools API**: Tavily (Web Search)
- **Vector Store (Optional)**: FAISS
- **Language**: Python 3.10+

## Project Structure

```text
c:\stateful agentic\
├── app.py                  # Entry point for the Streamlit application
├── requirements.txt        # Python dependencies
├── AINews/                 # Directory where AI news summaries are saved
└── src/langgraphagenticai/
    ├── graph/              # LangGraph StateGraph builders
    ├── LLMS/               # LLM model configuration and setup (Groq)
    ├── nodes/              # Execution nodes for different agentic workflows
    ├── state/              # Application state definition
    ├── tools/              # Tools integration (e.g., Search tool)
    └── ui/                 # Streamlit UI logic (Load UI, Display Results)
```

## Setup and Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   cd "stateful agentic"
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Ensure you have your API keys configured for Groq and Tavily. You can set these in your environment or a `.env` file (if implemented).
   - `GROQ_API_KEY`
   - `TAVILY_API_KEY`

## How to Run

Start the Streamlit application by running the following command:

```bash
streamlit run app.py
```

Select your desired use case from the Streamlit UI sidebar and interact with the stateful AI agent!