#!/usr/bin/env python
import sys
import warnings

from crewai import Agent
from crewai.utilities.prompts import Prompts

from datetime import datetime

from one_crew_of_agents.crew import OneCrewOfAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def preview_prompt(agent: Agent):
    prompt_generator = Prompts(
        agent=agent,
        has_tools=len(agent.tools) > 0,
        use_system_prompt=agent.use_system_prompt
    )
    generated_prompt = prompt_generator.task_execution()
    return generated_prompt

def run():
    inputs = {
        "topic": "Agentic AI"
    }

    crew = OneCrewOfAgents().crew()
    
    print(preview_prompt(crew.agents[0]))

    print("===========================================[ CREW RESULT ]===========================================")
    print(crew.kickoff(inputs=inputs))
    print("===========================================[ CREW RESULT ]===========================================")

if __name__ == "__main__":
    run()