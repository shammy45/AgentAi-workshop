from crewai import Task

def generate_tasks(topic, agents):
    return [
        Task(
            description=f"Research the topic: '{topic}' and provide a detailed overview.",
            expected_output="Detailed research notes with sources.",
            agent=agents["researcher"]
        ),
        Task(
            description="Summarize the research provided by the researcher into a concise paragraph.",
            expected_output="A summary paragraph with clear and accessible language.",
            agent=agents["summarizer"]
        )
    ]