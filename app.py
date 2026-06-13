import streamlit as st

st.set_page_config(
    page_title="BoardGame Buddy",
    page_icon="🎲",
    layout="wide"
)

st.title("🎲 BoardGame Buddy")
st.subheader("Learn Board Games in Minutes")

st.markdown("""
Welcome to BoardGame Buddy!

📚 Learn board games quickly

🎥 Watch tutorials

🧠 Test yourself with quizzes

🏆 Earn badges and track progress

Use the sidebar to explore the app.
""")

st.markdown("---")

st.header("🌟 Featured Games")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/Chess.jpg")
    st.caption("Chess")

with col2:
    st.image("assets/uno.jpg")
    st.caption("Uno")

with col3:
    st.image("assets/monopoly.jpg")
    st.caption("Monopoly")