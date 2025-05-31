import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI Resume Optimizer & Career Advisor")
st.write("Paste your resume below and get instant AI-powered suggestions!")

resume_text = st.text_area("Your Resume:", height=300)

if st.button("Optimize Resume"):
    if resume_text.strip():
        with st.spinner("Analyzing your resume..."):
            prompt = f"""
            You are a professional career advisor. Analyze this resume and suggest:
            - Improvements in structure and clarity
            - Keywords to add for job visibility
            - Tone changes for professionalism
            - Roles the candidate is suitable for

            Resume:
            \"\"\"{resume_text}\"\"\"
            """
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500
            )
            st.markdown("### ✅ AI Suggestions:")
            st.markdown(response["choices"][0]["message"]["content"])
    else:
        st.error("Please paste your resume first.")
