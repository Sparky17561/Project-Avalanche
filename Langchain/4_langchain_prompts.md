What are the input instructions or queries given to a model to guide its output 

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
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

template = PromptTemplate(
    template = """
                Please summarize the research paper titled "{paper_input}" with the following specifications:
                Explanation Style: {style_input}
                Explanation Length: {length_input}

                1. Mathematical Details:
                Include relevant mathematical equations if present in the paper.
                Explain the mathematical concepts using simple, intuitive code snippets where applicable.

                2. Analogies:
                Use relatable analogies to simplify complex ideas.
                If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing. Ensure the summary is clear, accurate, and aligned with the provided style and length.
            """,
            input_variables=['paper_input','style_input','length_input']
)


# fill the placeholders 

prompt = template.invoke({'paper_input': paper_input,'style_input':style_input,'length_input':length_input})



if st.button('summarize'):
    raw_content = model.invoke(prompt)
    print(raw_content)
    cleaned = raw_content.split('<|start_header_id|>assistant<|end_header_id|>')[-1]
    # Then remove any trailing tags
    cleaned = cleaned.split('<|eot_id|>')[0].strip()
    st.write(cleaned)
    # This looks for everything after the assistant header





# to run streamlit ->  streamlit run prompt_ui.py


Prompt Template


A PromptTemplate in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template. Instead of hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different inputs.

This makes it reusable, flexible, and easy to manage, especially when working with dynamic user inputs or automated workflows.

Why use PromptTemplate over f strings?

Default validation

Reusable

LangChain Ecosystem

# in main file
template = load_prompt('template.json') # to dynamically load prompts 


# in prompt file 

from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    template = """
                Please summarize the research paper titled "{paper_input}" with the following specifications:
                Explanation Style: {style_input}
                Explanation Length: {length_input}

                1. Mathematical Details:
                Include relevant mathematical equations if present in the paper.
                Explain the mathematical concepts using simple, intuitive code snippets where applicable.

                2. Analogies:
                Use relatable analogies to simplify complex ideas.
                If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing. Ensure the summary is clear, accurate, and aligned with the provided style and length.
            """,
            input_variables=['paper_input','style_input','length_input']
)



template.save('template.json')