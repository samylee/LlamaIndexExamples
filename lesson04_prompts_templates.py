from llama_index.llms.ollama import Ollama
from llama_index.core import PromptTemplate

qa_prompt_tmpl_str = """\
Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge, answer the query.
Please write the answer in the style of {tone_name}
Query: {query_str}
Answer: \
"""

prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)

partial_prompt_tmpl = prompt_tmpl.partial_format(tone_name="Shakespeare")
fmt_prompt = partial_prompt_tmpl.format(
    context_str="In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters",
    query_str="How many params does llama 2 have",
)

llm = Ollama(model="qwen2.5:latest", temperature=0.75)
response = llm.complete(fmt_prompt)

print(response)