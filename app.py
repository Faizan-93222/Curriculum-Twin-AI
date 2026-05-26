import streamlit as st
import pandas as pd
import os
import csv
from datetime import datetime

from twin_ai import create_learning_dna, predict_friction_points
from optimizer import optimize_curriculum
from curriculum_data import get_curriculum
from copilot_ai import copilot_assist

# ------------------ PAGE SETUP ------------------
st.set_page_config(page_title="Curriculum Twin AI", layout="centered")
st.title("🧠 Curriculum Twin AI")
st.write("Predict, personalize, and adapt learning before failure happens.")

# ------------------ STEP 1: LEARNING DNA ------------------
st.subheader("1️⃣ Create Your Learning DNA")

attention = st.selectbox("Attention Span", ["short", "medium", "long"])
content = st.selectbox("Preferred Content Format", ["video", "text"])
difficulty = st.selectbox("Difficulty Comfort Level", ["low", "medium", "high"])

# ------------------ STEP 2: GENERATE CURRICULUM ------------------
if st.button("Generate My Curriculum"):
    st.session_state.curriculum = get_curriculum()
    st.session_state.dna = create_learning_dna(attention, content, difficulty)

    st.session_state.friction = predict_friction_points(
        st.session_state.dna,
        st.session_state.curriculum
    )

    st.session_state.optimized = optimize_curriculum(
        st.session_state.curriculum,
        st.session_state.friction
    )

# ------------------ SHOW RESULTS ------------------
if "optimized" in st.session_state:
    st.subheader("📘 Original Curriculum")
    st.table(st.session_state.curriculum)

    st.subheader("⚠️ Predicted Friction Points")
    st.write(st.session_state.friction if st.session_state.friction else "No major friction 🎉")

    st.subheader("✅ Optimized Curriculum")
    st.table(st.session_state.optimized)

# ------------------ STEP 3: COPILOT AI ASSISTANT ------------------
st.divider()
st.subheader("🤖 AI Copilot Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_area("Talk to your AI Copilot (free text feedback / commands)")

if st.button("AI Assist"):
    st.session_state.messages.append(("user", user_input))

    updated, explanation = copilot_assist(
        user_input,
        st.session_state.optimized
    )

    st.session_state.optimized = updated
    st.session_state.messages.append(("ai", explanation))

# ------------------ CHAT HISTORY ------------------
for role, msg in st.session_state.messages:
    if role == "user":
        st.write("👤 You:", msg)
    else:
        st.write("🤖 Copilot:", msg)

# ------------------ UPDATED CURRICULUM ------------------
if "optimized" in st.session_state:
    st.subheader("🔁 Updated Curriculum After AI Copilot")
    st.table(st.session_state.optimized)

# ------------------ STEP 4: USER FEEDBACK FORM ------------------
st.divider()
st.subheader("📝 Platform Feedback (Stored for Improvement)")

domain_id = st.text_input("Enter your Domain ID (student / teacher / admin)")
platform_feedback = st.text_area("Your feedback about the platform")

FEEDBACK_FILE = "user_feedback.csv"

def save_feedback(domain_id, feedback):
    file_exists = os.path.isfile(FEEDBACK_FILE)
    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "domain_id", "feedback"])
        writer.writerow([datetime.now(), domain_id, feedback])

if st.button("Submit Platform Feedback"):
    if domain_id.strip() == "" or platform_feedback.strip() == "":
        st.warning("Please fill both fields")
    else:
        save_feedback(domain_id, platform_feedback)
        st.success("Thank you! Your feedback has been saved ❤️")

# ------------------ ADMIN VIEW (OPTIONAL) ------------------
if os.path.exists(FEEDBACK_FILE):
    if st.checkbox("📊 Show collected feedback (admin view)"):
        df = pd.read_csv(FEEDBACK_FILE)
        st.dataframe(df)

# ------------------ FOOTER ------------------
st.caption("Curriculum Twin AI • Predictive + Copilot-style Adaptive Learning System")
