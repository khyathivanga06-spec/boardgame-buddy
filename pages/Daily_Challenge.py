import streamlit as st
import random
from utils import load_css, sidebar_brand, hero_banner
st.set_page_config(
    page_title="Daily Challenge",
    page_icon="🎯",
    layout="wide"
)

load_css()
sidebar_brand()
hero_banner(
    "🎯 Daily Challenge",
    "Complete Challenges • Earn XP • Improve Skills"
)

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