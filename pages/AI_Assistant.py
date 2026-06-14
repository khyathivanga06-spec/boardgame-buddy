import streamlit as st
import google.generativeai as genai
st.set_page_config(
    page_title="AI Coach",
    page_icon="🤖",
    layout="wide"
)
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

st.title("🤖 BoardGame Buddy AI Coach")
st.markdown("""
<div style="
background:linear-gradient(135deg,#8B5CF6,#06B6D4);
padding:25px;
border-radius:20px;
text-align:center;
color:white;
">

<h2>🎮 Your Personal Board Game Coach</h2>

<p>
Ask questions and learn games like a pro!
</p>

</div>
""", unsafe_allow_html=True)
st.markdown("""
Ask me anything about board games!

Examples:

• How do I play Chess?

• Explain Uno

• Give me Monopoly tips

• What is Tangram?

• How do I build Jodo?
""")

question = st.text_input(
    "Ask your question"
)

if st.button("🚀 Ask Coach"):

    if question:

        with st.spinner(
            "🤖 Thinking..."
        ):

            prompt = f"""
            You are BoardGame Buddy AI.

            Help children learn board games.

            Explain things simply.

            Give clear beginner-friendly answers.

            Question:
            {question}
            """

            response = model.generate_content(
                prompt
            )

            st.markdown(
                f"""
                <div style="
                background:#151C2E;
                padding:20px;
                border-radius:20px;
                margin-top:10px;
                ">
                {response.text}
                </div>
                """,
                unsafe_allow_html=True
            )