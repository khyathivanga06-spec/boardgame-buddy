import streamlit as st

st.set_page_config(
    page_title="BoardGame Buddy AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 BoardGame Buddy AI Assistant")

st.markdown("""
Ask me anything about board games!

Examples:
- How do I win in Chess?
- What is the goal of Tangram?
- Is Uno easy for beginners?
- How many players can play Monopoly?
""")

question = st.text_area(
    "Ask your question"
)

if st.button("🚀 Ask AI"):

    if question:

        q = question.lower()

        if "chess" in q:
            answer = """
Chess is a strategy game for 2 players.
The goal is to checkmate your opponent's king.
Try controlling the center of the board and protecting your king.
"""

        elif "uno" in q:
            answer = """
Uno is a fast card game.
Match cards by color or number.
Don't forget to say UNO when you have one card left!
"""

        elif "monopoly" in q:
            answer = """
Monopoly is about buying properties and collecting rent.
The goal is to become the richest player and bankrupt your opponents.
"""

        elif "tangram" in q:
            answer = """
Tangram is a puzzle game.
Use all seven pieces to create shapes and figures.
It helps improve creativity and problem-solving skills.
"""

        elif "jodo" in q:
            answer = """
Jodo is a construction and creativity game.
Players use colorful sticks and connectors to build structures.
It encourages imagination and teamwork.
"""

        else:
            answer = f"""
Great question!

{question}

A good way to learn any board game is:

1. Understand the goal.
2. Learn the setup.
3. Practice a few turns.
4. Have fun and learn as you play.
"""

        st.success(answer)

    else:
        st.warning("Please enter a question first.")
