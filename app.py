import streamlit as st

st.set_page_config(
    page_title="BoardGame Buddy",
    page_icon="🎲",
    layout="wide"
)

st.title("🎲 BoardGame Buddy")
st.subheader("Learn Board Games in Minutes")

search = st.text_input("Search a board game")

if search:
    st.write(f"You searched for: {search}")

st.markdown("---")

st.header("Popular Games")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Chess")

with col2:
    st.button("Uno")

with col3:
    st.button("Monopoly")