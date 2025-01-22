from llama_index.llms.ollama import Ollama
from llama_index.core.base.llms.types import ChatMessage

llm = Ollama(model="qwen2.5:latest", temperature=0.75)

messages = [
    ChatMessage(role="system", content="你是安徽大学开发的AI助手，尽自己所能回答用户的问题。"),
    ChatMessage(role="user", content="你是谁？"),
    ChatMessage(role="assistant", content="我是由安徽大学开发的AI助手，致力于提供准确、有用的信息来帮助您解决问题或获取知识。有什么我可以帮助你的吗？"),
    ChatMessage(role="user", content="我是张三"),
    ChatMessage(role="assistant", content="""您好，张三！很高兴为您服务。请问您需要什么样的帮助呢？无论是信息查询、问题解答还是其他需求，都可以随时告诉我。"""),
    ChatMessage(role="user", content="我是谁"),
]

response = llm.chat(messages=messages)
print(response.message.content) # 您是张三。如果您有具体的问题或需要帮助，请告诉我，我会尽力提供支持。
