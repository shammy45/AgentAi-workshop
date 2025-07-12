from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import yaml
import os

def load_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)

@CrewBase
class Coder():
    """CrewAI-powered Python Coder"""

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.agents_config = load_yaml(os.path.join(base_dir, 'config/agents.yaml'))
        self.tasks_config = load_yaml(os.path.join(base_dir, 'config/tasks.yaml'))

    @agent
    def coder(self, assignment: str = None) -> Agent:
        config = self.agents_config['coder'].copy()
        if assignment:
            config['role'] = config['role'].format(assignment=assignment)
            config['goal'] = config['goal'].format(assignment=assignment)
        
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            llm=config['llm'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",  # Uses Docker for safety
            max_execution_time=30,
            max_retry_limit=3
        )

    @task
    def coding_task(self, assignment: str) -> Task:
        return Task(
            description=self.tasks_config['coding_task']['description'].format(assignment=assignment),
            expected_output=self.tasks_config['coding_task']['expected_output'],
            agent=self.coder(),
            output_file=self.tasks_config['coding_task']['output_file']
        )

    @crew
    def crew(self, assignment: str) -> Crew:
        """Creates the Coder crew with dynamic input"""
        
        task = self.coding_task(assignment)
      
        crew = Crew(
            agents=[self.coder(assignment)],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )
        print(f"✅ Crew created: {crew}")
        return crew