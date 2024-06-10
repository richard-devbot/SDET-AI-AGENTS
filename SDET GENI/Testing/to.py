from crewai_tools import BaseTool
import subprocess
import traceback
import os
import requests
from bs4 import BeautifulSoup

class PythonExecutorTool(BaseTool):
    name: str = "Python Executor"
    description: str = "Executes all Python scripts in the given folder and generates detailed reports."

    def _run(self, script_folder: str) -> str:
        try:
            reports = []
            for filename in os.listdir(script_folder):
                if filename.endswith('.py'):
                    script_path = os.path.join(script_folder, filename)
                    result = subprocess.run(['python', script_path], capture_output=True, text=True)
                    report = f"Script '{filename}' executed successfully.\nOutput:\n{result.stdout}\nError:\n{result.stderr}"
                    reports.append(report)
            return "\n\n".join(reports)
        except Exception as e:
            error_message = f"Error occurred while executing scripts in folder '{script_folder}': {e}"
            return f"**Error Report**\n{error_message}\n{traceback.format_exc()}"
              
class ReportingTool(BaseTool):
    name: str = "Reporting Tool"
    description: str = "Generates structured reports from execution results."

    def _run(self, script_output: str) -> str:
        try:
            if "Error" in script_output or "Exception" in script_output:
                return self._generate_error_report(script_output)
            else:
                return f"**Success Report**\n{script_output}"
        except Exception as e:
            return self._generate_error_report(str(e))

    def _generate_error_report(self, error_message: str) -> str:
        tb = traceback.format_exc()
        report = f"**Error Report**\nError Message: {error_message}\nTraceback:\n{tb}"
        return report

class ScriptAnalyzerTool(BaseTool):
    name: str = "Script Analyzer"
    description: str = "Analyzes the given script to identify issues or failures."

    def _run(self, script_log: str) -> str:
        error_messages = []
        for line in script_log.splitlines():
            if "ERROR" in line or "Exception" in line:
                error_messages.append(line.strip())
        
        if error_messages:
            return "Script analysis found errors:\n" + "\n".join(error_messages)
        else:
            return "Script analysis did not find any errors."

class WebInspectorTool(BaseTool):
    name: str = "Web Inspector"
    description: str = "Inspects the web application to identify changes in elements and locators."

    def _run(self, url: str) -> str:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.find_all()
            changes = []
            for element in elements:
                if 'id' in element.attrs:
                    changes.append(f"ID: {element.attrs['id']}")
                if 'class' in element.attrs:
                    changes.append(f"Class: {element.attrs['class']}")
            return f"Inspected the web application at {url} and identified changes: {', '.join(changes)}"
        except Exception as e:
            return f"Failed to inspect the web application: {e}"

class ScriptEditorTool(BaseTool):
    name: str = "Script Editor"
    description: str = "Edits the given script to update it with new locators or fix issues."

    def _run(self, script_path: str, changes: str) -> str:
        try:
            with open(script_path, "a") as script_file:
                script_file.write("\n" + changes)
            return "Script updated successfully."
        except Exception as e:
            return f"Failed to update script: {e}"

class ScriptGeneratorTool(BaseTool):
    name: str = "Script Generator"
    description: str = "Generates new automation scripts based on the given requirements."

    def _run(self, requirements: str) -> str:
        script_content = f"# Generated script based on requirements:\n# {requirements}\n\nprint('Script running')"
        script_path = "./generated_script.py"
        try:
            with open(script_path, "w") as script_file:
                script_file.write(script_content)
            return f"Script generated successfully and saved to {script_path}."
        except Exception as e:
            return f"Failed to generate script: {e}"

class VersionControlTool(BaseTool):
    name: str = "Version Control"
    description: str = "Manages version control for automation scripts, such as committing changes."

    def _run(self, commit_message: str) -> str:
        try:
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            return f"Changes committed with message: {commit_message}"
        except Exception as e:
            return f"Failed to commit changes: {e}"
