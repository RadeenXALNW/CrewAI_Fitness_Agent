from crewai import Task
from textwrap import dedent
from datetime import date


class FitnessTasks():

  def identify_task(self, agent, weight, diet, goal, date,context=None):
    return Task(description=dedent(f"""
        Analyze and select the best fitness plan for the client based 
        on specific criteria such as client's weight, dietary plan, which kind of physique they want to have
        and within how much time they want to achieve this. 
        This task involves comparing multiple factors, considering factors like current weight, health
        conditions, goal, determination and
        dietary plan. 
        
        Your final answer must be a detailed long report on selecting the task and why you are selecting the task, give long
        report on the chosen fitness plan, and everything you found out
        about it, including the actual problems we have to overcome.
        {self.__recommend_section()}

        Your weight: {weight}
        Dietary Plan: {diet}
        Goal : {goal}
        Achievable date: {date}
      """),
                agent=agent,context=context)

  def gather_task(self, agent, diet, goal, date,context=None):
    return Task(description=dedent(f"""
        As a fitness expert on this task you must compile an 
        in-depth guide for someone who want to have a fitness plan
        and wanting to maintain it properly.
        Gather information about  the excercies they can do, the diet
        they have to maintain, in the special events if they can have 
        a cheat meal, the goal they want to achieve and the time they want that
        to take to achieve the goal considering all these.
        Gather information about how much calories, protiens and other nutrients they can intake regularly.
        Gather information about the best dresses to wear during exercise, the kind of thing only an 
        expert would know.
        This guide should gather information from thorough overview of what 
        the fitness plan has to offer, including the exercices, dietary plan, 
        occasional diet, to be cautious about the excercise steps,
        and the intensity of the exercise.
        The final answer must be a report on gathering inforrmation about comprehensive fitness plan guide, 
        deep in fitness insights and practical tips, 
        tailored to enhance the fitness journey.
        {self.__recommend_section()}

        Dietary Plan: {diet}
        Goal : {goal}
        Achievable date: {date}
      """),agent=agent,context=context)

  def plan_task(self, agent, diet, goal, date,context=None):
    return Task(description=dedent(f"""
        Expand this guide into a a full 30-day fitness plan
        with long and detailed per-day plans that means each day's plans, including
        which exercise should take at morning, the morning breakfast,
        the brunch, the lunch and the dinner plan, what to eat,
        when to eat, how much times should we reserve for the exercise.
        
        You MUST suggest actual steps to complete, actual food
        to make.
        
        This plan should cover all aspects of the fitness, 
        from day 1 to day 30, integrating the all
        information with practical fitness plan and methods.
        
        Your final answer MUST be a complete expanded fitness plan,
        formatted as markdown, encompassing a daily workout schedule,
        anticipated workout, recommended clothing and
        items to use, and a detailed dietary plan, ensuring THE BEST
        fitness plan EVER. In the dietary plan also calculate the total nutrients one can intake daily.
        Make nutrients calculation for each meal.
        Make a complete understandable workout schedule that can be maintained properly.
        Be specific and give it a reason why you picked
        # up each plan, what make them effective!
        # Also add if any precaution has to be taken before workout sessions. {self.__recommend_section()}

        Dietary Plan: {diet}
        Goal : {goal}
        Achievable date: {date}
      """),
                agent=agent,context=context)

  def __recommend_section(self):
    return "If you do your BEST WORK, I'll recommend you to my friends."
