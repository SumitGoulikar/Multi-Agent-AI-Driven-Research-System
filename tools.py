import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.tools import tool
from rich import print
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable topic that returns Titles, URLs, and snippets."""
    results = tavily.search(query=query, max_results=5)

    outcome = []

    for r in results["results"]:
        outcome.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )

    return "\n========================\n".join(outcome)


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from given URL for deeper research."""
    try:
        response = requests.get(url, timeout=8, headers={"User-Agents": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scraoe the URL: {str(e)}"

