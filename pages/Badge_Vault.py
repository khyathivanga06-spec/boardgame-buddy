import streamlit as st

st.set_page_config(
    page_title="Badge Vault",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Badge Vault")
st.markdown("""
<div style="
background:linear-gradient(
135deg,
#FACC15,
#FB7185
);
padding:25px;
border-radius:20px;
text-align:center;
color:black;
">

<h2>🏆 Hall of Fame</h2>

<p>
Collect badges and become the ultimate Board Game Master!
</p>

</div>
""", unsafe_allow_html=True)
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