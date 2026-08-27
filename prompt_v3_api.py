# USING API TO MAKE RESPONSE FASTER

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.title("JOSH PROMPT ANALYZER V2")
prompt = st.text_input("Enter Your Prompt: ")
button = st.button("Analyze Prompt")

# RUNNIG THE API BY USING THE HF TOKEN(HF_TOKEN)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)
# GIVING THE SYSTEM INSTRUCTIONS TO FOLLOW
completion = client.chat.completions.create(
    model="zai-org/GLM-5.3-Flash:novita",
    messages=[
        {
            "role": "system",
            "content": "you are a prompt analysis assistant. Analyze the user's prompt and help make it clearer, more specific and useful."
            "Analyze this: "
            "Goal - is the user's main goal clear?."
            "Context - is enough relevant context provided?."
            "Specificity - is the request clear and actionable?."
            "Missing Information - what important information is missing?."
            "Feedback - what is good and what could be improved?."
            "Score - give a score of the user's prompt out of 100."
            "Imoroved Prompt - Rewrite the prompt to make it betterand if neccessary use the missing information to improve it. Dont give the user exactly what they input as the prompt, unless it's it has nothing to be improve"
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
            "Specificity:"
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

        {
        
         "role": "user",
         "content": prompt
        },
    ]

)
# USING STREAMLIT TO SHOW USERS THE RESPONSE
if button:
    many = completion.choices[0].message.content
    st.write(many)
elif not button:
    st.write("please input the prompt")
