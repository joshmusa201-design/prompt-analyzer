# SECOND VERSION OF THE PROMPT ANALYZER USINNG A OPEN SOURCE MODEL FROM HUGGING FACE AND RUNNING IT LOCALLY AND GET RESPONSE
from transformers import AutoModelForCausalLM, AutoTokenizer
import streamlit as st

st.title("JOSH PROMPT ANALYZER")
model_name = "Qwen/Qwen3-0.6B"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
with st.form(key="prompt analyzer"):
    prompt = st.text_input("enter your prompt here: ") 
    #submit = st.form_submit_button("Analyze Prompt")


#with st.form(key="prompt analyzer"): 
    #okay = st.file_uploader("enter your prompt here: ")


#passing the model with the instructions it has to follow to generate the output and make it to be more efficient 
messages = [
     {"role": "system", "content": "you are a prompt analysis assistant. Analyze the user's prompt and help make it clearer, more specific and useful."
     "Analyze this: "
     "Goal - is the user's main goal clear?."
     "Context - is enough relevant context provided?."
     "Specificity - is the request clear and actionable?."
     "Missing Information - what important information is missing?."
     "Feedback - what is good and what could be improved?."
     "Score - give a score of the user's prompt out of 100."
     "Imoroved Prompt - Rewrite the prompt to make it better."
     "Suggestions - give optional ideas that could make the user's project or results better."
     ""
     "RULES:"
     "1. preserve all information the user explicitly provided."
     "2. Never change numbers, dates, names, locations, technologies, features, requirements, or constraints."
     "3. Never remove important information from the improved prompt."
     "4. Do not invent requirements and present them as if the user requested them."
     "5. Use only the user's information when creating the improved prompt aslso with the missing information to make it much better."
     "6. Put new ideas that were not requested under suggestions. "
     "7. Missing information means important details needed to understand or complete the requets."
     "8. If the prompt is already clear, specific and actionable, say so."
     "9. Do not keep finding new problems just to make an already good promt better."
     "10. Always provide suggestions."
     "11. Do not simply repeat the original prompt as feedback."
     "12. Dont force improvement. If the prompt is already clear and complete, say so and dont rewrite it unnecessary."
     "13. Only call something 'missing' if it's neccessary. Put option ideas under 'suggestion'."
     "Always Return the responses in this exact format. Always:"
     "Goal: "
     ""
     "Context: "
     ""
     "Speecificity:"
     " "
     "Missing Information: "
     ""
     "Feedback:"
     " "
     "Score: /100"
     ""
     "Improved Prompt:"
     " "
     "Suggestions: "
     },

     {"role":"user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False# Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=2000
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

# parsing thinking content
try:
    # rindex finding 151668 (</think>)
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

if submit:
    thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
    content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
    st.write(content)
elif not submit:
    st.write("please input click on the analyzer button")





















