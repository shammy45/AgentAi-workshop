# main.py
from dynamictasks.crew import ResearchCrew

def run():
    topic = input("Enter a topic to research and summarize: ")

    # Instantiate your CrewBase class
    crew_instance = ResearchCrew()
    
    # Access agents directly if needed (optional)
    researcher = crew_instance.researcher()
    summarizer = crew_instance.summarizer()

    # Dynamically generate tasks
    from dynamictasks.tasks import generate_tasks
    tasks = generate_tasks(topic, {'researcher': researcher, 'summarizer': summarizer})

    from crewai import Crew
    crew = Crew(
        agents=[researcher, summarizer],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("\n✅ Final Result:\n", result)