import json
import os
from langchain_groq import ChatGroq
import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from dotenv import load_dotenv
load_dotenv()

    # url = f"https://api.scrapingdog.com/scrape?api_key={api_key}&url={website}&dynamic=false"

# class BrowserTools():


#   @tool("Scrape website content")

#   def scrape_and_summarize_website(website):
#     """Useful to scrape and summarize a website content"""

#     api_key = os.environ.get('SCRAPINGANT_API_KEY')  # Fetch API key from environment variable
#     if not api_key:
#         return "API key not found. Please set SCRAPINGANT_API_KEY environment variable."
    
#     url = f"https://api.scrapingant.com/v2/general?url={website}&x-api-key={api_key}"
#     payload = json.dumps({"url": website})
#     headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
#     response = requests.request("POST", url, headers=headers, data=payload)
#     elements = partition_html(text=response.text)  # Assuming you have the partition_html function defined
#     content = "\n\n".join([str(el) for el in elements])
#     content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
#     summaries = []
#     for chunk in content:
#         agent = Agent(
#             role='Principal Researcher',
#             goal=
#             'Do amazing researches and summaries based on the content you are working with',
#             backstory=
#             "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
#             allow_delegation=False)
#         task = Task(
#             agent=agent,
#             description=
#             f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
#         )
#         summary = task.execute()
#         summaries.append(summary)
#     return "\n\n".join(summaries)


from unstructured.partition.html import partition_html

class BrowserTool():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""

    # url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    url = "http://localhost:3000/content"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)

    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])

    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      chunking_agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing researches and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
          allow_delegation=False)
      chunking_task = Task(
          agent=chunking_agent,
          description=
          f'Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = chunking_task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)