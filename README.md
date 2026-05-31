# 🧠 Multi-Agent AI-Driven Research System

> Enter a topic. Get a fully researched, written, and reviewed report — automatically.

**Live Demo:** [multi-agent-ai-driven-research-system.streamlit.app](https://multi-agent-ai-driven-research-system.streamlit.app)

---

## What is this?

A fully autonomous research pipeline built with LangChain and Google Gemini. You type a topic — the system searches the web, scrapes the most relevant sources, writes a structured report, and critiques its own output. No manual steps.

---

## How it works

The pipeline runs 4 stages in sequence:

```
Topic Input
    │
    ▼
🔍 Search Agent       →  Queries the web via Tavily, returns titles, URLs & snippets
    │
    ▼
🌐 Reader Agent       →  Picks the best URL and scrapes full article content
    │
    ▼
✍️  Writer Chain       →  Synthesises research into a structured report
    │
    ▼
🎯 Critic Chain       →  Reviews the report and scores it with actionable feedback
```

---

## Project Structure

```
Multi-Agent-AI-Driven-Research-System/
├── app.py              # Streamlit UI
├── agents.py           # LangChain agents + writer/critic chains
├── pipeline.py         # Orchestrates the 4-stage research pipeline
├── tools.py            # web_search (Tavily) + scrape_url (BeautifulSoup)
├── requirements.txt
├── .env.example        # Template for API keys
└── .gitignore
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Google Gemini 2.5 Flash (`langchain-google-genai`) |
| Agents | LangChain ReAct agents |
| Web Search | Tavily Search API |
| Scraping | Requests + BeautifulSoup4 |
| UI | Streamlit |
| Deployment | Streamlit Cloud |

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/SumitGoulikar/Multi-Agent-AI-Driven-Research-System.git
cd Multi-Agent-AI-Driven-Research-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up API keys

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your keys here:
- **Google API Key** → [aistudio.google.com](https://aistudio.google.com) (free)
- **Tavily API Key** → [app.tavily.com](https://app.tavily.com) (free tier available)

### 4. Run locally

```bash
streamlit run app.py
```

---

## Deploying to Streamlit Cloud

1. Push your repo to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io) → **Create app**
3. Select your repo and set main file to `app.py`
4. Go to **Settings → Secrets** and add:

```toml
GOOGLE_API_KEY = "your_key_here"
TAVILY_API_KEY = "your_key_here"
```

5. Deploy — done.

---

## Example Output

**Input:** `AI in healthcare`

**Pipeline produces:**
- ✅ Search results with real URLs from the web
- ✅ Scraped content from the top article
- ✅ Structured report: Introduction → Key Findings → Conclusion → Sources
- ✅ Critic score with strengths and improvement areas

---

## Known Limitations

- Gemini 2.5 Flash can return 503 errors during peak hours — switch to `gemini-1.5-flash` if this happens frequently
- Some websites block scraping; the reader agent falls back to search summaries in that case
- Free Tavily tier has a monthly request limit

---

## License

MIT — free to use, modify, and build on.

---

## Author

**Sumit Goulikar** — [github.com/SumitGoulikar](https://github.com/SumitGoulikar)
