#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from three_engineering_team.crew import ThreeEngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

os.makedirs("output", exist_ok=True)

requirements = """
YOUR REQUIREMENTS HERE
"""

module_name = "YOUR MODULE NAME (without the .py extension)"
class_name = "YOUR CLASS NAME"

def run():
    inputs = {
        "requirements": requirements,
        "module_name": module_name,
        "class_name": class_name,
    }
    result =  ThreeEngineeringTeam().crew().kickoff(inputs=inputs)