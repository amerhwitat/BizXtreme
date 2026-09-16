# BizXtreme Media AI

Provider-neutral speech, audio, voice-control and camera/CV layer.

Supported integration families:
- Whisper and Vosk for ASR.
- WAV/PortAudio-compatible recording and GStreamer/native playback adapters.
- OpenCV for camera capture, preprocessing, edges, tracking and classical CV.
- MediaPipe for optional face, hand/gesture, pose, object and segmentation tasks.
- OCR/barcode/QR and model-backed detection adapters can consume the same frame contract.

Microphone and camera are off by default. Network upload is disabled by default. State-changing voice commands require confirmation.
