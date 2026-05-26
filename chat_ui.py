import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("🤖 AI Learning Assistant")

user_input = st.text_input("Ask me anything about your curriculum")

if st.button("Send"):
    st.session_state.messages.append(("user", user_input))

    # simple AI response
    ai_reply = f"I understand you said: '{user_input}'. I will help optimize your learning."
    st.session_state.messages.append(("ai", ai_reply))

for role, msg in st.session_state.messages:
    if role == "user":
        st.write("👤 You:", msg)
    else:
        st.write("🤖 AI:", msg)
