import openai
import streamlit as st
from util.util import chat

st.header("Fictional Focus Group")
st.markdown("Crafting the perfect message is essential for engaging voters and promoting your campaign. Our Fictional Focus Group helps you refine your messaging by testing how different demographics might respond to your platform, ad, or email.")
st.markdown("\nNOTE: this is an experimental feature, and cannot provide an accurate account of how voters might respond.")

speech = st.text_area("Text:")

if st.button("Generate"):
    sys = [{
        "role": "system",
        "content": "Simulate a long, American focus group transcript for the following candidate message." 
        "Include 10 participants, make them diverse in geography, partisanship, gender, race, age, and occupation, and describe them briefly."
        "BE REALISTIC. Some of the people should be critical and disagree. Do not make it fake or overly positive. Markdown:" 
    }]
    transcript = chat(speech, messages=sys, model="gpt-4", max_tokens=1000)
    st.write(transcript)
