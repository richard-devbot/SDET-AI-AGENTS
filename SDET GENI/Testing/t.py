from textwrap import dedent
from crewai import Task
from a import create_agents

def create_tasks(run_scripts_agent, auto_heal_agent, maintenance_agent = create_agents()):
    # Task 1: Run existing Python automation scripts
    run_scripts_task = Task(
        description=dedent(
            """
            Execute the existing Python automation scripts located in the specified folder. 
            Steps:
            1. Identify and load all Python scripts in the designated folder.
            2. Sequentially execute each script.
            3. Capture the output, including pass/fail status, logs, and any generated screenshots.
            4. Aggregate the results into a comprehensive report.
            5. Save and upload the report to the specified location.
            """
        ),
        expected_output=dedent(
            """
            The automation scripts are executed successfully. A detailed report is generated containing:
            - Pass/fail status of each script.
            - Execution logs.
            - Screenshots (if any).
            - Summary of overall results.
            The report is saved and accessible in the specified location.
            """
        ),
        agent=run_scripts_agent
    )

    # Task 2: Auto-heal failed scripts
    auto_heal_task = Task(
        description=dedent(
            """
            Monitor the execution of automation scripts and auto-heal any failed scripts.
            Steps:
            1. Monitor the execution results of automation scripts.
            2. Identify any script failures and log the failure details.
            3. Analyze the root cause of each failure (e.g., changes in web application elements, locators).
            4. Inspect the web application to detect changes related to the failures.
            5. Update the scripts to fix the identified issues.
            6. Re-execute the updated scripts to ensure they pass.
            7. Document the changes and update the script repository.
            """
        ),
        expected_output=dedent(
            """
            - Failures in automation scripts are identified and analyzed.
            - Scripts are updated to address the causes of the failures.
            - Updated scripts are successfully re-executed, ensuring they pass.
            - Changes are documented and the script repository is updated.
            """
        ),
        agent=auto_heal_agent
    )

    # Task 3: Maintain and update automation scripts
    maintain_scripts_task = Task(
        description=dedent(
            """
            Maintain and update automation scripts to ensure comprehensive coverage of the web application.
            Steps:
            1. Regularly review the web application for updates (e.g., new pages, elements).
            2. Identify new areas that require automation.
            3. Write new automation scripts for newly added pages or elements.
            4. Update existing scripts to accommodate changes in the web application.
            5. Test new and updated scripts to ensure they work as expected.
            6. Integrate new and updated scripts into the automation suite.
            7. Commit changes to the version control system with detailed commit messages.
            """
        ),
        expected_output=dedent(
            """
            - New automation scripts are created for newly added pages or elements.
            - Existing scripts are updated to reflect changes in the web application.
            - All new and updated scripts are tested and verified for correctness.
            - The automation suite is updated with the new and modified scripts.
            - Changes are committed to the version control system with detailed commit messages.
            """
        ),
        agent=maintenance_agent
    )

    return run_scripts_task, auto_heal_task, maintain_scripts_task
