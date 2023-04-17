import openai
import streamlit as st
from util.util import chat

st.header("Message Tester")
st.markdown("Crafting the perfect message is essential for engaging voters and promoting your campaign. Our Message Testing Bot helps you refine your messaging by testing how different demographics might respond.")
st.markdown("\nNOTE: this is an experimental feature, and cannot provide an accurate account of how voters might respond.")

speech = st.text_area("Speech:")
col1, col2, col3, col4 = st.columns(4)
with col1:
    age = st.selectbox("Age", ("Young adult", "Adult", "Senior"))
with col2:
    gender = st.selectbox("Gender", ("Male", "Female", "Other"))
with col3:
    race = st.selectbox("Race", ("White/Caucasian", "Black/African-American", "Hispanic/Latino",
                          "Asian", "Native American/Alaska Native", "Native Hawaiian/Pacific Islander"))
with col4:
    geography = st.selectbox("Geography", ("Urban", "Suburban", "Rural"))

if st.button("Message Test"):
    sys = [{
        "role": "system",
        "content": f"You are a {age}, {gender}, {race}, {geography} person voting in 2024."
                   f"How would you respond to this candidate's speech, GIVEN YOUR DEMOGRAPHICS?"
                   f"What do you like about it, and what would you improve?"
    }]
    summary = chat(speech, messages=sys, model="gpt-4", max_tokens=500)
    st.write(summary)
