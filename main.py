# import streamlit as st
from voice_utils import record_audio_google_stt, synthesize_speech
from agents import get_agent
import os
import streamlit as st
st.set_page_config(page_title="🎓 AI Tutor Avatar", layout="wide")
st.title("🎓 प्रोफेसर नील - AI Tutor (Hindi)")

# ⏳ Persist the agent in session
if "agent" not in st.session_state:
    st.session_state.agent = get_agent()

# Load CSS animation
with open("assets/waveform.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🎙️ बोलिए (Speak Your Question)"):
        user_query = record_audio_google_stt()
        if user_query:
            st.markdown(f"**आपने पूछा:** {user_query}")
            with st.spinner("AI सोच रहा है..."):
                response = st.session_state.agent.run(user_query)
                st.markdown(f"**प्रोफेसर नील:** {response}")
                audio_path = synthesize_speech(response)

                with col2:
                    st.markdown("### 🔊 प्रोफेसर उत्तर दे रहे हैं...")
                    st.markdown('<div class="circle-wave"></div>', unsafe_allow_html=True)
                    with open(audio_path, "rb") as audio_file:
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/mp3")
