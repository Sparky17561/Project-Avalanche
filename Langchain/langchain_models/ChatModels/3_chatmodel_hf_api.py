from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Parameters go DIRECTLY in the HuggingFaceEndpoint constructor
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    provider="auto",
    max_new_tokens=100,  # Moved out of pipeline_kwargs
    temperature=0.5,      # Moved out of pipeline_kwargs
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESSS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

try:
    result = model.invoke("What is the capital of India?")
    print(result.content)
except Exception as e:
    print(f"Error: {e}")