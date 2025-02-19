from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool,FileReadTool,FileWriterTool,DirectorySearchTool
AIPROXY_TOKEN = ""
AIPROXY_BASE_URL = "https://aiproxy.sanand.workers.dev/openai/v1"
file_read_tool = FileReadTool(file_path='latest_ai_development/src/latest_ai_development/config/info.md')
# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class LatestAiDevelopment():
	"""LatestAiDevelopment crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	
	@agent
	def Coder(self) -> Agent:
		return Agent(
			config=self.agents_config['Coder'],
			verbose=True,
			llm=LLM(model="gpt-4o-mini",  base_url=AIPROXY_BASE_URL,  api_key=AIPROXY_TOKEN),
			allow_code_execution=True,
			tools=[CodeInterpreterTool(),FileWriterTool(),file_read_tool,DirectorySearchTool()]
		)

	
	# @agent
	# def A_Agent(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['A_Agent'],
	# 		verbose=True,
	# 		llm=LLM(model="ollama/llama3.2:1b", base_url="http://localhost:11434")
	# 	)

	# @agent
	# def B_Agent(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['B_Agent'],
	# 		verbose=True,
	# 		llm=LLM(model="ollama/llama3.2:1b", base_url="http://localhost:11434")
	# 	)


	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def coding_task(self) -> Task:
		return Task(
			config=self.tasks_config['coding_task'],
		)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		output_file='report.md'
	# 	)

	@crew
	def crew(self) -> Crew:
		"""Creates the LatestAiDevelopment crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
