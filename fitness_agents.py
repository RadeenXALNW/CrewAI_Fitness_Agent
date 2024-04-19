from crewai import Agent
from langchain.llms import OpenAI
from langchain_groq import ChatGroq
from tools.browser_tools import BrowserTool
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
import os


class FitnessAgents():
    def __init__(self):
        self.llm=ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )



    def fitness_selection_agent(self):
        return Agent(
            role='Fitness Selection Expert',
            goal="""Select the best fitness plan based on current weight, health
            conditions, goal, determination and
            dietary plan.""",
            backstory=
            'An expert in analyzing user data to pick ideal fitness plan',
            tools=[
                SearchTools.search_internet,
                BrowserTool.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=self.llm,
            max_iter=2,)

    def local_expert(self):
        return Agent(
            role='Local Fitness Expert at this city',
            goal='Provide the BEST insights about the selected fitness plan',
            backstory="""A knowledgeable local expert guide with extensive information
            about the fitness plan, it's steps and duty""",
            tools=[
                SearchTools.search_internet,
                BrowserTool.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=self.llm,
            max_iter=2,)

    def fitness_concierge(self):
        return Agent(
            role='Amazing Fitness Concierge',
            goal="""Create the most amazing fitness itineraries with diet, nutrients calculation of each meal and 
            exercise suggestions for the plan""",
            backstory="""Specialist in fitness planning and executing with 
            decades of experience""",
            tools=[
                SearchTools.search_internet,
                BrowserTool.scrape_and_summarize_website,
                CalculatorTools.calculate,
            ],
            verbose=True,
            llm=self.llm,
            max_iter=2,)