import streamlit as st
from utils import load_css

st.set_page_config(
    page_title="AI Coach",
    page_icon="🤖",
    layout="wide"
)

load_css()


st.markdown("""
<div style="
background:linear-gradient(135deg,#8B5CF6,#06B6D4);
padding:40px;
border-radius:25px;
            margin-bottom:25px;
            box-shadow:0px 0px 40px rgba(6,182,212,0.4);
text-align:center;
color:white;
">

<h1 style="
color:white;
font-size:56px;
font-weight:800;
margin-bottom:10px;
">
🤖 AI Coach
</h1>

<h2 style="
color:white;
font-size:28px;
">
Your Personal Board Game Coach
</h2>

<p>
Ask questions and learn games like a pro!
</p>

</div>
""", unsafe_allow_html=True)

st.info("""
💡 Ask about:

♟️ Chess

🃏 Uno

🏠 Monopoly

🧩 Tangram

🏗️ Jodo

🔤 Scrabble

🏝️ Catan

🚂 Ticket to Ride
""")

question = st.text_input(
    "🎯 Ask your board game question",
    placeholder="How do I play Chess?"
)
if st.button(
    "🚀 Ask Coach",
    use_container_width=True
):

    q = question.lower()

    # CHESS

    if "chess" in q:

        st.success("""
♟️ Chess Coach

Goal:
Checkmate your opponent's king.

Beginner Tips:

• Control the center.

• Develop knights and bishops early.

• Castle your king for safety.

• Don't move the same piece too many times.

Think of Chess like planning an adventure before making your move.
""")

    # UNO

    elif "uno" in q:

        st.success("""
🃏 Uno Coach

Goal:
Be the first player to get rid of all cards.

Tips:

• Save your wild cards.

• Watch what colors opponents need.

• Remember to say UNO when one card remains.

Uno is all about timing and surprises!
""")

    # MONOPOLY

    elif "monopoly" in q:

        st.success("""
🏠 Monopoly Coach

Goal:
Become the richest player.

Tips:

• Buy properties early.

• Build houses quickly.

• Don't spend all your money.

• Railroads are valuable.

Think like a property investor!
""")

    # TANGRAM

    elif "tangram" in q:

        st.success("""
🧩 Tangram Coach

Goal:
Create shapes using all seven pieces.

Tips:

• Start with the large triangles.

• Use all seven pieces.

• Pieces may touch.

• Pieces must not overlap.

Practice makes you faster!
""")

    # JODO

    elif "jodo" in q:

        st.success("""
🏗️ Jodo Coach

Goal:
Build structures using sticks and connectors.

Tips:

• Start with simple shapes.

• Build strong foundations.

• Connect pieces carefully.

• Experiment with your own designs.

Think like an engineer!
""")

    # SCRABBLE

    elif "scrabble" in q:

        st.success("""
🔤 Scrabble Coach

Goal:
Create words and score points.

Tips:

• Use bonus squares.

• Save valuable letters.

• Create multiple words at once.

Think strategically before placing tiles.
""")

    # CATAN

    elif "catan" in q:

        st.success("""
🏝️ Catan Coach

Goal:
Reach 10 victory points.

Tips:

• Collect resources early.

• Trade wisely.

• Build roads quickly.

• Watch where opponents expand.
""")

    # TICKET TO RIDE

    elif "ticket" in q or "ride" in q:

        st.success("""
🚂 Ticket to Ride Coach

Goal:
Complete train routes.

Tips:

• Finish destination tickets.

• Claim important routes early.

• Block opponents when possible.

Plan ahead!
""")

    else:

        st.info("""
🤖 I'm your BoardGame Buddy Coach!

Try asking:

• How do I play Chess?

• Explain Uno

• Monopoly tips

• What is Tangram?

• How do I build Jodo?
""")