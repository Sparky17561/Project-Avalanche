import re 



raw_output= """
content='<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nCutting Knowledge Date: December 2023\nToday Date: 16 Feb 2026\n\n<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nPlease summarize the research paper titled "Attention is all you need" with the following specifications:\n                Explanation Style: Explain me as I am a 10 year old\n                Explanation Length: Medium (3-4 Lines)\n\n                1. Mathematical Details:\n                Include relevant mathematical equations if present in the paper.\n                Explain the mathematical concepts using simple, intuitive code snippets where applicable.\n\n           
     2. Analogies:\n                Use relatable analogies to simplify complex ideas.\n                If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing. Ensure the summary is clear, accurate, and aligned with the provided style and length.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nI\'d be happy to explain the research paper "Attention is all you need" to you.\n\n**Mathematical Details:**\n\nThe paper discusses the concept of attention and its role in human perception. It suggests that attention is not just a passive process, but an active one that involves the brain\'s ability to selectively focus on certain aspects of the environment. The researchers found that attention is not just limited to the visual cortex, but also involves the prefrontal cortex and other brain regions. They also' additional_kwargs={} response_metadata={} id='lc_run--019c6580-e7d6-7f72-943b-f7e2e1efb88e-0' tool_calls=[] invalid_tool_calls=[]
""" # Your raw string
# This regex finds everything between the assistant header and the end of the string
clean_match = re.search(r'<\|start_header_id\|>assistant<\|end_header_id\|>(.*)', raw_output, re.DOTALL)

if clean_match:
    result = clean_match.group(1).strip()
    # If there are trailing tokens like <|eot_id|>, remove them:
    result = result.split('<|')[0].strip()
    print(result)