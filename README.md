# Stateful Agentic AI Framework

A production-grade, stateful AI orchestration framework built to design, test, and deploy multi-agent workflows using LangGraph and LangChain. 

This repository provides a modular, graph-based architecture that enables the creation of robust AI agents capable of state management, tool integration (e.g., search, retrieval), and context-aware interactions.

## Problem Statement

Developing autonomous AI agents often leads to complex spaghetti code when managing conversational context, tool execution, and dynamic decision-making. This project solves this by abstracting agent workflows into directed graphs, ensuring predictable execution, seamless state persistence, and scalable integration with external tools and LLMs.

## Features

* **Stateful Workflows**: Leverages LangGraph to maintain context across multi-turn conversational sequences.
* **Graph-Based Orchestration**: Implements deterministic agent execution paths using directed graphs.
* **Dynamic Tool Calling**: Seamlessly integrates external capabilities, such as web search (Tavily) and custom utilities, directly into the agent's decision loop.
* **Multi-Node Architecture**: Supports various agent personas and functionalities (e.g., Basic Chatbot, Tool-Augmented Agent, AI News Summarizer).
* **Interactive UI**: Includes a fully featured Streamlit interface for real-time agent interaction and testing.
* **LLM Agnostic**: Abstracted LLM integration, currently configured for high-speed inference via Groq.

## Architecture

The system is built on a highly modular architecture emphasizing separation of concerns:

1.  **State Management (`state.py`)**: Defines the shared state schema passed between nodes in the graph, ensuring all agent actions have access to the latest context.
2.  **Nodes (`nodes/`)**: Isolated execution units (e.g., `ai_news_node.py`, `chatbot_with_Tool_node.py`) that perform specific tasks or LLM invocations based on the current state.
3.  **Graph Builder (`graph_builder.py`)**: The orchestration layer that connects nodes, defines conditional edges, and compiles the final LangGraph runnable based on the selected use case.
4.  **Tools (`tools/`)**: Modular external utilities (like `search_tool.py`) that agents can invoke dynamically.
5.  **UI Layer (`ui/`)**: A Streamlit application handling user inputs, configuration, and real-time streaming of agent responses.

## Workflow

1.  **Initialization**: The user accesses the Streamlit UI, configures the LLM parameters, and selects an agent use case.
2.  **Graph Compilation**: The `GraphBuilder` constructs the LangGraph workflow based on the chosen use case, linking the appropriate nodes and tools.
3.  **Execution**: User input is injected into the initial state. The graph processes the state, routing it through necessary nodes (e.g., reasoning, tool execution, final synthesis).
4.  **Response Generation**: The final node updates the state with the generated response, which is then rendered on the UI.

## Tech Stack

*   **AI/LLM**: LangChain, LangGraph, Groq API
*   **Vector DB / Retrieval**: FAISS (faiss-cpu)
*   **External Integration**: Tavily Search API
*   **Frontend**: Streamlit
*   **Language**: Python 3.x

## Project Structure

```
├── app.py                         # Application entry point
├── requirements.txt               # Project dependencies
├── AINews/                        # Generated summaries and output files
└── src/
    └── langgraphagenticai/
        ├── LLMS/                  # LLM configuration and abstraction (Groq)
        ├── graph/                 # Graph compilation and routing logic
        ├── nodes/                 # Individual agent execution nodes
        ├── state/                 # Graph state schema definitions
        ├── tools/                 # External tool integrations (Search, etc.)
        └── ui/                    # Streamlit UI components and configuration
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/stateful-agentic.git
    cd stateful-agentic
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory or set the following variables:
    ```env
    GROQ_API_KEY=your_groq_api_key
    TAVILY_API_KEY=your_tavily_api_key
    ```

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

## Challenges Faced

*   **State Management**: Ensuring the graph state schema was robust enough to handle complex, multi-turn tool invocations without context loss.
*   **Deterministic Routing**: Designing conditional edges in LangGraph that reliably handle unexpected LLM outputs or tool failures.
*   **Latency Optimization**: Migrating to Groq for LLM inference to significantly reduce time-to-first-token in multi-step reasoning chains.

## Future Improvements

*   **Multi-Agent Collaboration**: Introduce workflows where specialized agents (e.g., a researcher and a writer) collaborate on a single task.
*   **Persistent Memory**: Integrate a vector database (e.g., Pinecone or robust FAISS implementation) for long-term user memory across sessions.
*   **Advanced RAG Pipelines**: Implement hybrid search capabilities within the tool nodes for more accurate context retrieval.

## License

[MIT License](LICENSE)