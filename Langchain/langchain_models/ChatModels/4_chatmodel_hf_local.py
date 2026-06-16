from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(temperature=0.5,max_new_tokens=100)
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("What is the capital of India")

print(res.content)