# LangChain Chatbot

A conversational AI chatbot built with LangChain, FastAPI, and Streamlit. Supports multiple LLM providers including Ollama and OpenAI.

## Features

- **Multiple LLM Providers**: Switch between Ollama (local) and OpenAI models
- **FastAPI Backend**: RESTful API for chatbot interactions
- **Streamlit UI**: User-friendly web interface
- **Environment-based Configuration**: Easy setup via `.env` file

## Requirements

- Python 3.11+
- Ollama (for local models) or OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langchain-chatbot
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

## Configuration

Configure your environment variables in `.env`:

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_BASE_URL` | Ollama server URL | `http://localhost:11434` |
| `OLLAMA_MODEL` | Ollama model name | `llama2` |
| `OPENAI_API_KEY` | OpenAI API key | - |
| `OPENAI_MODEL` | OpenAI model name | `gpt-4` |

## Usage

### Start the API Server

```bash
uvicorn src.main:app --reload
```

### Start the Streamlit UI

```bash
streamlit run app.py
```

## Project Structure

```
langchain-chatbot/
├── src/
│   ├── api/              # API endpoints
│   ├── config/           # Configuration settings
│   ├── core/             # Core utilities (logging, etc.)
│   ├── providers/        # LLM provider integrations
│   │   ├── ollama.py
│   │   └── openai.py
│   └── main.py           # FastAPI application
├── .env                  # Environment variables
├── .env.example          # Environment template
├── pyproject.toml        # Project metadata
└── README.md
```

## Tech Stack

- **LangChain**: AI chain orchestration
- **FastAPI**: Web framework
- **Streamlit**: UI framework
- **Ollama**: Local LLM runtime

## License

MIT
