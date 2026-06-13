import streamlit as st

st.title("📊 Progress Dashboard")

st.metric(
    "Games Completed",
    0
)

st.progress(0)

st.write("Complete quizzes to earn badges!")

st.markdown("### 🏆 Badges")

st.write("🔒 Chess Master")
st.write("🔒 Uno Champion")
st.write("🔒 Monopoly Expert")
