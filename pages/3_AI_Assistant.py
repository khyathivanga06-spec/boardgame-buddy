import streamlit as st

st.title("🤖 BoardGame Buddy AI")

question = st.text_area(
    "Ask a question about a board game"
)

if st.button("Ask AI"):

    if question:

        st.success(
            f"""
            Example Response:

            {question}

            Imagine you're teaching a 10-year-old.

            Board games are easier when you focus on the goal first,
            then learn the rules step by step.
            """
        )
