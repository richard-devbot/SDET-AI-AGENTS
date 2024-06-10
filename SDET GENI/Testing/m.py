from a import create_agents
from t import create_tasks


def main():
    # Create the agents
    run_scripts_agent, auto_heal_agent, maintenance_agent = create_agents()

    # Create the tasks
    run_scripts_task, auto_heal_task, maintain_scripts_task = create_tasks(run_scripts_agent, auto_heal_agent, maintenance_agent)

    tasks = [
        run_scripts_task, auto_heal_task, maintain_scripts_task
    ]

    # Execute each task
    for task in tasks:
        print(f"Executing task: {task.description}")
        output = task.agent.execute_task(task)
        print(f"Task output: {output}")
        print(f"Expected output: {task.expected_output}\n")


if __name__ == "__main__":
    main()