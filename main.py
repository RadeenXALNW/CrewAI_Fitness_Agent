from crewai import Crew
from textwrap import dedent
from fitness_agents import FitnessAgents
from fitness_tasks import FitnessTasks
from crewai import Process


from dotenv import load_dotenv
load_dotenv()

class FitnessCrew:

  def __init__(self, weight, diet, goal, date):
    self.weight = weight
    self.diet = diet
    self.goal = goal
    self.date_range = date

  def run(self):
    agents = FitnessAgents()
    tasks = FitnessTasks()

    fitness_selector_agent = agents.fitness_selection_agent()
    local_expert_agent = agents.local_expert()
    fitness_concierge_agent = agents.fitness_concierge()

    identify_task = tasks.identify_task(
      fitness_selector_agent,
      self.weight,
      self.diet,
      self.goal,
      self.date_range
    )
    gather_task = tasks.gather_task(
      local_expert_agent,
      self.diet,
      self.goal,
      self.date_range,
      context=[identify_task]
    )
    plan_task = tasks.plan_task(
      fitness_concierge_agent, 
      self.diet,
      self.goal,
      self.date_range,
      context=[gather_task]
    )

    crew = Crew(
      agents=[
        fitness_selector_agent, local_expert_agent, fitness_concierge_agent
      ],
      tasks=[identify_task, gather_task, plan_task],
      max_rpm=29,
      verbose=True,
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Fitness Planner Crew")
  print('-------------------------------')
  weight = input(
    dedent("""
      How much is your weight in kg?
    """))
  diet = input(
    dedent("""
      What is your current diet plan?
    """))
  goal = input(
    dedent("""
      What is your goal to achieve this?
    """))
  date = input(
    dedent("""
      Within how many days you want to achieve your goal?
    """))
  
  fitness_crew = FitnessCrew(weight, diet, goal, date)
  result = fitness_crew.run()
  print("\n\n########################")
  print("## Here is you fitness Plan")
  print("########################\n")
  print(result)
