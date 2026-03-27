from duckduckgo_search import DDGS
import trafilatura
from typing import List, Dict

class ResearcherDriver:
    """
    Performs live web research and scraping to provide real-time data to NEXUS.
    Free and requires no API keys.
    """
    def __init__(self, max_results: int = 3):
        self.max_results = max_results

    def search_and_scrape(self, query: str) -> str:
        """
        Searches DuckDuckGo and scrapes the top results.
        Returns a synthesized text block of all findings.
        """
        research_content = f"--- LIVE RESEARCH DATA FOR: {query} ---\n\n"
        
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=self.max_results))
                
                for i, result in enumerate(results):
                    url = result.get('href')
                    research_content += f"[Source {i+1}]: {url}\n"
                    
                    # Scrape the actual page content
                    downloaded = trafilatura.fetch_url(url)
                    if downloaded:
                        content = trafilatura.extract(downloaded)
                        if content:
                            research_content += f"CONTENT: {content[:2000]}...\n\n" # Limit per source
                    else:
                        research_content += f"SUMMARY: {result.get('body')}\n\n"
                        
            return research_content
        except Exception as e:
            return f"Research Error: {str(e)}"

if __name__ == "__main__":
    # Quick test
    researcher = ResearcherDriver(max_results=2)
    print("Testing live research on 'Current AI Side Hustles 2026'...")
    print(researcher.search_and_scrape("Current AI Side Hustles 2026")[:500] + "...")
