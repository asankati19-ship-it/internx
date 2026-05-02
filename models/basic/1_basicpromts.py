from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
)

cm = ChatHuggingFace(llm=endpoint)

topic = input("Enter topic: ")
number_of_lines = input("Enter number of lines: ")
style = input("Enter style: ")
language = input("Enter language: ")
print()

system_prompt = f"You are a helpful assistant. You need to answer the questions in {style} form and in {number_of_lines} lines only about {topic} in {language}"

result = cm.invoke(system_prompt)

print(result.content)