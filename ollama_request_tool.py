import requests
from superagi.tools.base_tool import BaseTool
from superagi.models.task import Task

class OllamaRequestTool(BaseTool):
    name = "Ollama Tool"
    description = "Sends prompts to a locally running Ollama instance and retrieves responses"
    agent_required = False

    def _execute(self, task: Task, *args, **kwargs):
        prompt = kwargs.get("prompt", "Say something profound")
        model = kwargs.get("model", "llama3")  # Alternatives: mistral, gemma, etc.

        response = requests.post("http://trapscholar.netbird.cloud:11434/api/generate", json={
            "model": model,
            "prompt": prompt
        })
        return response.json().get("response", "No response from Ollama.")
