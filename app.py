import streamlit as st
import cv2
import tempfile
from pathlib import Path

st.set_page_config(page_title="SignBridge", page_icon="🤝", layout="centered")

st.title("🤝 SignBridge")
st.subheader("Offline Multilingual Sign Language Video Translator")

st.info(
    "Proof-of-concept interface. The recognition model is intentionally kept "
    "as a replaceable local component so a validated sign-language model can "
    "be deployed and optimized for Snapdragon hardware."
)

language = st.selectbox(
    "Output language",
    ["English", "Tamil", "Hindi", "French", "Spanish"]
)

mode = st.radio("Input mode", ["Upload Video", "Live Camera"])

if mode == "Upload Video":
    video = st.file_uploader(
        "Upload a sign-language video",
        type=["mp4", "mov", "avi", "mkv"]
    )

    if video:
        st.video(video)

        if st.button("Analyze Video"):
            with st.spinner("Processing locally..."):
                suffix = Path(video.name).suffix or ".mp4"
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
                    f.write(video.read())
                    video_path = f.name

                cap = cv2.VideoCapture(video_path)
                frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                fps = cap.get(cv2.CAP_PROP_FPS) or 1
                duration = frames / fps
                cap.release()

            st.success("Video preprocessing completed.")
            st.write(f"Frames detected: {frames}")
            st.write(f"Approximate duration: {duration:.2f} seconds")

            st.warning(
                "Recognition model placeholder: connect a validated local "
                "sign-language model here before claiming full sign-language translation."
            )

            st.text_input("Recognized meaning", value="HELLO", key="demo_meaning")
            st.write(f"Selected output language: **{language}**")
            st.caption("Prototype demo output. Replace with model inference for evaluated results.")

else:
    st.warning(
        "Live camera mode is a UI placeholder in this MVP. "
        "Connect the same local recognition pipeline to webcam frames."
    )
    st.button("Start Camera")

st.divider()
st.caption("SignBridge • Designed for offline-first, privacy-aware on-device AI.")
