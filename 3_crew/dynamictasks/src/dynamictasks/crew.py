import yaml
import os
from crewai import Agent, Crew
from dynamictasks.tasks import generate_tasks  # Dynamic task generator
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ResearchCrew():
    """Research crew for comprehensive topic analysis and reporting"""

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base_dir, 'config/agents.yaml'), 'r') as f:
            self.agents_config = yaml.safe_load(f)
        #with open(os.path.join(base_dir, 'config/tasks.yaml'), 'r') as f:
        #    self.tasks_config = yaml.safe_load(f)
        # The @agent and @task decorators from CrewBase should auto-collect these
        # But if not, you may need to collect them manually
        # self.agents = [self.researcher(), self.analyst()]
        # self.tasks = [self.research_task(), self.analysis_task()]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            #tools=[SerperDevTool()],
            verbose=True
            
        )
    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True
        )

def setup_crew(topic):
    """Dynamically setup a CrewAI workflow based on the input topic."""
    agents = load_agents()
    tasks = generate_tasks(topic, agents)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    return crew