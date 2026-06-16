from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    model_kwargs={
        "device_map": None,
        "torch_dtype": "auto"
    },
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
    }

)


model = ChatHuggingFace(llm=llm)


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    result =model.invoke(user_input)
    raw_content = result.content
    cleaned = raw_content.split('<|start_header_id|>assistant<|end_header_id|>')[-1]
    # Then remove any trailing tags
    cleaned = cleaned.split('<|eot_id|>')[0].strip()
    print("Assistant:", cleaned)