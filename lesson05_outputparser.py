from llama_index.core.output_parsers import LangchainOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema, JsonOutputToolsParser
from llama_index.llms.ollama import Ollama

response_schemas = [
    ResponseSchema(
        name="sql",
        description=(
            "查询mysql数据库的sql语句"
        ),
    ),
    ResponseSchema(
        name="database",
        description=(
            "假设的数据库表名"
        ),
    )
]

lc_output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
output_parser = LangchainOutputParser(lc_output_parser)

fmt_prompt = """你是mysql数据库查询语句生成专家，根据用户的问题，生成可以查询数据库的sql语句。
注意：数据库表名和字段名都是英文。
用户的问题：查询张三的数学成绩和历史成绩"""
fmt_qa_tmpl = output_parser.format(fmt_prompt)
print(fmt_qa_tmpl)

llm = Ollama(model="qwen2.5:latest", temperature=0.75)
response = llm.complete(fmt_qa_tmpl)
result = output_parser.parse(response.text)

print(result)