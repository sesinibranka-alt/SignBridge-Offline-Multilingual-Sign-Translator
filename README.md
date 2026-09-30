# SignBridge

## Offline Multilingual Sign Language Video Translator

SignBridge is a proof-of-concept accessibility application that accepts a sign-language video or webcam input and is designed to produce a recognized meaning, multilingual text and optional voice output.

### Current MVP
- Streamlit user interface
- Video upload
- Local video preprocessing
- Frame/duration inspection
- Output-language selection
- Replaceable local AI inference component
- Clear separation between prototype UI and validated model inference

### Planned AI pipeline
Video/Webcam -> Frame Processing -> Hand/Pose Features -> Sign Recognition Model -> Intermediate Meaning -> Translation -> Text/Speech

### Snapdragon deployment
The architecture is designed so the recognition model can be replaced by a Qualcomm AI Hub / compatible on-device model and optimized for Snapdragon hardware. Do not claim Snapdragon performance until the model is actually validated on supported Snapdragon hardware.

### Important scope
The initial MVP is not a complete translator for every sign language. A validated dataset and trained/optimized recognition model are required before making broad recognition-accuracy claims.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Suggested next development steps
1. Select a validated sign-language dataset.
2. Train or fine-tune a temporal sign-recognition model.
3. Export/convert the model to a Snapdragon-compatible format.
4. Validate inference on supported Qualcomm hardware.
5. Add offline translation and text-to-speech models.
6. Evaluate accuracy, latency and privacy behavior.
