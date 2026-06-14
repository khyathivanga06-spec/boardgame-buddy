import streamlit as st
from utils import load_css, sidebar_brand, hero_banner

st.set_page_config(
    page_title="Badge Vault",
    page_icon="🏆",
    layout="wide"
)
load_css()
sidebar_brand()
hero_banner(
    "🏆 Badge Vault",
    "Collect badges and become the ultimate Board Game Master!"
)

st.markdown("""
Collect badges by:

✅ Learning games

✅ Completing quizzes

✅ Finishing challenges

✅ Earning XP
""")

st.divider()

# -------------------
# BADGES
# -------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
    ♟️ Chess Master

    Complete the Chess Quiz
    """)

with col2:

    st.success("""
    🃏 Uno Champion

    Complete the Uno Quiz
    """)

with col3:

    st.success("""
    🏠 Monopoly Expert

    Complete the Monopoly Quiz
    """)

st.write("")

col4, col5, col6 = st.columns(3)

with col4:

    st.info("""
    🧩 Tangram Builder

    Complete the Tangram Challenge
    """)

with col5:

    st.info("""
    🏗️ Jodo Engineer

    Complete the Jodo Challenge
    """)

with col6:

    st.warning("""
    🌟 BoardGame Hero

    Earn 500 XP
    """)

st.divider()

st.subheader("⭐ Progress")

if "xp" not in st.session_state:
    st.session_state["xp"] = 250

xp = st.session_state["xp"]

st.progress(min(xp / 1000, 1.0))

st.write(f"Current XP: {xp}")

if xp >= 500:

    st.balloons()

    st.success(
        "🏆 BoardGame Hero Badge Unlocked!"
    )

else:

    st.warning(
        f"Earn {500 - xp} more XP to unlock BoardGame Hero!"
    )