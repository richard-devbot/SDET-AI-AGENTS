import os
from textwrap import dedent
import streamlit as st
from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


Groq_llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192")

# gemini_llm = ChatGoogleGenerativeAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     model="gemini-pro")


gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0,
    google_api_key="AIzaSyAU97ZxASlUERhrK3MJ2IlIEYLL5lzxm4Y",
)


def streamlit_callback(step_output):
    # This function will be called after each step of the agent's execution
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict) and "tool" in action and "tool_input" in action and "log" in action:
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action['tool']}")
                st.markdown(f"**Tool Input** {action['tool_input']}")
                st.markdown(f"**Log:** {action['log']}")
                st.markdown(f"**Action:** {action['Action']}")
                st.markdown(
                    f"**Action Input:** ```json\n{action['tool_input']}\n```")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")
            else:
                st.markdown(f"**Action:** {str(action)}")

            st.markdown(f"**Observation**")
            if isinstance(observation, str):
                observation_lines = observation.split('\n')
                for line in observation_lines:
                    if line.startswith('Title: '):
                        st.markdown(f"**Title:** {line[7:]}")
                    elif line.startswith('Link: '):
                        st.markdown(f"**Link:** {line[6:]}")
                    elif line.startswith('Snippet: '):
                        st.markdown(f"**Snippet:** {line[9:]}")
                    elif line.startswith('-'):
                        st.markdown(line)
                    else:
                        st.markdown(line)
            else:
                st.markdown(str(observation))
        else:
            st.markdown(step)


import os
from textwrap import dedent
import streamlit as st
from crewai import Agent
# from crewai_tools import SeleniumTool, BeautifulSoupTool, PyAutoGUITool
from dotenv import load_dotenv
from tools.tools import (
    RequirementsAnalyzerTool,
    TestCaseManagerTool,
    SeleniumTool,
    CI_CDIntegrationTool,
    TestExecutionFramework,
    TestResultsMonitorTool,
    JIRATool,
    TestDataGeneratorTool,
    TestDataManagerTool,
    PerformanceMonitorTool,
    AnalyticsTool,
    CommunicationTool,
    CollaborationPlatform,
    SelfHealingTool,
    PredictiveAnalyticsTool
)

load_dotenv()

def create_agents():
    test_planning_design_agent = Agent(
        role="Test Planning and Design",
        goal="""Define test scope, create detailed test cases based on functionality and requirements, and prioritize test cases for execution.""",
        tools=[RequirementsAnalyzerTool(), TestCaseManagerTool()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, skilled in planning and designing test cases for web applications.
            You have a deep understanding of application requirements and can efficiently create and prioritize test cases.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    test_automation_agent = Agent(
        role="Test Automation",
        goal="""Automate test cases using suitable tools, integrate automation scripts with CI/CD pipelines to ensure continuous testing.""",
        tools=[SeleniumTool(), CI_CDIntegrationTool()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, proficient in writing and maintaining automation scripts for web applications.
            You can seamlessly integrate automation scripts with CI/CD pipelines for continuous testing.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    test_execution_maintenance_agent = Agent(
        role="Test Execution and Maintenance",
        goal="""Execute automated tests, monitor test results to identify failures, and maintain test scripts to keep them up-to-date.""",
        tools=[TestExecutionFramework(), TestResultsMonitorTool()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, skilled in executing automated tests and monitoring results.
            You can quickly identify failures and ensure test scripts are regularly updated and maintained.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    defect_reporting_tracking_agent = Agent(
        role="Defect Reporting and Tracking",
        goal="""Identify and report defects found during testing, and track defects in a defect tracking system to ensure timely resolution.""",
        tools=[JIRATool()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, proficient in identifying, reporting, and tracking defects.
            You ensure that all defects are logged and tracked for timely resolution.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    test_data_management_agent = Agent(
        role="Test Data Management",
        goal="""Generate test data that accurately represents the application's expected inputs and outputs, and manage test data to keep it up-to-date.""",
        tools=[TestDataGeneratorTool(), TestDataManagerTool()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, proficient in generating and managing test data for web applications.
            You ensure that test data is comprehensive and up-to-date for effective testing.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    continuous_improvement_agent = Agent(
        role="Continuous Improvement",
        goal="""Monitor test performance, identify areas for improvement, and refine test automation scripts and processes for optimal efficiency.""",
        tools=[PerformanceMonitorTool(), AnalyticsTool()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, dedicated to continuously improving test processes and automation efficiency.
            You use performance monitoring and analytics tools to optimize testing.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    collaboration_communication_agent = Agent(
        role="Collaboration and Communication",
        goal="""Communicate test results with stakeholders, including developers and project managers, and collaborate closely with developers to ensure defects are resolved.""",
        tools=[CommunicationTool(), CollaborationPlatform()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, skilled in communicating test results and collaborating with development teams.
            You ensure effective communication and collaboration for timely defect resolution.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    self_healing_predictive_maintenance_agent = Agent(
        role="Self-Healing and Predictive Maintenance",
        goal="""Implement self-healing capabilities in automation tools to automatically recover from minor UI changes and use predictive analytics to anticipate and prevent potential issues.""",
        tools=[SelfHealingTool(), PredictiveAnalyticsTool()],
        backstory=dedent(
            """
            You are an experienced SDET engineer, proficient in implementing self-healing capabilities and predictive maintenance.
            You use advanced automation techniques to enhance the resilience and predictive power of test scripts.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm,
        step_callback=streamlit_callback,
    )

    return (
        test_planning_design_agent,
        test_automation_agent,
        test_execution_maintenance_agent,
        defect_reporting_tracking_agent,
        test_data_management_agent,
        continuous_improvement_agent,
        collaboration_communication_agent,
        self_healing_predictive_maintenance_agent,
    )
