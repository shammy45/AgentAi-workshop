#!/usr/bin/env python
import os
import warnings
import gradio as gr
from datetime import datetime
import re

from crew import Coder  # Fixed import

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Ensure output directory exists
os.makedirs('output', exist_ok=True)



def solve_code_problem(assignment: str):
    try:
        coder = Coder()
        crew = coder.crew(assignment=assignment)
        result = crew.kickoff()

        raw = result.raw
        code = raw
        output = raw

        # Save code to file
        with open("output/response.py", "w") as f:
            f.write(code)

        return f"###  Code:\n`python\n{code}\n`\n\n###  Output:\n{output}"
    except Exception as e:
        return f" Error occurred:\n{str(e)}"

def run():
    """
    Main function to launch Gradio UI — used by uv or direct call
    """
    iface = gr.Interface(
        fn=solve_code_problem,
        inputs=gr.Textbox(lines=4, label="Enter your Python Problem Statement"),
        outputs=gr.Markdown(label="Generated Code + Output"),
        title="CrewAI Python Code Generator",
        description="Enter a problem and get Python code written + executed by a CrewAI agent.",
        flagging_mode="never"
    )
    iface.launch()

# For direct run: python main.py
if __name__ == "__main__":
    run()