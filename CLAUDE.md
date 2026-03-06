# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LangChain Chatbot - A conversational AI chatbot built with LangChain, FastAPI, and Streamlit. Supports multiple LLM providers including Ollama (local) and OpenAI.

## Common Commands

```bash
# Install dependencies
pip install -e .

# Start the API server
uvicorn src.main:app --reload

# Start the Streamlit UI
streamlit run app1.py
```

## Architecture

The project has two main entry points:

- **app1.py** - Main chatbot implementation using LangChain with Ollama. Implements a conversational CLI with chat history tracking and turn limits.
- **src/main.py** - FastAPI application (currently minimal, serves as API backend scaffold)

### Source Structure

```
src/
├── config/settings.py     # Configuration module (uses python-dotenv)
├── core/loggings.py       # Logging utilities
├── providers/
│   ├── ollama.py         # Ollama LLM provider integration
│   └── openai.py         # OpenAI LLM provider integration
└── main.py               # FastAPI app entry point
```

### Key Components

- **Chat Implementation** (`app1.py`): Uses `ChatOllama` from langchain-ollama, maintains chat history with `MessagesPlaceholder`, limits conversation turns (default 6), uses `StrOutputParser`
- **Configuration**: Environment variables loaded via `python-dotenv` from `.env` file

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_BASE_URL` | Ollama server URL | `http://localhost:11434` |
| `OLLAMA_MODEL` | Ollama model name | `llama2` |
| `OPENAI_API_KEY` | OpenAI API key | - |
| `OPENAI_MODEL` | OpenAI model name | `gpt-4` |
| `MODEL_NAME` | Model to use | - |
| `TEMPERATURE` | LLM temperature | - |
| `MAX_TURNS` | Max conversation turns | - |

## Tech Stack

- **LangChain**: AI chain orchestration
- **FastAPI**: Web framework
- **Streamlit**: UI framework
- **Ollama**: Local LLM runtime
- **python-dotenv**: Environment variable management

## Notes

- The project uses Python 3.11+
- Dependencies managed via `pyproject.toml` with `uv` (uv.lock present)
- The `src/` directory structure is set up but most modules are placeholders
- The working chatbot logic is currently in `app1.py`
