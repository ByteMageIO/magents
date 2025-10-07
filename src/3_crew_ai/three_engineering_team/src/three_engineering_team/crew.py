from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ThreeEngineeringTeam():
    """ThreeEngineeringTeam crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def engineering_lead(self):
        return Agent(config=self.agents_config['engineering_lead'], verbose=True)

    @agent
    def backend_engineer(self):
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
        )

    @agent
    def frontend_engineer(self):
        return Agent(
            config=self.agents_config['frontend_engineer'],
            verbose=True,
        )

    @agent
    def test_engineer(self):
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True,
        )

    @task
    def design_task(self):
        return Task(config=self.tasks_config['design_task'], verbose=True)
        
    @task
    def test_task(self):
        return Task(config=self.tasks_config['test_task'], verbose=True)

    @task
    def code_task(self):
        return Task(config=self.tasks_config['code_task'], verbose=True)

    @task
    def frontend_task(self):
        return Task(config=self.tasks_config['frontend_task'], verbose=True)


    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )