from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    temperature=1.7
)

cm = ChatHuggingFace(llm=endpoint)

result = cm.invoke("Where is the Eiffel Tower?")

print(result.content)