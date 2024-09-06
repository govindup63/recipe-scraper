# from firecrawl import FirecrawlApp

# app = FirecrawlApp(api_key="fc-2278e8938538492086116cd02fd7dc74")

# # Crawl a website:
# crawl_status = app.crawl_url(
#   'https://www.simplyrecipes.com/search?q=french+fries', 
#   params={
#     'limit': 100, 
#     'scrapeOptions': {'formats': ['markdown', 'html']}
#   },
#   poll_interval=30
# )
# print(crawl_status['data'][1])

from serpapi import GoogleSearch

def get_top_google_result(query):
    params = {
        "q": query,
        "api_key": "1c23e2dbcfc32ce06e9f962de328dd7007703dbe7051611bab455f62807fde41",
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    top_result = results['organic_results'][0]['link']  # Get the top result link
    return top_result

# Example usage:
top_link = get_top_google_result("best chocolate cake recipe")
print("Top Google result:", top_link)
