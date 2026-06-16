from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
import re
load_dotenv()

st.header("Research Tool")


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

# user_input = st.text_input("Enter your prompt: ")

paper_input = st.selectbox("Select: Research Paper Name",["Attention is all you need","Word2Vec"])

style_input = st.selectbox("Select : Explanation Style",["Beginner-Friendly","Technical","Explain me as I am a 10 year old"])

length_input=st.selectbox("Select explanation length",["Short (1-2 Lines)","Medium (3-4 Lines)","Detailed (8-10 lines)"])

template = load_prompt('template.json') # to dynamically load prompts 

# fill the placeholders 

# prompt = template.invoke({'paper_input': paper_input,'style_input':style_input,'length_input':length_input})



if st.button('summarize'):
    chain = template | model 
    result = chain.invoke({'paper_input': paper_input,'style_input':style_input,'length_input':length_input}) # using chains .. rather than invoking seperately for prompt template and model .. we tied them and used a single invoke using chaining 
    # res = model.invoke(prompt) traditional way
    # raw_content = res.content
    raw_content = result.content

    print(raw_content)
    cleaned = raw_content.split('<|start_header_id|>assistant<|end_header_id|>')[-1]
    # Then remove any trailing tags
    cleaned = cleaned.split('<|eot_id|>')[0].strip()
    st.write(cleaned)
    # This looks for everything after the assistant header





# to run streamlit ->  streamlit run prompt_ui.py