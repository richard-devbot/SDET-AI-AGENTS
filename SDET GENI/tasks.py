from crewai import Task
from textwrap import dedent
from agents import create_agents

from crewai import Task
from textwrap import dedent

def create_tasks(
    test_planning_design_agent, 
    test_automation_agent, 
    test_execution_maintenance_agent, 
    defect_reporting_tracking_agent, 
    test_data_management_agent, 
    continuous_improvement_agent, 
    collaboration_communication_agent, 
    self_healing_predictive_maintenance_agent = create_agents()
):
    # Task 1: Define Test Scope
    define_test_scope_task = Task(
        description=dedent(
            """
            Define the specific areas of the web application that need to be tested:
            1. Review the application's requirements and functionality documentation.
            2. Identify key features, modules, and components that are critical to the application.
            3. Determine the boundaries and limitations of the testing scope.
            4. Document the identified test scope in a clear and detailed manner.
            """
        ),
        expected_output=dedent(
            """
            A document outlining the test scope, specifying the modules and features to be tested, including any assumptions or limitations.
            """
        ),
        agent=test_planning_design_agent,
    )

    # Task 2: Create Test Cases
    create_test_cases_task = Task(
        description=dedent(
            """
            Develop detailed test cases based on the application's functionality and requirements:
            1. Analyze the application's requirements and functionality specifications.
            2. Break down the application into testable units.
            3. Create test cases for each unit, detailing the input data, execution steps, and expected outcomes.
            4. Ensure test cases cover positive, negative, and edge cases.
            5. Review and validate the test cases for completeness and accuracy.
            """
        ),
        expected_output=dedent(
            """
            A set of detailed test cases covering all aspects of the application's functionality, including positive, negative, and edge cases.
            """
        ),
        agent=test_planning_design_agent,
    )

    # Task 3: Prioritize Test Cases
    prioritize_test_cases_task = Task(
        description=dedent(
            """
            Determine the order in which test cases should be executed based on priority:
            1. Assess the risk and impact associated with each test case.
            2. Identify critical paths and high-risk areas in the application.
            3. Assign priority levels to test cases (e.g., high, medium, low).
            4. Create a prioritized test execution plan.
            5. Review and adjust the prioritization with stakeholders if necessary.
            """
        ),
        expected_output=dedent(
            """
            A prioritized list of test cases, with high-priority cases identified and a test execution plan.
            """
        ),
        agent=test_planning_design_agent,
    )

    # Task 4: Write Automation Scripts
    write_automation_scripts_task = Task(
        description=dedent(
            """
            Use automation tools to write scripts that execute the test cases:
            1. Choose appropriate automation tools based on the application and test requirements.
            2. Write automation scripts for each test case, ensuring they follow best practices for readability and maintainability.
            3. Implement error handling and logging mechanisms in the scripts.
            4. Review and test the automation scripts to ensure they work correctly.
            5. Store the scripts in a version control system.
            """
        ),
        expected_output=dedent(
            """
            A set of automation scripts for executing the test cases, stored in a version control system, and reviewed for accuracy.
            """
        ),
        agent=test_automation_agent,
    )

    # Task 5: Integrate with CI/CD
    integrate_with_ci_cd_task = Task(
        description=dedent(
            """
            Integrate the automation scripts with Continuous Integration and Continuous Deployment (CI/CD) pipelines:
            1. Set up a CI/CD environment if not already in place.
            2. Configure the CI/CD pipeline to trigger automated tests on each build and deployment.
            3. Ensure that automation scripts can be executed in the CI/CD environment.
            4. Monitor the CI/CD pipeline for successful execution of tests.
            5. Troubleshoot and resolve any issues with the integration.
            """
        ),
        expected_output=dedent(
            """
            Automation scripts integrated with the CI/CD pipelines, enabling automated testing for each build and deployment.
            """
        ),
        agent=test_automation_agent,
    )

    # Task 6: Run Automated Tests
    run_automated_tests_task = Task(
        description=dedent(
            """
            Execute the automated tests to verify the application's functionality and identify defects:
            1. Schedule and run the automated test scripts.
            2. Monitor the execution of the tests for any issues or failures.
            3. Collect and analyze the results of the automated tests.
            4. Document any defects or discrepancies identified during the tests.
            5. Generate a test execution report summarizing the outcomes.
            """
        ),
        expected_output=dedent(
            """
            A report indicating the status of each test case, including any defects identified and a summary of the test execution.
            """
        ),
        agent=test_execution_maintenance_agent,
    )

    # Task 7: Monitor Test Results
    monitor_test_results_task = Task(
        description=dedent(
            """
            Analyze test results to identify failures and track defects:
            1. Review the test execution results for any anomalies or failures.
            2. Correlate test failures with potential defects in the application.
            3. Log identified defects in the defect tracking system.
            4. Track the progress of defect resolution.
            5. Update the test results documentation with detailed analysis.
            """
        ),
        expected_output=dedent(
            """
            A detailed analysis of test results, highlighting any failures and logged defects, and an updated test results documentation.
            """
        ),
        agent=test_execution_maintenance_agent,
    )

    # Task 8: Identify and Report Defects
    identify_report_defects_task = Task(
        description=dedent(
            """
            Detect and report defects found during testing:
            1. Conduct thorough analysis of test results to identify defects.
            2. Document each defect with detailed information including steps to reproduce, severity, and screenshots.
            3. Report the defects in the defect tracking system.
            4. Communicate the reported defects to relevant stakeholders.
            5. Follow up to ensure defects are addressed in a timely manner.
            """
        ),
        expected_output=dedent(
            """
            A list of defects reported in the defect tracking system, complete with detailed documentation and communication logs.
            """
        ),
        agent=defect_reporting_tracking_agent,
    )

    # Task 9: Track Defects
    track_defects_task = Task(
        description=dedent(
            """
            Log and track defects in a defect tracking system to ensure timely resolution:
            1. Enter all identified defects into the defect tracking system.
            2. Assign appropriate priority and severity levels to each defect.
            3. Regularly update the status of defects as they are resolved.
            4. Collaborate with developers to ensure defects are fixed.
            5. Verify defect fixes through retesting.
            """
        ),
        expected_output=dedent(
            """
            Updated defect tracking system with logged defects and their current status, including retesting results.
            """
        ),
        agent=defect_reporting_tracking_agent,
    )

    # Task 10: Create Test Data
    create_test_data_task = Task(
        description=dedent(
            """
            Generate test data that accurately represents the application's expected inputs and outputs:
            1. Analyze the application's requirements and data flow to understand the needed test data.
            2. Create diverse test data sets covering different input scenarios, including edge cases.
            3. Ensure the test data is realistic and aligns with the application's data validation rules.
            4. Document the created test data sets with descriptions and usage guidelines.
            """
        ),
        expected_output=dedent(
            """
            A set of test data representing various input scenarios for the application, along with documentation on their usage.
            """
        ),
        agent=test_data_management_agent,
    )

    # Task 11: Manage Test Data
    manage_test_data_task = Task(
        description=dedent(
            """
            Store and manage test data to ensure it remains relevant and up-to-date:
            1. Organize the test data into a structured repository.
            2. Implement version control for test data sets to track changes.
            3. Regularly update the test data to reflect any changes in the application's data structure or validation rules.
            4. Perform periodic audits to ensure the test data remains accurate and relevant.
            """
        ),
        expected_output=dedent(
            """
            An organized and updated test data repository with version control and audit records.
            """
        ),
        agent=test_data_management_agent,
    )

    # Task 12: Monitor Test Performance
    monitor_test_performance_task = Task(
        description=dedent(
            """
            Continuously monitor test performance to identify areas for improvement:
            1. Set up performance monitoring tools to track test execution metrics (e.g., execution time, pass/fail rates).
            2. Regularly review test performance data to identify trends and bottlenecks.
            3. Document any performance issues or areas needing improvement.
            4. Propose and implement improvements to enhance test performance.
            """
        ),
        expected_output=dedent(
            """
            Regular performance reports highlighting areas for improvement, along with implemented enhancements.
            """
        ),
        agent=continuous_improvement_agent,
    )

    # Task 13: Refine Test Automation
    refine_test_automation_task = Task(
        description=dedent(
            """
            Refine test automation scripts and processes to optimize testing efficiency and effectiveness:
            1. Review existing automation scripts for readability, maintainability, and efficiency.
            2. Refactor and optimize scripts to improve performance and reliability.
            3. Update the automation framework to incorporate best practices and new technologies.
            4. Document changes and provide training or guidance to the team on new improvements.
            """
        ),
        expected_output=dedent(
            """
            Improved and optimized test automation scripts and processes, with documentation and team training sessions.
            """
        ),
        agent=continuous_improvement_agent,
    )

    # Task 14: Communicate Test Results
    communicate_test_results_task = Task(
        description=dedent(
            """
            Share test results with stakeholders, including developers and project managers:
            1. Compile and summarize test results into a clear and concise report.
            2. Highlight critical defects, test coverage, and areas of concern.
            3. Schedule and conduct meetings to present the test results to stakeholders.
            4. Provide actionable insights and recommendations based on the test outcomes.
            """
        ),
        expected_output=dedent(
            """
            Detailed reports on test results shared with relevant stakeholders, including meeting notes and actionable insights.
            """
        ),
        agent=collaboration_communication_agent,
    )

    # Task 15: Collaborate with Developers
    collaborate_with_developers_task = Task(
        description=dedent(
            """
            Work closely with developers to ensure that defects are properly addressed and resolved:
            1. Schedule regular collaboration sessions with developers to discuss defects and testing progress.
            2. Provide detailed information and context for each reported defect.
            3. Assist developers in reproducing and diagnosing defects.
            4. Retest fixed defects to verify resolution.
            """
        ),
        expected_output=dedent(
            """
            Regular collaboration sessions with developers, detailed defect information, and verification of defect fixes.
            """
        ),
        agent=collaboration_communication_agent,
    )

    # Task 16: Implement Self-Healing
    implement_self_healing_task = Task(
        description=dedent(
            """
            Implement self-healing capabilities in the automation tools to automatically recover from minor UI changes:
            1. Analyze common UI changes and their impact on automation scripts.
            2. Enhance automation scripts with self-healing logic to detect and adapt to minor changes.
            3. Test the self-healing capabilities to ensure they function as expected.
            4. Document the self-healing mechanisms and provide training to the team.
            """
        ),
        expected_output=dedent(
            """
            Enhanced automation scripts with self-healing capabilities, tested for effectiveness, and documented for team training.
            """
        ),
        agent=self_healing_predictive_maintenance_agent,
    )

    # Task 17: Predictive Maintenance
    predictive_maintenance_task = Task(
        description=dedent(
            """
            Use predictive analytics to anticipate and prevent potential issues before they occur:
            1. Collect and analyze historical test data to identify patterns and trends.
            2. Implement predictive models to forecast potential issues based on the data.
            3. Set up monitoring and alerting systems to detect early warning signs.
            4. Take proactive measures to prevent identified potential issues.
            """
        ),
        expected_output=dedent(
            """
            Predictive maintenance reports highlighting potential issues and preventive measures taken.
            """
        ),
        agent=self_healing_predictive_maintenance_agent,
    )

    return (
        define_test_scope_task,
        create_test_cases_task,
        prioritize_test_cases_task,
        write_automation_scripts_task,
        integrate_with_ci_cd_task,
        run_automated_tests_task,
        monitor_test_results_task,
        identify_report_defects_task,
        track_defects_task,
        create_test_data_task,
        manage_test_data_task,
        monitor_test_performance_task,
        refine_test_automation_task,
        communicate_test_results_task,
        collaborate_with_developers_task,
        implement_self_healing_task,
        predictive_maintenance_task
    )

