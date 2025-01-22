from llama_index.llms.ollama import Ollama
from llama_index.core.tools.tool_spec.base import BaseToolSpec

class CustomToolSpec(BaseToolSpec):
    """Custom tool spec."""

    spec_functions = [
        "multiply",
        "add",
    ]

    # function tools
    def multiply(self, a: float, b: float) -> float:
        """计算两个数的乘积，返回计算的结果"""
        return a * b

    def add(self, a: float, b: float) -> float:
        """计算两个数的和，返回计算的结果"""
        return a + b

tools = CustomToolSpec().to_tool_list()

llm = Ollama(model="qwen2.5:latest", temperature=0.75)
response = llm.chat_with_tools(tools=tools, user_msg="3+5等于多少？") # 你是谁？ / 3+5等于多少？
tool_selections = llm.get_tool_calls_from_response(response=response, error_on_no_tool_call=False)

print('response:', response.message.content)
print('tools call:', tool_selections)