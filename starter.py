"""
Program Management Knowledge Agent - Starter Code

This program demonstrates two approaches to answering program management questions:
1. Using hardcoded knowledge
2. Using an LLM API

Complete the TODOs to build your knowledge agent.
"""
import openai
from openai import OpenAI
import os

client = OpenAI()

SYSTEM_PROMPT = f"""You are an expert on progam management."""

QUESTIONS = [
    "How do you decide when to use a Gantt chart versus an Agile board?",
    "What role do milestones play in tracking program progress?",
    "How do you identify and manage the critical path in a complex program?",
    "What strategies do you use to keep stakeholders aligned across multiple projects?",
    "How do you ensure clear communication between project teams and executives?"
]

def get_hardcoded_answer(question):
    """
    Return answers to program management questions using hardcoded knowledge.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer to the question
    """
    question = question.lower()
    
    if "gantt charts" in question:
        return("A Gantt chart is a horizontal bar chart that visualizes a project's schedule, showing tasks, their start and end dates, durations, and dependencies over a timeline. It is used for project management.")
    elif "agile" in question:
        return("Agile software development is a group of iterative and incremental methodologies that emphasize collaboration, flexibility, and rapid delivery of high-quality software.")
    elif "sprints" in question:
        return("Agile teams are typically self-organizing and cross-functional, working in short cycles called sprints to continuously inspect and adapt their products and processes.")
    elif "critical path" in question:
        return("The Critical Path Method (CPM) is a project management technique that identifies the sequence of tasks—the \"critical path\"—that determines the shortest possible project completion time.")
    elif "milestones" in question:
        return("A \"milestone\" is a significant point in development, a marker on a project's timeline, or a physical roadside marker indicating distance.")
    else:
        return("That question is not in my knowledge base.")

def get_llm_answer(question):
    """
    Get answers to program management questions using an LLM API.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer from the LLM
    """
    if not client:
        return "OpenAI client not initialized. Please set your API key."

    try:
        response = client.responses.create(
            model="gpt-5",
            instructions=SYSTEM_PROMPT,
            input=question
        )
        return response.output_text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Demo function to compare both approaches
def compare_answers(question):
    """Compare answers from both approaches for a given question."""
    print(f"\nQuestion: {question}")
    print("-" * 50)
    
    print(f"""Hardcoded answer \n
          {get_hardcoded_answer(question)}\n""")
    
    print(f"""LLM answer: \n
          {get_llm_answer(question)}\n""")
    
    print("=" * 50)

# Demo with sample questions
if __name__ == "__main__":
    print(f"Used `openai` module version {openai.__version__}")
    print("PROGRAM MANAGEMENT KNOWLEDGE AGENT DEMO")
    print("=" * 50)
    
    for question in QUESTIONS:
        compare_answers(question)