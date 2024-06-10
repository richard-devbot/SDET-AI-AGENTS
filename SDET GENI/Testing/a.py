import os
from textwrap import dedent
import streamlit as st
from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from to import PythonExecutorTool, ReportingTool, ScriptAnalyzerTool, WebInspectorTool, ScriptEditorTool, ScriptGeneratorTool, VersionControlTool

load_dotenv()

python_executor_tool = PythonExecutorTool()
script_folder = r"E:\\Appdata\\program files\\python\\projects\\projects folder on crewAI\\linkdin crew\\New folder"
result = python_executor_tool._run(script_folder)
print(result)

Groq_llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0,
    google_api_key="AIzaSyAU97ZxASlUERhrK3MJ2IlIEYLL5lzxm4Y"
)

def create_agents():
    # Agent to run existing Python automation scripts
    run_scripts_agent = Agent(
        role="Script Runner",
        goal="""Execute existing Python automation scripts for the web application and report results to ensure ongoing functionality and performance.""",
        tools=[python_executor_tool, ReportingTool()],
        backstory=dedent(
            """
            This agent is responsible for executing existing automation scripts to ensure the web application's functionality is as expected.
            It runs the scripts, captures outputs, logs any issues, and provides detailed reports for further analysis.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
    )

    # Agent to auto-heal failed scripts
    auto_heal_agent = Agent(
        role="Script Healer",
        goal="""Automatically identify and fix failures in automation scripts caused by web application changes, ensuring scripts remain effective.""",
        tools=[ScriptAnalyzerTool(), WebInspectorTool(), ScriptEditorTool()],
        backstory=dedent(
            """
            This agent ensures the robustness of the automation scripts by detecting failures due to changes in the web application.
            It analyzes the root causes of failures, inspects the web application for changes (like new locators or updated elements), and modifies the scripts to restore functionality.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
    )

    # Agent to maintain and update automation scripts
    maintenance_agent = Agent(
        role="Script Maintainer",
        goal="""Ensure the automation scripts are always up-to-date with the web application by adding new scripts for newly added pages, elements, and functionalities.""",
        tools=[WebInspectorTool(), ScriptGeneratorTool(), VersionControlTool()],
        backstory=dedent(
            """
            This agent is tasked with the ongoing maintenance and enhancement of the automation suite.
            It monitors the web application for changes such as new pages or elements and writes new automation scripts or updates existing ones to incorporate these changes,
            ensuring the automation suite remains comprehensive and effective.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
    )

    return run_scripts_agent, auto_heal_agent, maintenance_agent
