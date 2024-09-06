from firecrawl import FirecrawlApp
import google.generativeai as genai
import os

genai.configure(api_key="YOUR_GENERATIVEAI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
# Initialize Firecrawl SDK with API key
app = FirecrawlApp(api_key="YOUR_FIRECRAWL_API_KEY")


def scrape_website(url):
    """Scrape the given URL and return markdown and HTML content."""
    scrape_result = app.scrape_url(url, params={'formats': ['markdown', 'html']})
    response = model.generate_content("this is a receipe website it contains receipe of a certain dish analyse this website and give me complete receipe of that dish with name of that receipe on top and the reqirement next the the recipe next also add tips at the end for that dist with some extra trivia about that dish. dont add any more data. also if its not a website with a receipe of a dish then just return 'this is not a dish'"+scrape_result['markdown'])
    return response.text

