# 📚 AI Multi-Agent System with Persistent Memory
This project is an AI-powered multi-agent system that collaboratively performs technical research, document drafting, and fact-checking — while persistently storing conversation context in a SQLite database for later recall.
#📖 Overview
The system consists of three intelligent agents working together:

- **Researcher Agent** — conducts research on a given topic using the Gemini API.

- **Writer Agent** — drafts a technical document based on the research findings.

- **Fact-Checker Agent** — reviews the document against the research, identifies issues, and suggests corrections.

All interactions and context (research, document drafts, fact-check feedback) are stored in a local SQLite database for persistent memory and later recall.


# ⚙️ Technologies Used
Python 3.12+

- **Gemini API** (Generative AI by Google)

- **SQLite** (via sqlite3 module)

- **python-docx** (for DOCX report export)

# 🗄️ Database Schema

**Table:** `context`

| Field      | Type      | Description                                                        |
|------------|-----------|--------------------------------------------------------------------|
| `id`       | INTEGER    | Primary key (autoincrement)                                         |
| `topic`    | TEXT       | Type of context (`research_text`, `document_text`, `fact_check_text`) |
| `content`  | TEXT       | The actual stored content                                           |
| `created_at` | TIMESTAMP | Timestamp of entry (auto-set)                                       |


# Usage
## Add your gemini api key on config.json file
[
    {
         "model": "gemini-1.5-flash",
         "api_key": "your api here",
         "api_type": "google"
    },
    {
         "model": "gemini-1.5-pro",
         "api_key": "your api here",
         "api_type": "google"
    }
]
