import streamlit as st
from ai_agent import analyze_code

st.title("🧠 Code Helper AI Agent 🤖")

code = st.text_area("Enter your code here:")

if st.button("Analyze"):
    if code.strip() == "":
        st.warning("Please enter some code")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_code(code)

        st.subheader("Result")
        st.write(result)
