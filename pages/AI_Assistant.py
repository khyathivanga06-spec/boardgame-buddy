import streamlit as st

st.title("🤖 BoardGame Buddy AI Coach")

question = st.text_input(
    "Ask me about any game"
)

if st.button("Ask Coach"):

    q = question.lower()

    if "chess" in q:

        st.success("""
♟️ Chess Tip

Control the center of the board.

Protect your king.

Develop your pieces early.
""")

    elif "uno" in q:

        st.success("""
🎨 Uno Tip

Save special cards for later.

Don't forget to say UNO when one card remains.
""")

    elif "monopoly" in q:

        st.success("""
🏠 Monopoly Tip

Buy properties early.

The more properties you own,
the more rent you collect.
""")

    elif "tangram" in q:

        st.success("""
🧩 Tangram Tip

Use all seven pieces.

Pieces can touch but never overlap.
""")

    elif "jodo" in q:

        st.success("""
🏗️ Jodo Tip

Start with simple shapes.

Then combine them into larger structures.
""")

    else:

        st.info("""
I'm your BoardGame Buddy Coach!

Try asking:

• How do I play Chess?
• Explain Uno
• Monopoly tips
• What is Tangram?
""")
