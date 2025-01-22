from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core.agent import ReActAgent
from llama_index.core.tools.tool_spec.base import BaseToolSpec

class CustomToolSpec(BaseToolSpec):
    """Custom tool spec."""

    spec_functions = [
        "multiply",
        "add",
    ]

    def __init__(self) -> None:
        """Initialize the Custom tool spec."""

    # function tools
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and returns the product"""
        return a * b

    def add(self, a: float, b: float) -> float:
        """Add two numbers and returns the sum"""
        return a + b


Settings.llm = Ollama(model="qwen2.5:latest", temperature=0.75)

tools = CustomToolSpec().to_tool_list()
agent = ReActAgent.from_tools(tools, verbose=True)

response = agent.chat("What is 2+3?")

print(response)