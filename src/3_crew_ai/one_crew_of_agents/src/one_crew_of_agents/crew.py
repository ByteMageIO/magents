from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool
from pydantic import BaseModel

from one_crew_of_agents.tools.email_tool import EmailTool

class ResearchOutput(BaseModel):
    key_concepts: List[str]
    historical_development: List[str]
    major_challenges: List[str]
    notable_applications: List[str]
    future_outlook: List[str]

@CrewBase
class OneCrewOfAgents():
    """OneCrewOfAgents crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self):
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[SerperDevTool()],
        )
    
    @agent
    def analyst(self):
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True,
        )

    @agent
    def email_sender(self):
        return Agent(
            config=self.agents_config['email_sender'],
            verbose=True,
            tools=[EmailTool()],
        )

    @task
    def research_task(self):
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def analysis_task(self):
        return Task(
            config=self.tasks_config['analysis_task'],
        )

    @task
    def send_email_task(self):
        return Task(
            config=self.tasks_config['send_email_task'],
        )

    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )