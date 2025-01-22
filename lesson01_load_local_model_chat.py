from llama_index.llms.ollama import Ollama

llm = Ollama(model="qwen2.5:32b-instruct-q8_0", temperature=0.75, request_timeout=360.0)

# ollama version does not match arg of 'usage'
# token_counts = self._get_response_token_counts(response)
# if token_counts:
#     response["usage"] = token_counts
result = llm.complete('你好，今天天气怎么样')

print(result)