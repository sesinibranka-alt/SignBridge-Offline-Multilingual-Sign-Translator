# SignBridge Architecture

```text
Sign-language Video / Webcam
            |
            v
      Frame Processing
            |
            v
 Hand / Pose Feature Extraction
            |
            v
  Local Sign Recognition Model
            |
            v
     Intermediate Meaning
            |
            v
  Offline / Local Translation
            |
            +------> Text
            |
            +------> Text-to-Speech
```

The model layer is deliberately modular so a validated sign-language model can be deployed and optimized for the target Snapdragon platform.
