import streamlit as st
import random

st.title("🎯 Daily Challenge")

challenges = [
    "Score 100% in Chess Quiz",
    "Learn Tangram",
    "Watch a Monopoly Tutorial",
    "Complete Uno Quiz",
    "Learn a New Game Today",
    "Build a Jodo House",
    "Create a Tangram Animal"
]

challenge = random.choice(challenges)

st.success(
    f"Today's Challenge:\n\n{challenge}"
)

if st.button("Completed!"):
    st.balloons()
    st.success("🏆 Challenge Completed!")