import streamlit as st
from PIL import Image
import io
import os

# --- Page Config ---
st.set_page_config(page_title="Rakshabandhan Quiz", page_icon="🎉", layout="centered")

# --- Custom Styling ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #fff8e7; /* cream */
    color: #4b2e2e; /* dark maroon */
    font-family: 'Trebuchet MS', sans-serif;
}
[data-testid="stHeader"] {
    background: none;
}
h1, h2, h3, h4, h5, h6, p {
    color: #4b2e2e !important;
}
select, input[type="text"] {
    background-color: white !important;
    color: black !important;
    border: 2px solid #4b2e2e !important;
}
button[kind="primary"] {
    background-color: #4b2e2e !important;
    color: #fff8e7 !important;
    border: 2px solid #4b2e2e !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Questions for each sister ---
questions_map = {
    "DEEKSHA": [
        {"q": "Which is AADI's favourite song in the following?", "options": ["Bismil", "Golden Brown", "Dangal", "Wavy"], "ans": "Bismil"},
        {"q": "Which is AADI's favourite subject?", "options": ["Physics", "Maths", "Computer Science", "All of the above"], "ans": "Computer Science"},
        {"q": "Which is AADI's favourite web series?", "options": ["Game of Thrones", "The Family Man", "Breaking Bad", "F.R.I.E.N.D.S."], "ans": "Game of Thrones"}
    ],
    "DEEPANSHI": [
        {"q": "Which of the following is AADI's favourite food?", "options": ["Aloo shimlamirch", "Arvi", "Aloo soya badi", "Baingan ka bharta"], "ans": "Arvi"},
        {"q": "Who is AADI's favourite actor?", "options": ["Christian Bale", "Brad Pitt", "Manoj Bajpayee", "Morgan Freeman"], "ans": "Brad Pitt"},
        {"q": "Which is AADI'S favourite car?", "options": ["Mustang GT", "Dodge Charger 1969", "Mustang 1969", "Scorpio N"], "ans": "Dodge Charger 1969"}
    ],
    "RISHU": [
        {"q": "Which is AADI's favourite Hollywood movie?", "options": ["Harry Potter", "The Odyssey", "Pirates of the Caribbean", "Dangal"], "ans": "Harry Potter"},
        {"q": "Who is AADI's favourite actress?", "options": ["Helena Bonham Carter", "Emma Stone", "Alia Bhatt", "Emma Watson"], "ans": "Helena Bonham Carter"},
        {"q": "Which type of vehicle does AADI like the most?", "options": ["Car", "Bike", "Cycle", "Tractor"], "ans": "Bike"}
    ]
}

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "name"
    st.session_state.username = ""
    st.session_state.score = 0

# --- Name Selection Page ---
if st.session_state.page == "name":
    st.title("🎉 Rakshabandhan Quiz 🎉")
    name = st.selectbox("Select your name:", ["DEEKSHA", "DEEPANSHI", "RISHU"])
    if st.button("Submit"):
        st.session_state.username = name
        st.session_state.page = "quiz"
        st.rerun()

# --- Quiz Page ---
elif st.session_state.page == "quiz":
    st.title(f"🎉 Welcome {st.session_state.username}! 🎉")
    st.write("Answer the 3 questions below:")

    score = 0
    for i, q in enumerate(questions_map[st.session_state.username]):
        st.subheader(f"Q{i+1}: {q['q']}")
        choice = st.radio("Select your answer:", q["options"], key=f"q{i}")
        if choice == q["ans"]:
            score += 1

    if st.button("Submit"):
        st.session_state.score = score
        st.session_state.page = "result"
        st.rerun()

# --- Result Page ---
elif st.session_state.page == "result":
    st.title("🎉 Rakshabandhan Quiz Result 🎉")

    # Build filename based on name + score
    filename = f"{st.session_state.username}_{st.session_state.score}.jpg"
    filepath = os.path.join("C:\\PYTHON", filename)

    try:
        img = Image.open(filepath)
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.image(img, caption="Your Rakhi Result Card")
        st.download_button("📥 Download Result Image", data=byte_im, file_name=filename, mime="image/jpeg")
    except FileNotFoundError:
        st.error(f"Result card image not found at {filepath}. Please check the file exists.")

    st.write("PLEASE SHARE THIS WITH ADITYA TO RECEIVE YOUR GIFT :)")
