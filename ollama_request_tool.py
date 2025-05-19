import requests
from superagi.tools.base_tool import BaseTool

class OllamaRequestTool(BaseTool):
    name = "Ollama Tool"
    description = "Sends prompts to a locally running Ollama instance and retrieves responses"
    agent_required = False

    def _execute(self, *args, **kwargs):
        prompt = kwargs.get("prompt", "Say something profound")
        model = kwargs.get("model", "llama3")  # Alternatives: mistral, gemma, etc.

        response = requests.post("http://gpu.tsc.tekoda.cloud:11434/api/generate", json={
            "model": model,
            "prompt": prompt
        })
        return response.json().get("response", "No response from Ollama.")
