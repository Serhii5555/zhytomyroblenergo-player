import cv2
import numpy as np
import json
import subprocess

def video_to_binary_json_and_audio(video_path, output_json, output_audio):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Rescale to 48x12
        resized = cv2.resize(gray, (48, 12), interpolation=cv2.INTER_AREA)

        # Convert to binary 
        _, binary = cv2.threshold(resized, 127, 1, cv2.THRESH_BINARY_INV)

        frames.append(binary.tolist())

    cap.release()

    data = {
        "fps": fps,
        "frames": frames
    }

    with open(output_json, "w") as f:
        json.dump(data, f)

    print(f"✅ Frames saved to {output_json}")
    print(f"Total frames: {len(frames)}, FPS: {fps:.2f}")

    try:
        subprocess.run([
            "ffmpeg",
            "-i", video_path,
            "-vn",         
            "-acodec", "mp3",
            "-y",          
            output_audio
        ], check=True)
        print(f"✅ Audio saved to {output_audio}")
    except subprocess.CalledProcessError:
        print("❌ Error extracting audio. Make sure ffmpeg is installed and in PATH.")

video_to_binary_json_and_audio("input.mp4", "output.json", "audio.mp3")
